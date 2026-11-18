# Slide Content and Speaker Notes
## Cloud Before Code — 10-Slide Class Presentation

> **How to use this document:** Each slide section contains the slide title, the text that appears on the slide, and the speaker notes. Speaker notes are for the presenter's reference — they do not appear on the slide itself. Adapt the notes to your natural speaking style.

---

## Slide 1 — Title

**Slide title:** Cloud Before Code

**Slide body text:**
> Learn Cloud Computing Through a Business Story
>
> A scenario-based curriculum for beginners
>
> *[Student name] | [Course name] | [Date]*

**Speaker notes:**

"Good [morning/afternoon]. Today I'm presenting a curriculum project called Cloud Before Code. The subtitle is 'Learn Cloud Computing Through a Business Story.' The core idea is simple: before learners encounter any cloud vocabulary, they work through the problem in everyday language first. I'll walk you through the structure, the design choices, the sample activities, and how I plan to evaluate it. Let's start with the problem this curriculum tries to solve."

---

## Slide 2 — The Problem

**Slide title:** Why Does Vocabulary Stop Beginners?

**Slide body text:**

- Cloud-computing resources often lead with terminology.
- Learners see: *bucket*, *container*, *IAM*, *serverless* — before they know what problem each solves.
- The result: surface-level memorization, not genuine understanding.
- The goal: give learners a reason to care about a term before they learn it.

**Speaker notes:**

"If you've ever tried to learn cloud computing from documentation or a certification guide, you may have experienced this. The vocabulary is dense and highly interconnected. 'What is a bucket?' leads to 'What is object storage?' which leads to 'What is a database?' — and suddenly you're 20 terms deep with no context for why any of it matters.

This curriculum tries to flip that. Every lesson starts with a business problem the learner can relate to, and only introduces the technical vocabulary after the learner has already tried to solve the problem in plain language. The term gets meaning before it gets a name."

---

## Slide 3 — Audience and Objectives

**Slide title:** Who Is This For?

**Slide body text:**

**Audience:**
- Students and nontechnical adults
- No prior cloud-computing experience required
- No coding, cloud accounts, or software installations required

**Three fully developed lessons teach learners to:**
- Distinguish object storage from a database
- Describe virtual machines, containers, and serverless compute
- Distinguish authentication from authorization; apply least-privilege access control

**Speaker notes:**

"The primary audience is people who want foundational cloud literacy without an engineering background. That includes students in this kind of introductory course, career changers, and anyone who works near cloud technology but hasn't had a formal introduction to it.

I want to emphasize the constraints I designed around: no coding, no cloud accounts, no paid services. Everything works on paper or in a text document. This keeps the barrier to entry extremely low for both the learner and whoever facilitates the lesson.

The three fully developed lessons address storage, compute options, and identity and access management. Each lesson has measurable objectives — I'll show you what those look like in a moment."

---

## Slide 4 — The Curriculum Concept

**Slide title:** Three Design Features

**Slide body text:**

**1. Explain it before you name it**
Every lesson begins with a problem in plain language.

**2. Explain it twice**
Learners explain each solution twice:
- To Jordan (the business owner) — no jargon
- To Alex (the technology helper) — correct vocabulary

**3. The jargon journal**
For each key term, learners complete a five-part entry:
- Definition, plain-language meaning, LunchRush application, analogy limitation, open question

**Speaker notes:**

"These three features are the backbone of every lesson. The first feature is about sequencing — the problem always comes before the term.

The 'explain it twice' task is the most important for consolidating understanding. It's easy to recognize a term when you see it; it's much harder to explain it accurately in two different registers. When learners try to explain 'serverless' to a nontechnical business owner versus a technical colleague, they discover quickly whether they understand it or just recognize it.

The jargon journal is a personal glossary with an important twist: every entry includes an explicit statement of where the analogy stops being accurate. Analogies are helpful, but they can also create misconceptions if learners take them too literally. For example, calling serverless 'like a vending machine' is useful up to a point — but a vending machine doesn't scale to serve thousands of users simultaneously. Making that limitation explicit is part of building accurate understanding."

---

## Slide 5 — The Eight-Lesson Journey

**Slide title:** LunchRush's Eight Challenges

**Slide body text:**

| Lesson | Challenge | Key vocabulary |
|--------|-----------|----------------|
| 1 | Going online | Cloud computing, client, server |
| **2** ★ | Storing menus and orders | Object storage, database |
| **3** ★ | Running the application | VM, container, serverless |
| 4 | How an order travels | DNS, HTTP, API |
| 5 | Handling the noon rush | Scaling, load balancing |
| **6** ★ | Who can change the menu | Authentication, authorization, IAM |
| 7 | Releasing an update safely | Pipeline, CI/CD |
| 8 | Investigating slow orders | Monitoring, metrics, logs |

★ Fully developed lesson

**Speaker notes:**

"The curriculum follows one business — LunchRush — through eight challenges. The business starts with nothing and gradually builds toward a more sophisticated cloud setup. Each lesson is self-contained, but the story accumulates.

Three lessons are fully developed into ready-to-use packs: Lessons 2, 3, and 6. The other five are concise teaching outlines that give an instructor or a future developer enough to build from.

The choice of these three was deliberate. Storage, compute options, and identity and access management are foundational concepts that connect to almost every other cloud topic. If a learner understands these three well, they have a framework for approaching the remaining five."

---

## Slide 6 — The Teaching Sequence

**Slide title:** How Every Lesson Works

**Slide body text:**

Each lesson follows six steps:

1. **Encounter the business problem** — in plain language
2. **Attempt a plain-language solution** — before any vocabulary
3. **Discover the cloud terminology** — with accurate definitions and analogy limitations
4. **Apply the vocabulary** — in a hands-on activity
5. **Explain the solution twice** — without jargon, then with vocabulary
6. **Check understanding** — three-question exit assessment

**Speaker notes:**

"This is the core teaching loop, and it repeats in every lesson. I want to highlight step 2 specifically — the exploratory task. Learners write their initial thinking before they hear any vocabulary. This isn't a trick. It's a deliberate move to activate prior knowledge and give learners a stake in the new vocabulary. When I then introduce the term 'object storage,' the learner already has a mental hook: 'Oh, that's the name for what I was describing when I said a safe place to drop files.'

Step 5 — explain it twice — happens before the exit assessment. It's not just a final check; it's a learning activity. The act of trying to explain something in plain language and then in technical language deepens encoding.

Step 6 is a quick three-question check: one recitation, one application, and one clarification question that addresses a common misconception. I'll show you what this looks like in Lesson 6 during the demo."

---

## Slide 7 — Sample Activity: Lesson 6

**Slide title:** Who Can Change the Menu? (Lesson 6 Activity)

**Slide body text:**

**The scenario:** Sam changed a menu price by accident. Jordan realizes no one has formally decided who can access what.

**Business policy (stated before the activity):**
- Jordan: view and change anything.
- Sam: menu content only; no financial access.
- Riley: orders and delivery status only.
- Alex: technical configuration; no customer payment data during normal operations.

**The activity:** Complete a permissions table using R (read), W (write), or — (no access).

**Key principle applied:** Least privilege — give each person only the access they need.

**Speaker notes:**

"This is Lesson 6's main activity. Before learners hear the terms 'authentication,' 'authorization,' or 'IAM,' they work through the opening story — an incident where a price was changed without authorization. They already understand why this is a problem.

Then they're given this four-character, eight-resource permissions table and a business policy. The table is intentionally not fully obvious. For example, should Alex have read access to customer order details for debugging purposes? The business policy says no during normal operations — but a learner who argues 'yes, with appropriate logging' gets credit for a justified answer.

This is the 'accept justified alternatives' principle. Access control policy design has genuine trade-offs. I don't want learners to think there's always one correct answer — I want them to reason from a stated policy.

After the table, learners complete the 'explain it twice' task, and then the exit assessment."

---

## Slide 8 — Assessments

**Slide title:** How Understanding Is Measured

**Slide body text:**

**Pre-test:** 6 questions before lessons begin
**Post-test:** 6 different but comparable questions after lessons

Question types:
- Multiple choice (4 questions) — including "I'm not sure yet"
- Short answer (2 questions)

**"Explain it twice" rubric:** 3-level scale (Beginning / Developing / Strong)

**Feedback survey:** 5 questions, mix of rating and open text

**Question-to-objective alignment table** included

**Speaker notes:**

"The assessment package includes everything needed to measure learning and collect feedback in a pilot session. The pre-test and post-test are six questions each. They're different questions but assess the same objectives — this matters for a valid pre/post comparison.

I included an 'I'm not sure yet' option on multiple-choice questions. This is deliberate. A learner who selects 'I'm not sure yet' on the pre-test is giving me useful information — they're not guessing. That's more informative than a 50-50 guess.

The 'explain it twice' rubric is a three-level formative scale, not a high-stakes grade. I designed it to give learners and facilitators useful feedback about whether explanations are strong, developing, or just beginning.

The question-to-objective alignment table makes it easy to see which questions assess which lessons — important for a pilot where you want to know exactly which concepts learners struggled with."

---

## Slide 9 — Evaluation Plan and Limitations

**Slide title:** How I Plan to Evaluate the Curriculum

**Slide body text:**

**Planned pilot:**
- 3–5 volunteers; no prior cloud experience
- One 60–75-minute session
- Pre-test → Lessons 2, 3, 6 → Post-test → Feedback survey

**What I will collect:**
- Pre/post scores (per participant)
- Activity completion observations
- Rubric scores for "explain it twice"
- Timing data
- Survey responses and facilitator notes

**Limitations:**
- Small convenience sample
- No control group
- Short-term recall only; no retention follow-up
- Results describe this group; do not generalize

**Speaker notes:**

"I want to be clear about what this evaluation can and cannot tell us. A pilot of three to five volunteers provides preliminary feedback about whether the materials work as written. It can tell me if instructions are confusing, if timing is off, if a particular activity is too hard or too easy. It cannot tell me whether this curriculum is effective for learners broadly.

I've included a full limitations section in the pilot evaluation plan precisely because I think it's important to be honest about scope. This is a student project, not a research study. The evaluation is designed to generate revision opportunities, not to prove anything.

The blank results templates are ready. I will fill them in only after running actual sessions with real volunteers. No invented data has been placed in the templates."

---

## Slide 10 — Deliverables and Next Steps

**Slide title:** What's in the Project

**Slide body text:**

**Completed deliverables:**
- Project overview | Curriculum map
- Instructor guide (3 full lessons + 5 outlines)
- Learner workbook (Lessons 2, 3, 6)
- Assessments and answer keys
- Pilot evaluation plan (blank templates)
- 10-slide presentation | 5-minute demo script
- Submission proposal
- Sources and verification checklist
- Production checklist

**Next steps:**
1. Verify technical definitions against authoritative sources.
2. Run a 3–5-person pilot session.
3. Document findings and revise materials.
4. Optionally develop full lesson packs for Lessons 1, 4, 5, 7, 8.

**Speaker notes:**

"Here's the complete deliverable list. Everything in the left column has been created as a Markdown document in a structured project folder. All technical content is labeled as a draft pending verification — that's intentional and honest.

The three next steps are the natural continuation of this project: verify the definitions, run the pilot, revise the materials. These are future tense because they haven't happened yet. I'd rather be accurate about what this project is — a complete, structured curriculum draft — than overstate it as a tested and proven product.

Thank you. I'm happy to take questions, and I have a five-minute live demonstration of Lesson 6 ready to show if you'd like to see the teaching sequence in action."

---

*[Student: customize slide 1 with your name, course, and date before presenting. All other content can be used as written or paraphrased.]*
