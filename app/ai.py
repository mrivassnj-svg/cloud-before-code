import httpx
import json
from sqlalchemy.orm import Session
from database import Term

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"


def _ask(prompt: str, timeout: int = 45) -> str:
    """Send a prompt to Ollama and return the response text."""
    try:
        r = httpx.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=timeout,
        )
        r.raise_for_status()
        return r.json().get("response", "").strip()
    except Exception as e:
        return f"[AI unavailable: {e}]"


def probe_and_rank(lesson_number: int, probe_answer: str, db: Session) -> dict:
    """
    Given a learner's free-text probe answer and the lesson's terms,
    ask the LLM to:
      1. Identify which terms the learner already seems to understand.
      2. Identify which terms they seem uncertain or wrong about.
      3. Return a ranked list (most-needed first) and brief personalised feedback.

    Returns:
        {
          "feedback": str,           # conversational reply to the learner
          "ranked_term_ids": [int],  # term IDs, most-needed first
          "understood_words": [str], # terms the learner already has
          "unclear_words": [str],    # terms to reinforce
        }
    """
    terms = db.query(Term).filter(Term.lesson_id == lesson_number, Term.essential == 1).all()
    term_list = "\n".join(f"- {t.word}: {t.plain}" for t in terms)

    prompt = f"""You are a friendly cloud-computing tutor helping a beginner.

The learner is about to study Lesson {lesson_number}. Before seeing any vocabulary,
they answered this exploratory question in their own words:

LEARNER'S ANSWER:
\"\"\"{probe_answer}\"\"\"

The lesson covers these terms (term: plain-language meaning):
{term_list}

Your job:
1. Write 2-3 sentences of warm, encouraging feedback that connects what the learner said to what they're about to learn. Be specific — reference words they actually used. Do NOT use jargon yet.
2. List the terms they seem to already understand (even partially), comma-separated, on a line starting with "UNDERSTOOD:"
3. List the terms they seem unclear or wrong about, comma-separated, on a line starting with "UNCLEAR:"

Keep feedback under 60 words. If their answer was very brief or off-topic, still be encouraging and list all terms as UNCLEAR.
"""

    raw = _ask(prompt)

    # Parse the structured output
    feedback_lines = []
    understood = []
    unclear = []

    for line in raw.splitlines():
        line = line.strip()
        if line.upper().startswith("UNDERSTOOD:"):
            understood = [w.strip() for w in line.split(":", 1)[1].split(",") if w.strip()]
        elif line.upper().startswith("UNCLEAR:"):
            unclear = [w.strip() for w in line.split(":", 1)[1].split(",") if w.strip()]
        else:
            feedback_lines.append(line)

    feedback = " ".join(feedback_lines).strip()
    if not feedback:
        feedback = "Great start — let's explore these ideas together."

    # Rank term IDs: unclear terms first, then understood, preserve DB order within groups
    understood_lower = {w.lower() for w in understood}
    unclear_lower = {w.lower() for w in unclear}

    unclear_ids = [t.id for t in terms if t.word.lower() in unclear_lower]
    understood_ids = [t.id for t in terms if t.word.lower() in understood_lower]
    # any terms not mentioned go to the unclear bucket
    mentioned = unclear_lower | understood_lower
    unmentioned_ids = [t.id for t in terms if t.word.lower() not in mentioned]

    ranked = unclear_ids + unmentioned_ids + understood_ids

    # fall back to natural order if parsing failed
    if not ranked:
        ranked = [t.id for t in terms]

    return {
        "feedback": feedback,
        "ranked_term_ids": ranked,
        "understood_words": understood,
        "unclear_words": unclear,
    }


def explain_it_back(term_word: str, term_definition: str, learner_response: str) -> dict:
    """
    After a learner types their explanation of a term, check it and give feedback.
    Returns {"score": "strong"|"developing"|"beginning", "comment": str, "missed": [str]}
    """
    prompt = f"""You are a friendly cloud-computing tutor.

The learner was asked to explain the term "{term_word}" in their own words.
The correct definition is: "{term_definition}"

The learner wrote:
\"\"\"{learner_response}\"\"\"

Assess their explanation:
1. Write one SHORT sentence of specific feedback (under 25 words). Be encouraging but honest.
2. On a new line write: SCORE: strong OR SCORE: developing OR SCORE: beginning
   - strong = captures the core idea accurately
   - developing = partially correct or missing one key idea
   - beginning = missing the core idea or confused

Do not repeat the definition back to them verbatim.
"""
    raw = _ask(prompt, timeout=30)

    score = "developing"
    comment_lines = []
    for line in raw.splitlines():
        l = line.strip()
        if l.upper().startswith("SCORE:"):
            val = l.split(":", 1)[1].strip().lower()
            if val in ("strong", "developing", "beginning"):
                score = val
        else:
            if l:
                comment_lines.append(l)

    comment = " ".join(comment_lines).strip() or "Keep going — you're on the right track."
    return {"score": score, "comment": comment}
