# Learner Workbook
## Cloud Before Code — LunchRush Curriculum

> **This workbook belongs to you.** Write in it, circle answers, and keep it as your personal record of what you learned. There are no trick questions. If you're not sure of an answer, write your best thinking and note your uncertainty — that counts too.

---

## Welcome

You're about to help a small food-ordering business called **LunchRush** solve eight real challenges — from storing menu photos to figuring out why orders are slow.

Before you meet any cloud-computing vocabulary, you'll try to solve each problem in plain language. After that, you'll learn the technical terms that describe what you just figured out. By the end of the three main lessons in this workbook, you'll be able to explain cloud concepts two ways: once to a friend who knows nothing about technology, and once to a technical colleague using the right vocabulary.

**The four people you'll be helping:**

| Name | Role |
|-------|-------------------------------|
| Jordan | Business owner |
| Sam | Menu and content manager |
| Riley | Delivery coordinator |
| Alex | Technology helper |

---

## Before You Start: Confidence Check

*Rate your current confidence with each statement. Circle one number. This is not a test — there are no right or wrong answers here.*

**1 = I have no idea / 5 = I could explain this to someone else**

| Statement | Confidence |
|-----------|-----------|
| I can explain what "cloud computing" means in plain language. | 1 — 2 — 3 — 4 — 5 |
| I can describe the difference between object storage and a database. | 1 — 2 — 3 — 4 — 5 |
| I can name two ways an application can run in the cloud. | 1 — 2 — 3 — 4 — 5 |
| I can explain what authentication and authorization mean. | 1 — 2 — 3 — 4 — 5 |
| I can explain a cloud concept to someone with no technical background. | 1 — 2 — 3 — 4 — 5 |

---

---

# LESSON 2 — WHERE SHOULD OUR INFORMATION GO?

---

## The Challenge

LunchRush is going online. Sam has 50 menu photos to upload. Riley needs to find any order in seconds during the lunch rush. Jordan asks: "Where do we keep all of this?"

---

## Before the Vocabulary: Your First Thoughts

**Answer these questions before your instructor introduces any new terms.**

**Question 1:** LunchRush has 50 photos of menu items (JPG files). Customers need to be able to view them. What would be a good place to keep them?

> *My answer:*
>
> _______________________________________________________________
>
> _______________________________________________________________

**Question 2:** LunchRush records every order: customer name, items ordered, delivery address, time, and total. Sam needs to find all orders placed in the last hour. What would be a good place to keep that information?

> *My answer:*
>
> _______________________________________________________________
>
> _______________________________________________________________

---

## Vocabulary — Lesson 2

*Your instructor will introduce each term. Write the definition in your own words in the space provided.*

**Storage**
Definition (in your own words):
_______________________________________________________________

**Object storage**
Definition (in your own words):
_______________________________________________________________

**Object**
Definition (in your own words):
_______________________________________________________________

**Bucket**
Definition (in your own words):
_______________________________________________________________

**Database**
Definition (in your own words):
_______________________________________________________________

---

## Stretch Vocabulary (Optional)

If you want to go further, ask your instructor about these terms:

- **Structured data** — data organized in a defined format with rows and columns (like a spreadsheet).
- **Unstructured data** — data that doesn't have a predefined format (like a photo or audio file).
- **Query** — a request for specific data from a database (for example, "show me all orders from today").

---

## Activity — Storage Sort

**Instructions:**

1. Review the 12 data items in the card list below.
2. Write each card letter in the correct column of the sort table.
3. For each item you sort, write one sentence explaining why you placed it there.
4. If you're unsure, write your best guess and note your uncertainty — that is a valid answer.

---

**Data Items:**

| Card | Item Description |
|------|--------------------------------------------------------------|
| A | Photo of today's lunch special (JPG) |
| B | Customer's delivery address |
| C | Audio clip of Jordan's welcome message (MP3) |
| D | List of menu item prices |
| E | PDF of LunchRush's food-safety certificate |
| F | A customer's order history (10 past orders) |
| G | Video of Riley explaining the delivery area (MP4) |
| H | Inventory count: how many sandwiches are left |
| I | The LunchRush app's logo (PNG) |
| J | Each driver's total deliveries today |
| K | A scanned copy of LunchRush's business license (PDF) |
| L | Customer feedback ratings (1–5 stars, with a comment) |

---

**Sort Table:**

| Object Storage | Database |
|----------------|----------|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

*(Write card letters in the appropriate column.)*

---

**My Justifications:**

For each card, write one sentence explaining your choice. If your choice was not obvious, say why.

| Card | My reasoning |
|------|--------------|
| A | |
| B | |
| C | |
| D | |
| E | |
| F | |
| G | |
| H | |
| I | |
| J | |
| K | |
| L | |

---

**After sorting:** Look back at your answers from "Before the Vocabulary." Did you change your thinking? Write one sentence about what — if anything — changed.

> _______________________________________________________________
>
> _______________________________________________________________

---

## Explain It Twice — Lesson 2

**Part 1: To Jordan (no jargon)**

Jordan asks: "So where are we keeping the photos, and where are the orders?"

Write 2–3 sentences explaining the storage plan in plain, everyday language. Do not use any technical terms from this lesson.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

**Part 2: To Alex (technical vocabulary)**

Alex wants a one-paragraph technical summary. Use at least three vocabulary terms from this lesson.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

## Jargon Journal — Lesson 2

Complete one entry for **Object storage** and one for **Database**.

---

**Entry 1: Object storage**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________
_______________________________________________________________

---

**Entry 2: Database**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________
_______________________________________________________________

---

---

# LESSON 3 — HOW WILL OUR APPLICATION RUN?

---

## The Challenge

LunchRush now knows where to store its data. Next, Alex needs to explain how the ordering application itself will run. Jordan, Sam, and Riley have never heard of virtual machines, containers, or serverless.

---

## Before the Vocabulary: Your First Thoughts

**Answer these questions before your instructor introduces any new terms.**

> Alex presents three options for running LunchRush's application:
>
> - **Option A:** Rent a whole restaurant kitchen space. You control everything, but you're responsible for all maintenance.
> - **Option B:** Rent a section in a shared food hall. Your section is separated from others; the building manages heating and plumbing.
> - **Option C:** Use a catering company. You tell them what food to make; they handle all equipment and cleanup. You pay per dish.

**Question 1:** Which option gives you the most control over how things are set up?

> *My answer:*
>
> _______________________________________________________________

**Question 2:** Which option requires the least day-to-day management from you?

> *My answer:*
>
> _______________________________________________________________

**Question 3:** Which option makes the most sense if you don't know yet how many customers you'll have?

> *My answer:*
>
> _______________________________________________________________

---

## Vocabulary — Lesson 3

*Write each definition in your own words.*

**Virtual machine (VM)**
Definition (in your own words):
_______________________________________________________________

**Operating system (OS)**
Definition (in your own words):
_______________________________________________________________

**Container**
Definition (in your own words):
_______________________________________________________________

**Container image**
Definition (in your own words):
_______________________________________________________________

**Serverless**
Definition (in your own words):

> ⚠️ Important note to write down:
> "Serverless" does NOT mean there are no servers. It means: _______________________________________________________________
>
> _______________________________________________________________

---

## Stretch Vocabulary (Optional)

- **Orchestration** — automated management of containers across multiple servers.
- **IaaS (Infrastructure as a Service)** — cloud service model where you manage VMs and above; the provider manages the physical hardware.
- **PaaS (Platform as a Service)** — cloud service model where the provider manages the underlying platform; you manage only your application.

---

## Activity — Decision Cards

**Scenario:**

> LunchRush is a small business just getting started online. Alex will manage the technical side but has limited time. Order volume is low during most of the day but spikes at noon. The team wants to minimize ongoing server management.

---

**Option Card 1 — Virtual Machine**

- Control: You manage the operating system and all software.
- Setup time: Moderate — you provision the VM and install your app.
- Scaling: Manual or configured separately.
- Cost model: You pay for the VM while it is running, even when idle.
- Best suited for: Applications needing full OS control or specific configuration.
- One trade-off: Requires OS updates and security patches.

**Option Card 2 — Container**

- Control: You manage the application and its dependencies.
- Setup time: Requires building a container image first.
- Scaling: Faster than VMs; can be automated.
- Cost model: Pay for the compute resources used by your containers.
- Best suited for: Portable, consistent application packaging.
- One trade-off: Requires understanding how to build and manage container images.

**Option Card 3 — Serverless**

- Control: You write the function; the provider handles everything else.
- Setup time: Often the fastest to get started.
- Scaling: Automatic — the provider scales up and down with demand.
- Cost model: Pay per execution and duration; idle time costs nothing.
- Best suited for: Event-driven tasks and intermittent workloads.
- One trade-off: Less control over the runtime; may have execution time limits.

---

**Decision Worksheet:**

**1.** Which option would you recommend for LunchRush's ordering application?

Circle one:   **VM**   /   **Container**   /   **Serverless**

**2.** Write one reason this option fits LunchRush's situation.

> _______________________________________________________________
>
> _______________________________________________________________

**3.** Write one trade-off your recommended option introduces.

> _______________________________________________________________
>
> _______________________________________________________________

**4.** Which option would you NOT recommend for LunchRush right now? Write one reason.

> _______________________________________________________________
>
> _______________________________________________________________

---

**Accuracy reminder:** There is no single correct answer. VMs, containers, and serverless are not three levels you must pass through — they are different approaches, and many real applications use more than one. Your reasoning matters as much as your choice.

---

## Explain It Twice — Lesson 3

**Part 1: To Jordan (no jargon)**

Jordan asks: "So how is our app going to run?"

Write 2–3 sentences using no technical terms.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

**Part 2: To Alex (technical vocabulary)**

Write a one-paragraph technical summary. Use at least three vocabulary terms from this lesson.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

## Jargon Journal — Lesson 3

Complete one entry for each of these three terms: **Virtual machine**, **Container**, **Serverless**.

---

**Entry 1: Virtual machine**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________

---

**Entry 2: Container**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________

---

**Entry 3: Serverless**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________

---

---

# LESSON 6 — WHO CAN CHANGE THE MENU?

---

## The Challenge

A customer's order was charged at the wrong price. Someone changed the price last night — but no one on the team knows who. Jordan realizes LunchRush has never formally decided who is allowed to change what. That needs to change today.

---

## Before the Vocabulary: Your First Thoughts

**Think of a real place that has different levels of access — a hospital, a school, an office, or a hotel.**

**Question 1:** How does that place know who you are?

> _______________________________________________________________

**Question 2:** Once they know who you are, how does the place decide what you're allowed to do or enter?

> _______________________________________________________________

---

## Business Policy for This Activity

Read the policy carefully before you complete the permissions table.

> **LunchRush Access Policy (fictional, for this activity):**
>
> - **Jordan** manages the whole business and must be able to view and change anything.
> - **Sam** manages menu content. Sam can add, edit, and remove menu items and photos, but cannot access financial records or change prices.
> - **Riley** manages deliveries. Riley can view order details and update delivery status, but cannot change menu items or financial data.
> - **Alex** maintains technology systems. Alex can view and change technical configurations. Alex does not need to view customer payment information during normal operations.
>
> **Principle to apply:** Give each person the minimum access needed to do their job.

---

## Vocabulary — Lesson 6

*Write each definition in your own words.*

**Authentication**
Definition (in your own words):
_______________________________________________________________

**Authorization**
Definition (in your own words):
_______________________________________________________________

**What is the key difference between authentication and authorization?**
> Authentication answers the question: ___________________________
>
> Authorization answers the question: ___________________________

**Identity and access management (IAM)**
Definition (in your own words):
_______________________________________________________________

**Least privilege**
Definition (in your own words):
_______________________________________________________________

**Shared responsibility**
Definition (in your own words):

> ⚠️ Important note to write down:
> The cloud provider is NOT responsible for all security. The provider handles: _______________________________________________________________
>
> LunchRush is responsible for: _______________________________________________________________

---

## Stretch Vocabulary (Optional)

- **Multi-factor authentication (MFA)** — requiring two or more types of verification before granting access.
- **Role-based access control (RBAC)** — assigning permissions to roles rather than to individual users, so access is managed by job function.

---

## Activity — Permissions Table

**Instructions:**

Using the LunchRush Access Policy above, fill in each cell of the table with one of three options:

- **R** = Read (can view but not change)
- **W** = Write (can view and change)
- **—** = No access

After completing the table, choose **two cells** where you were unsure. Write one sentence for each explaining your reasoning.

---

**Permissions Table:**

| Resource | Jordan | Sam | Riley | Alex |
|---------------------------------|--------|-----|-------|------|
| Menu item names and descriptions | | | | |
| Menu photos | | | | |
| Menu item prices | | | | |
| Customer order details | | | | |
| Delivery status | | | | |
| Financial records | | | | |
| Technical system configuration | | | | |
| Customer payment information | | | | |

---

**Two cells I was unsure about:**

**Cell 1:** *(resource and character)*
_______________________________________________________________

My reasoning:
_______________________________________________________________
_______________________________________________________________

**Cell 2:** *(resource and character)*
_______________________________________________________________

My reasoning:
_______________________________________________________________
_______________________________________________________________

---

**Reflection:** Looking back at the LunchRush story — the wrong price was changed at 11 p.m. Using your completed permissions table, explain who would have been able to make that change, and what access control prevented or would have prevented others.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

## Explain It Twice — Lesson 6

**Part 1: To Jordan (no jargon)**

Jordan wants to understand the new access plan.

Write 2–3 sentences with no technical terms.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

**Part 2: To Alex (technical vocabulary)**

Write a one-paragraph technical summary. Use at least three vocabulary terms from this lesson.

> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________
>
> _______________________________________________________________

---

## Jargon Journal — Lesson 6

Complete one entry for each of these three terms: **Authentication**, **Authorization**, **Least privilege**.

---

**Entry 1: Authentication**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________

---

**Entry 2: Authorization**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________

---

**Entry 3: Least privilege**

The technical term is:
_______________________________________________________________

In my own words, it means:
_______________________________________________________________
_______________________________________________________________

At LunchRush, we would use it when:
_______________________________________________________________

One limitation of the analogy I heard is:
_______________________________________________________________
_______________________________________________________________

A question I still have is:
_______________________________________________________________

---

---

# AFTER THE LESSONS: CONFIDENCE CHECK

*Come back to these questions after completing all three lessons. Circle one number for each statement.*

**1 = I have no idea / 5 = I could explain this to someone else**

| Statement | Confidence |
|-----------|-----------|
| I can explain what "cloud computing" means in plain language. | 1 — 2 — 3 — 4 — 5 |
| I can describe the difference between object storage and a database. | 1 — 2 — 3 — 4 — 5 |
| I can name two ways an application can run in the cloud. | 1 — 2 — 3 — 4 — 5 |
| I can explain what authentication and authorization mean. | 1 — 2 — 3 — 4 — 5 |
| I can explain a cloud concept to someone with no technical background. | 1 — 2 — 3 — 4 — 5 |

---

## Final Reflection

Answer these questions after completing all three lessons.

**1.** Which cloud concept was hardest for you to understand? What helped?

> _______________________________________________________________
>
> _______________________________________________________________

**2.** Which lesson's activity was most useful for your learning? Why?

> _______________________________________________________________
>
> _______________________________________________________________

**3.** Write one cloud term you feel confident enough to explain to a friend. Write your explanation here.

> _______________________________________________________________
>
> _______________________________________________________________

**4.** Write one question that the curriculum didn't fully answer for you.

> _______________________________________________________________
>
> _______________________________________________________________

**5.** If LunchRush were a real business you were advising, what is one more cloud challenge you think they would face that wasn't covered here?

> _______________________________________________________________
>
> _______________________________________________________________

---

*Thank you for learning with LunchRush.*

---

> **A note on this workbook:** All business names, characters, scenarios, and data are fictional and created for educational purposes. No real business data is used.
