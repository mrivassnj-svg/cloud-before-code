# Five-Minute Demonstration Script
## Cloud Before Code — Lesson 6: Who Can Change the Menu?

> **Purpose:** This script guides a five-minute live demonstration of Lesson 6's teaching sequence. It is designed for a class presentation or project showcase. All timing is approximate. Adapt the language to your natural speaking style.
>
> **What you need:** Printed or projected copies of the LunchRush Access Policy and the blank permissions table (pages from the learner workbook). Participants do not need to have read anything in advance.

---

## At a Glance

| Segment | What happens | Time |
|---------|-------------|------|
| Setup | Introduce the scenario | 0:30 |
| Exploratory task | Participants write their initial thinking | 0:45 |
| Vocabulary reveal | Introduce two terms | 1:00 |
| Main activity | Complete one row of the permissions table | 1:30 |
| Understanding check | One question | 0:30 |
| Closing statement | Describe the design | 0:45 |
| **Total** | | **~5:00** |

---

## Full Script

---

### Setup (0:00–0:30)

**What I say:**

> "I'm going to walk you through five minutes of Lesson 6. You're going to be a learner for a moment, so I'd like you to actually engage with this. Ready?
>
> Here's the situation: LunchRush is a small food-ordering business. Last night, someone changed the price of an item on the menu. No one knows who did it. Jordan, the owner, asks: 'Wait — does everyone on the team have access to everything?'
>
> Before I teach you any vocabulary, I want you to think about this question for thirty seconds."

**What participants do:** Listen and prepare to respond.

---

### Exploratory Task (0:30–1:15)

**What I say:**

> "Think about your workplace, your school, or any organization you've been part of. When different people need access to different things — files, systems, rooms — how does the organization decide who gets what?
>
> Write one sentence: What principle or question would you use to decide what access a person should have?"

**What participants do:** Write one sentence individually (30 seconds), then one or two volunteers share aloud.

**What I say (after responses):**

> "What you're describing — giving people what they need and not more — is a real security principle. And there's a name for it. I'll tell you in a moment."

---

### Vocabulary Reveal (1:15–2:15)

**When terminology is revealed:** After participants have already articulated the concept themselves.

**What I say:**

> "Let me introduce two terms.
>
> First: **authentication**. That's the process of verifying who someone is. When you log in with a username and password, the system is authenticating you. It's checking: 'Are you who you say you are?'
>
> Second: **authorization**. That's what happens after authentication. The system already knows who you are — now it decides: 'What are you allowed to do?'
>
> These two are often confused. Authentication is 'Who are you?' Authorization is 'What can you do?'
>
> And that principle you described a moment ago — giving people only the access they need — that's called **least privilege**. It's the foundation of good access design."

**What participants do:** Write the definitions in their own words (or in the demo context, listen and take mental note).

---

### Main Activity (2:15–3:45)

**What participants receive:** The LunchRush Access Policy and the blank permissions table.

**What I say:**

> "Here's LunchRush's access policy. Read it quickly — thirty seconds.
>
> *(Allow 30 seconds.)*
>
> Now I want you to fill in just one row: **Riley**, the delivery coordinator.
>
> For each resource in the table, write R for read, W for write, or a dash for no access. Apply least privilege: give Riley only what Riley needs to do the job.
>
> You have sixty seconds."

**What participants do:** Complete the Riley row on the permissions table.

**What I say (after 60 seconds):**

> "Let's check a few. What did you give Riley for 'delivery status'? ... And for 'menu item prices'? ...
>
> Here's the expected answer: Riley gets **W** for delivery status — that's the job. And Riley gets **—** for menu item prices — not needed. If Riley had write access to prices, we'd have no guarantee Sam changed that price last night, not Riley.
>
> That's least privilege in action."

---

### Understanding Check (3:45–4:15)

**What I say:**

> "Quick check — one question.
>
> True or false: The cloud provider is responsible for making sure Sam can't change menu prices.
>
> Think for ten seconds, then raise your hand for true or raise your hand for false."

**What participants do:** Indicate true or false.

**What I say (after responses):**

> "False. Under what's called **shared responsibility**, the cloud provider secures the physical infrastructure and the platform. But the access policies we just built? Those are LunchRush's responsibility — not the provider's. That distinction matters a lot in real cloud security."

---

### Closing Statement (4:15–5:00)

**What I say:**

> "What you just experienced is Lesson 6 in compressed form. Notice the sequence: I didn't start with 'today we're learning IAM.' I started with a business problem — a price that got changed. You articulated a solution in plain language before I introduced any vocabulary. And then you applied the vocabulary immediately in a realistic activity.
>
> That's the core design of this curriculum: explain it before you name it, then explain it twice — once in plain language, once using the right vocabulary.
>
> I'm not claiming this design is proven. What I can say is that it's deliberate, it's consistent across all eight lessons, and I've built it to be pilotable with real learners using nothing more than a printed worksheet.
>
> Thank you."

---

## Notes for the Presenter

- **If you run long:** Cut the exploratory task to 20 seconds and do not ask for volunteers to share. Go directly from the prompt to: "You were probably thinking something like..."
- **If you run short:** Extend the shared discussion after participants complete the Riley row. Ask: "Did anyone put something different for 'customer order details'? Why?"
- **If a participant gives an unexpected answer:** Accept it and ask them to explain their reasoning. "Tell me more about why you gave Riley read access to financial records." This demonstrates the 'accept justified alternatives' principle live.
- **If participants don't engage:** Read the exploratory prompt aloud, give them 20 seconds of silence, then say: "If you're not sure, that's exactly the right starting point for this lesson."

---

*[This script is for a demonstration of one portion of Lesson 6. The full lesson runs 24–26 minutes and includes vocabulary for all five terms: authentication, authorization, IAM, least privilege, and shared responsibility.]*
