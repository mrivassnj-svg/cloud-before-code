# Assessments and Answer Keys
## Cloud Before Code — LunchRush Curriculum

> **For instructor use.** This document contains the pre-test, post-test, answer keys, scoring instructions, the "explain it twice" rubric, and the learner feedback survey. Do not distribute the answer keys or scoring notes to learners before they complete the assessments.

---

## Question-to-Objective Alignment Table

| Question | Test | Lesson | Objective tested |
|----------|------|--------|------------------|
| Pre-Q1 / Post-Q1 | Both | L2 | Distinguish object storage from a database |
| Pre-Q2 / Post-Q2 | Both | L2 | Identify an appropriate storage type for a given item |
| Pre-Q3 / Post-Q3 | Both | L3 | Describe serverless compute accurately |
| Pre-Q4 / Post-Q4 | Both | L3 | Compare VM and container at a basic level |
| Pre-Q5 / Post-Q5 | Both | L6 | Distinguish authentication from authorization |
| Pre-Q6 / Post-Q6 | Both | L6 | Apply least-privilege principle to a scenario |

*All questions assess objectives taught in Lessons 2, 3, and 6 only.*

---

---

# PRE-TEST

> **To the learner:** This short quiz checks what you already know before the lessons begin. There are no wrong answers — honest uncertainty is useful information. For any question you're not sure about, circle "I'm not sure yet" or write "I don't know." Your score on this test is not a grade.

---

**Question 1 (Multiple choice)**

LunchRush needs to store 50 menu photos so customers can view them online. Which type of storage is best suited for this?

- A) A database
- B) Object storage
- C) A spreadsheet
- D) I'm not sure yet

---

**Question 2 (Multiple choice)**

Which of the following data items would be BEST stored in a database?

- A) A video of Jordan welcoming customers (MP4)
- B) A scanned copy of LunchRush's business license (PDF)
- C) A record of every customer order: name, items, time, and delivery address
- D) I'm not sure yet

---

**Question 3 (Multiple choice)**

What does the term "serverless" mean in cloud computing?

- A) The application runs without using any computers.
- B) The developer does not manage the servers; the cloud provider handles them.
- C) The application does not need an internet connection.
- D) I'm not sure yet

---

**Question 4 (Short answer)**

Describe one difference between a virtual machine and a container. Use your own words. If you're not sure, write "I'm not sure yet."

> _______________________________________________________________
>
> _______________________________________________________________

---

**Question 5 (Multiple choice)**

Riley logs into the LunchRush system by entering a username and password. What is this process called?

- A) Authorization
- B) Encryption
- C) Authentication
- D) I'm not sure yet

---

**Question 6 (Short answer)**

What does the principle of "least privilege" mean? Give one example. If you're not sure, write "I'm not sure yet."

> _______________________________________________________________
>
> _______________________________________________________________

---

---

# PRE-TEST ANSWER KEY

*(Instructor use only. Do not share with learners before or during assessment.)*

**Q1 — Correct answer: B) Object storage**

Rationale: Menu photos are files retrieved as whole units; object storage is designed for this. Databases are optimized for structured, searchable data. A spreadsheet is not a cloud storage service. If a learner answers A, note this as a common misconception to address in Lesson 2.

**Q2 — Correct answer: C) Order records**

Rationale: Order records contain structured fields (name, items, time, address) that need to be searched, filtered, and updated. A, B, and D are files best stored as whole objects in object storage.

**Q3 — Correct answer: B) Developer does not manage servers**

Rationale: This is the essential clarification about "serverless." Answer A is the most common misconception and should be addressed explicitly in Lesson 3.

**Q4 — Acceptable responses (short answer)**

Award credit for responses that capture at least one of the following ideas:
- A VM has its own operating system; a container shares the host OS.
- A VM simulates a full physical computer; a container is lighter and packages just the application and its dependencies.
- VMs provide stronger isolation; containers are more efficient.

Do not penalize learners for not knowing the technical terminology before Lesson 3.

**Q5 — Correct answer: C) Authentication**

Rationale: Logging in with credentials is authentication (verifying identity). Authorization happens after — it determines what the user is allowed to do. If a learner answers A, note this as a misconception to address in Lesson 6.

**Q6 — Acceptable responses (short answer)**

Award credit for responses that capture the core idea: giving a user only the access they need to do their job, nothing more.

Example: "Sam can edit the menu but can't see financial records because that's not part of Sam's job."

Partial credit: acknowledge the idea of "limiting access" even if the learner doesn't name the principle.

---

## Pre-Test Scoring Instructions

| Score | Interpretation |
|-------|----------------|
| 5–6 correct | Learner has prior cloud knowledge. The lessons will reinforce and formalize concepts. |
| 3–4 correct | Some prior knowledge. Lessons will fill in gaps. |
| 0–2 correct | No prior knowledge expected at this level. This is a normal starting point for this curriculum. |

**Important:** Pre-test scores are baseline data, not a measure of readiness or ability. All learners should proceed regardless of pre-test score.

---

---

# POST-TEST

> **To the learner:** This short quiz checks what you learned in Lessons 2, 3, and 6. Try each question on your own. If you're not sure, write your best answer and note your uncertainty.

---

**Question 1 (Multiple choice)**

Riley needs to look up all orders placed in the last hour and see the customer name, delivery address, and items for each one. Which storage type is best suited for this?

- A) Object storage
- B) A bucket
- C) A database
- D) I'm not sure yet

---

**Question 2 (Multiple choice)**

Which of the following data items would be BEST stored in object storage?

- A) A list of menu item prices that changes weekly
- B) The count of sandwiches remaining in inventory
- C) An audio message from Jordan welcoming new customers (MP3)
- D) I'm not sure yet

---

**Question 3 (Short answer)**

A classmate says: "If the app is serverless, there must be no servers involved." Write 2–3 sentences correcting this misunderstanding.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

**Question 4 (Multiple choice)**

LunchRush is packaging its application so it can run the same way on any cloud provider's infrastructure, without managing a full operating system. Which compute option does this describe?

- A) Virtual machine
- B) Container
- C) Database
- D) I'm not sure yet

---

**Question 5 (Short answer)**

Explain the difference between authentication and authorization. Use LunchRush as your example.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

**Question 6 (Multiple choice)**

Sam is a menu manager at LunchRush. Under the principle of least privilege, which set of permissions is most appropriate for Sam?

- A) Sam can view and change everything — menus, prices, orders, and financial records.
- B) Sam can view and change menu items and photos but cannot access financial records or pricing.
- C) Sam can only view menu items but cannot change anything.
- D) I'm not sure yet

---

---

# POST-TEST ANSWER KEY

*(Instructor use only.)*

**Q1 — Correct answer: C) A database**

Rationale: Riley needs to query structured data by time range and retrieve specific fields. This is a database use case. Object storage and buckets do not support this kind of structured query.

**Q2 — Correct answer: C) MP3 audio file**

Rationale: An audio file is retrieved as a whole unit and does not require searching inside it. A (menu prices) and B (inventory count) are structured data that changes and needs to be queried — better suited to a database.

**Q3 — Acceptable responses (short answer)**

Award full credit for responses that include both of the following ideas:
1. Servers do exist — the cloud provider runs them.
2. "Serverless" means the developer doesn't manage the servers; the provider handles provisioning and scaling.

Award partial credit for responses that include only one of the two ideas.

**Q4 — Correct answer: B) Container**

Rationale: Containers package an application and its dependencies to run consistently across environments. A VM includes a full OS. A database stores data, not running application code.

**Q5 — Acceptable responses (short answer)**

Award full credit for responses that:
- Define authentication as verifying identity (e.g., "Riley logs in with a password to prove who she is").
- Define authorization as determining what the authenticated user is allowed to do (e.g., "After logging in, Riley can update delivery status but not change the menu, because that's what she's authorized to do").

**Q6 — Correct answer: B**

Rationale: Sam's job is managing menu content. Least privilege means Sam gets exactly that access — not less (which would prevent Sam from doing the job) and not more (which would give unnecessary access to financial data or pricing).

---

## Post-Test Scoring Instructions

| Score | Interpretation |
|-------|----------------|
| 5–6 correct | Strong grasp of Lesson 2, 3, and 6 objectives. |
| 3–4 correct | Partial understanding; review areas with incorrect answers. |
| 0–2 correct | Re-visit the lessons; consider one-on-one clarification on the objectives missed. |

**Pre/Post comparison:** Calculate improvement per learner by subtracting the pre-test score from the post-test score. A gain of +2 or more points across six questions suggests the lessons addressed knowledge gaps. Gains and lack of gains are both informative; do not interpret a small pilot as proving or disproving effectiveness.

---

---

# "EXPLAIN IT TWICE" RUBRIC

This rubric applies to both the plain-language explanation (to Jordan) and the technical explanation (to Alex) produced in each lesson's worksheet.

---

## Plain-Language Explanation (To Jordan)

| Level | Description |
|-------|-------------|
| **3 — Strong** | Explains the concept clearly without using technical jargon. Uses an analogy or familiar example. The business owner could act on this explanation. |
| **2 — Developing** | Conveys the main idea but includes some jargon without explaining it, or the analogy is confusing or absent. |
| **1 — Beginning** | Mostly restates the technical term without explaining it in plain language, or the explanation is too vague to be useful. |

---

## Technical Explanation (To Alex)

| Level | Description |
|-------|-------------|
| **3 — Strong** | Uses at least three correct technical terms from the lesson. Demonstrates understanding of the concept, not just vocabulary recall. The explanation would make sense to a technical colleague. |
| **2 — Developing** | Uses some technical terms correctly but misuses or omits one or more key terms. The technical meaning is partially conveyed. |
| **1 — Beginning** | Uses few or no technical terms correctly, or the explanation does not demonstrate conceptual understanding. |

---

**Scoring note:** The "explain it twice" task is a learning activity, not a high-stakes assessment. Use the rubric for formative feedback, not for grading. Accept justified alternatives. Award Level 3 when the learner's explanation is accurate and shows understanding, even if it uses different vocabulary than the model response.

---

---

# LEARNER FEEDBACK SURVEY

> **To the learner:** Your feedback helps improve this curriculum. All responses are voluntary and there are no right or wrong answers. This survey is not graded.

---

**Question 1:** How would you rate the difficulty of the three lessons overall?

- Too easy
- About right
- Too hard
- I'm not sure

---

**Question 2:** Which part of the curriculum was most helpful for your learning?

*(Write as much or as little as you want.)*

> _______________________________________________________________
>
> _______________________________________________________________

---

**Question 3:** Was there anything that was confusing or unclear? If yes, please describe it.

*(Write as much or as little as you want.)*

> _______________________________________________________________
>
> _______________________________________________________________

---

**Question 4:** How useful was the "explain it twice" activity?

- Very useful — it helped me understand the vocabulary better
- Somewhat useful
- Not very useful
- I'm not sure

---

**Question 5:** Is there anything you would change or add to the curriculum?

*(Write as much or as little as you want.)*

> _______________________________________________________________
>
> _______________________________________________________________

---

*Thank you for your feedback.*

---

*[DRAFT — Assessment questions should be reviewed for alignment with final lesson content before use. Answer keys require verification against confirmed technical definitions.]*
