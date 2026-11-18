# Instructor Guide
## Cloud Before Code — LunchRush Curriculum

> **How to use this guide:** Lessons 2, 3, and 6 are fully developed. Each includes an opening story, a step-by-step instructor script, activity support, expected responses, accessibility adaptations, and an answer key for the exit assessment. Lessons 1, 4, 5, 7, and 8 are concise teaching outlines. All technical content is marked [DRAFT] and requires verification against official documentation before classroom use.

---

# PART ONE: CONCISE OUTLINES

---

## Lesson 1 Outline — What Does Our Online Business Need?

**Challenge:** LunchRush wants customers to order online. Jordan, the owner, is not sure what "the cloud" actually means or whether LunchRush needs it.

**Learning objective:** Describe what happens when a customer uses an online application and identify where the cloud fits in.

**Essential vocabulary:** Cloud computing, Client, Server

**Stretch vocabulary:** Compute, Application, Data center

**Teaching sequence:**

1. *Open with the problem.* Ask learners: "Imagine you wanted to order food from a restaurant online. What would need to exist for that to work?" Accept all reasonable answers. Do not introduce vocabulary yet.
2. *Exploratory task.* Learners sketch or list the pieces they think are needed: a device, something that holds the menu, something that takes the order.
3. *Introduce vocabulary.* Define client, server, and cloud computing in plain language. Use the analogy of a customer at a counter (client) and the kitchen (server). Note where the analogy stops: a kitchen does not simultaneously serve thousands of customers across the globe.
4. *Vocabulary note:* "Cloud computing" [DRAFT] refers to delivering computing services — such as storage, processing power, and software — over the internet, on demand, with pay-as-you-go pricing. (Source to verify: NIST SP 800-145.)
5. *Activity.* Learners annotate their sketch, labeling the client, the server, and the network connection between them. They add a note: "Where does the cloud fit in this picture?"
6. *Explain it twice.* To Jordan: "The website your customers see lives on a computer somewhere else, connected to the internet." To Alex: "A client makes requests to a server that hosts our application."
7. *Exit check.* Three questions: (a) What is a client? (b) What is a server? (c) Why might a business use cloud computing instead of buying its own server?

**Common misconception:** "The cloud is just the internet." Clarify that the cloud uses the internet to deliver services, but the cloud specifically refers to on-demand computing resources managed by a provider.

**Jargon journal:** Cloud computing, Server.

**Estimated time:** 15 minutes

---

## Lesson 4 Outline — How Does an Order Travel?

**Challenge:** A customer submits an order and the correct service must receive it. Jordan wants to understand how this happens without thinking about wires and cables.

**Learning objective:** Trace an order request through a simplified network diagram; identify the roles of DNS, HTTP, and APIs.

**Essential vocabulary:** Network, IP address, Domain Name System (DNS), Hypertext Transfer Protocol (HTTP), Application programming interface (API)

**Stretch vocabulary:** REST, Endpoint, Packet

**Teaching sequence:**

1. *Open with the problem.* Ask learners: "If you type 'lunchrush.example' into a browser, how does the browser know where to go?" Accept all answers without correction yet.
2. *Exploratory task.* Learners arrange six blank cards labeled: *Customer types address → Browser asks for directions → Directions returned → Browser contacts the server → Server finds the order service → Response returned.* Ask them to put the cards in what they think is the right order.
3. *Introduce vocabulary.* Introduce each term when it appears in the journey: DNS as a directory that translates names to IP addresses; HTTP as the agreed format for requests and responses; API as the defined way one software service asks another for something.
4. *Accuracy note:* An API is not the same as the network. Not all APIs use HTTP (some use other protocols). Label all diagrams as simplified.
5. *Activity.* Learners re-arrange cards with correct labels and add a one-sentence description of what happens at each step.
6. *Explain it twice.* To Jordan: "It's like looking up a phone number in a directory, dialing, and asking for a specific department." To Alex: "The browser resolves the domain via DNS, sends an HTTP request to the server's IP address, and the server routes it to the correct API endpoint."
7. *Exit check.* Three questions: (a) What does DNS do? (b) What is an API? (c) Name one difference between HTTP and an API.

**Common misconception:** "The API is what connects the internet." Clarify: the API defines how software services communicate with each other; the network carries the data.

**Jargon journal:** API, DNS.

**Estimated time:** 15–20 minutes

---

## Lesson 5 Outline — What Happens During the Lunch Rush?

**Challenge:** At noon, far more customers order at once than the application was originally set up to handle. Orders are slow or fail.

**Learning objective:** Explain what scaling means; describe how load balancing distributes requests; identify at least one limit of adding instances.

**Essential vocabulary:** Scaling, Application instance, Load balancing

**Stretch vocabulary:** Orchestration, Kubernetes, Horizontal vs. vertical scaling

**Teaching sequence:**

1. *Open with the problem.* Ask learners: "If one checkout lane at a grocery store gets too busy, what do stores do?" (They open more lanes.) Ask: "What if the store only had one cash register in the building?" (Opening a lane doesn't help.)
2. *Exploratory task.* Learners receive a scenario: LunchRush normally runs one copy of its ordering application. At noon, 50 customers try to order at the same time. What would they suggest?
3. *Introduce vocabulary.* Introduce *scaling* as increasing or decreasing resources to match demand. Introduce *application instance* as one running copy of the application. Introduce *load balancing* as distributing incoming requests across multiple instances.
4. *Accuracy note:* Adding instances helps when the application itself is the bottleneck. If the database or network is the constraint, more instances will not help. Kubernetes is one tool that can automate instance management, but it is not required for every cloud application. Orchestration and load balancing are related but separate concepts.
5. *Activity.* Learners use cards to represent customers (requests) and application instances (lanes). They model distributing five requests across two instances, then three instances.
6. *Explain it twice.* To Jordan: "We run more copies of the app when it gets busy, and a traffic director sends each customer to a free copy." To Alex: "We scale horizontally by adding instances and use a load balancer to distribute incoming requests."
7. *Exit check.* Three questions: (a) What is scaling? (b) What does a load balancer do? (c) Name one situation where adding more instances would not solve the problem.

**Common misconception:** "Scaling automatically fixes all performance problems." Clarify: scaling addresses compute bottlenecks, but slowness can also come from the database, network, or external services.

**Jargon journal:** Scaling, Load balancing.

**Estimated time:** 15–20 minutes

---

## Lesson 7 Outline — How Do We Release an Update?

**Challenge:** LunchRush wants to add a new "meal of the day" feature. The team is nervous about releasing changes that might break the site for customers.

**Learning objective:** Describe a basic CI/CD pipeline; distinguish continuous delivery from continuous deployment; arrange pipeline stages in order.

**Essential vocabulary:** Deployment, Automation, Pipeline, Continuous integration (CI), Continuous delivery

**Stretch vocabulary:** Continuous deployment, Rollback, Environment

**Teaching sequence:**

1. *Open with the problem.* Ask learners: "If you wanted to add a new page to a website without taking the site down, how would you do it safely?" Accept all answers.
2. *Exploratory task.* Learners receive six unlabeled stage cards: Change code → Build → Test → Approval (or skip) → Deploy → Verify. Ask them to arrange the cards in what they think is a sensible order.
3. *Introduce vocabulary.* Define pipeline as an automated sequence of steps that moves a change from code to running in production. Define CI as automatically building and testing each change. Distinguish continuous delivery (the pipeline stops before production for a human approval) from continuous deployment (the pipeline automatically deploys to production if all tests pass).
4. *Accuracy note:* A pipeline does not guarantee error-free releases. It reduces risk by catching problems earlier. The choice between delivery and deployment depends on the business's risk tolerance.
5. *Activity.* Learners create two pipeline diagrams on paper: one for continuous delivery (with an approval gate), one for continuous deployment (without). They label each stage.
6. *Explain it twice.* To Jordan: "Every time the team saves a change, the system automatically checks it and, when we're ready, sends it live." To Alex: "We use a CI/CD pipeline that builds and tests each commit; delivery requires a manual approval before the final deploy."
7. *Exit check.* Three questions: (a) What is a pipeline? (b) What is the main difference between continuous delivery and continuous deployment? (c) Does a pipeline guarantee no bugs will reach production?

**Common misconception:** "Continuous deployment means the code is always deployed." Clarify: continuous deployment means the deployment step is automated when tests pass — not that code is released without testing.

**Jargon journal:** Pipeline, Continuous integration.

**Estimated time:** 15–20 minutes

---

## Lesson 8 Outline — Why Are Orders Slow?

**Challenge:** Customers are reporting slow or failed orders. Jordan wants to know what is happening, but the team needs to investigate before drawing conclusions.

**Learning objective:** Identify what logs, metrics, and alerts provide; distinguish observations from conclusions; list additional evidence needed.

**Essential vocabulary:** Monitoring, Metric, Log, Alert, Latency

**Stretch vocabulary:** Tracing, Observability, Mean time to resolution (MTTR)

**Teaching sequence:**

1. *Open with the problem.* Ask learners: "If orders are slow, what information would you want before deciding what to fix?" Accept all answers. Do not introduce vocabulary yet.
2. *Exploratory task.* Provide a fictional one-page "dashboard" showing: average order time is 12 seconds (normally 2), one server's CPU is at 90%, and three error entries appear in a log. Ask learners: "What do you know for certain? What is still a question?"
3. *Introduce vocabulary.* Define metric as a measured number recorded over time; log as a text record of events; alert as an automatic notification when a metric crosses a threshold; latency as the time between sending a request and receiving a response; monitoring as the practice of collecting these signals continuously.
4. *Accuracy note:* High CPU on one server does not prove it is the cause of slow orders. It is an observation that needs further investigation. Treat each data point as evidence to consider, not as proof.
5. *Activity.* Learners complete a guided worksheet: (a) List three things you can observe from the dashboard. (b) Write one conclusion you cannot yet confirm. (c) List two more pieces of evidence you would want.
6. *Explain it twice.* To Jordan: "The dashboard shows the app is slower than normal and one part is under heavy load. We need more information before we know the exact cause." To Alex: "Latency metrics are elevated, one instance shows high CPU utilization, and the logs show repeated timeout errors. I'd want to check the database query times and network latency before concluding the compute layer is the bottleneck."
7. *Exit check.* Three questions: (a) What is a metric? (b) What is latency? (c) Why is one high metric not enough to identify a root cause?

**Common misconception:** "If the CPU is high, the server is broken." Clarify: high CPU is a symptom that could have many causes. Investigation requires combining multiple signals.

**Jargon journal:** Metric, Log.

**Estimated time:** 15–20 minutes

---

---

# PART TWO: FULLY DEVELOPED LESSON PACKS

---

## LESSON 2 — WHERE SHOULD OUR INFORMATION GO?

---

### Objectives

By the end of this lesson, learners will be able to:

1. Distinguish between object storage and a database in the context of a small business scenario and explain the simplified distinction.
2. Sort at least five fictional business data items into appropriate storage categories and provide a written justification for each choice.
3. Define *storage*, *object*, *bucket*, and *database* in their own words using the jargon-journal template.
4. Explain the storage decision to a nontechnical business owner using plain language and to a technical teammate using correct vocabulary.

---

### Materials

- Learner workbook, Lesson 2 pages (or printed copies)
- Storage-sorting cards (12 cards; included in the learner workbook)
- Two labeled columns on paper or on the board: **Object Storage** | **Database**
- Optional: a physical file folder and a notebook to illustrate the analogy

No software, accounts, or internet access required.

---

### Timing

| Segment | Time |
|-------------------------------|--------|
| Opening story | 3 min |
| Exploratory task | 3 min |
| Vocabulary introduction | 5 min |
| Main activity (sort + justify) | 7 min |
| Explain it twice | 3 min |
| Exit assessment | 3 min |
| Jargon journal (optional) | +5 min |
| **Total (without journal)** | **24 min** |

---

### Opening Story

*Read or paraphrase to learners:*

> LunchRush has been taking orders over the phone, but Jordan wants customers to order online. Sam needs to upload photos of every menu item. Riley needs to look up every order quickly during the lunch rush. Jordan asks Alex: "Where do we keep all of this?"
>
> Alex says: "Before I answer, let me ask you something. Do you want to quickly look up 'all orders placed between noon and 1 p.m. today'? Or do you just want a safe place to keep the photos so customers can see them?"
>
> Jordan thinks for a moment. "Both, actually. But they feel different somehow."
>
> Alex nods. "They are different. And that difference is exactly what we need to talk about."

---

### Exploratory Task (Before Terminology)

**Say to learners:**

> "Before I introduce any vocabulary, I want you to think about two kinds of information LunchRush deals with. Take two minutes and write your answers."

Distribute or project the two prompts:

1. LunchRush has 50 photos of menu items (JPG files). They need customers to be able to view them. What would be a good place to keep them? Why?
2. LunchRush records every order: customer name, items ordered, delivery address, time, and total. Sam needs to find all orders placed in the last hour. What would be a good place to keep that information? Why?

**Allow 2–3 minutes of individual or pair work. Do not confirm or correct answers yet.**

Say: "Hold onto your answers. We'll come back to them after I introduce a few terms."

---

### Vocabulary Introduction with Accurate Definitions

*Introduce each term in the order below. Use the script or paraphrase.*

---

**Term 1: Storage** [DRAFT — verify against NIST or provider-neutral sources]

> "In cloud computing, *storage* refers to the services that hold data persistently — meaning the data stays saved even when nothing is actively processing it. Think of storage as the place your information lives when it's not being used right now."

---

**Term 2: Object Storage** ✓ Verified — *Introduction to Object Storage*, IBM Cloud Databases documentation, Nov 17 2026

> "Object storage is a way of saving data as individual, self-contained units called *objects*. Each object contains the data itself — like a photo file — plus information about that data, called metadata. Objects are stored in containers called *buckets*."
>
> "Object storage is well-suited for data you need to store and retrieve as a whole unit: a photo, a video, a PDF. It is generally not designed to let you search inside the data or update part of it efficiently."
>
> *IBM Cloud source definition:* "Object storage is a data storage architecture that manages data as objects, as opposed to other storage architectures such as file systems, which manage data as a file hierarchy, or reliable durable file storage (network-attached block storage), which manage data as blocks within sectors and tracks."

**Analogy:** "Think of object storage like a labeled envelope in a filing cabinet. You put the whole thing in, and you take the whole thing out. You don't rewrite paragraphs inside the envelope while it's in the cabinet."

**Analogy limitation:** "Unlike physical envelopes, objects in cloud storage can be accessed by thousands of people simultaneously, often from anywhere in the world. And unlike a filing cabinet, the system can store billions of envelopes."

---

**Term 3: Object** ✓ Verified — *Setting up a cloud object storage bucket*, IBM Cloud documentation, Nov 17 2026

> "An *object* is one piece of data stored in object storage. It includes the actual content (the file) and metadata — information about the file, such as when it was created or its file type."
>
> *IBM Cloud source:* An object is stored in a named bucket within a COS (Cloud Object Storage) service. Objects are addressed by bucket name and object key.

---

**Term 4: Bucket** ✓ Verified — *Setting up a cloud object storage bucket*, IBM Cloud documentation, Nov 17 2026

> "A *bucket* is a named container that holds objects. You can think of it as a top-level folder in object storage, though it works differently from a traditional folder system."

**Analogy limitation:** "Unlike a folder on your laptop, a bucket typically cannot be nested inside another bucket in most object storage systems. The structure is flatter."

*IBM Cloud source confirms:* "A COS bucket must be created and empty. The bucket name must be all lower case, and the bucket cannot be shared with other table configurations."

---

**Term 5: Database** [DRAFT — verify against IBM Cloud Databases overview]

> "A *database* is an organized system for storing, managing, and retrieving structured information. Databases are designed to let you search, filter, sort, and update specific pieces of information efficiently — for example, finding all orders placed by a specific customer in the last 24 hours."

**Accuracy note:** "Object storage and databases have more overlapping capabilities in real production systems than this lesson suggests. Some databases can store files; some object storage systems support querying metadata. For LunchRush's simple starting scenario, we're making a practical choice: photos go to object storage, order records go to a database. We'll note where this simplification has limits."

---

### Worked Example

Say to learners:

> "Let's look at two real items and decide together."

**Item A: A photo of the LunchRush logo (a JPG file, 2 MB)**

Walk through the reasoning:

- Do we need to search *inside* this file? No.
- Do we need to update part of it? No.
- Do we need customers to be able to load it quickly as a whole file? Yes.
- **Decision:** Object storage. We store it as an object in a bucket named `lunchrush-images`.

**Item B: An order record — customer name, items ordered, total, delivery address, timestamp**

Walk through the reasoning:

- Do we need to search by customer name or time? Yes.
- Do we need to retrieve individual fields (just the total, or just the address)? Yes.
- Do we need to update the status (from "received" to "delivered")? Yes.
- **Decision:** Database. The structured, searchable nature of this data suits a database.

---

### Main Activity — Storage Sort

**Instructions (also in learner workbook):**

1. Review the 12 data items on the sorting cards.
2. Place each card in one of two columns: **Object Storage** or **Database**.
3. For each item, write one sentence explaining your choice.
4. If you're unsure, write your best guess and explain your uncertainty.

**Data items on the cards:**

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

### Expected Responses

| Card | Expected placement | Reasoning |
|------|-------------------|-----------|
| A | Object storage | A photo file is retrieved as a whole unit; no need to search inside it. |
| B | Database | An address is a structured field that may need to be queried or updated. |
| C | Object storage | An audio file is retrieved whole. |
| D | Database | Prices are structured data that need to be updated and queried by name. |
| E | Object storage | A PDF certificate is typically stored and retrieved as a whole document. |
| F | Database | Order history is queried, filtered by date or item, and updated. |
| G | Object storage | A video file is retrieved as a whole unit. |
| H | Database | Inventory counts change frequently and need to be queried and updated. |
| I | Object storage | A logo image is retrieved whole. |
| J | Database | Driver totals are numeric data queried and updated throughout the day. |
| K | Object storage | A scanned document is typically stored and retrieved as a whole file. |
| L | Database | Ratings and comments need to be searched, averaged, and analyzed. |

**Note on Card L:** Some learners may argue that the comment text could be stored as an object (a text file). This is a defensible answer. Accept it with a discussion of trade-offs: a database makes it easier to search comments by rating or date.

**Note on Card E and K:** In practice, PDFs are sometimes stored in both systems — the file in object storage, with metadata (document name, date, type) in a database. Accept this nuanced answer as a stretch response.

---

### "Explain It Twice" Task

Provide the following prompts (also in learner workbook):

**Prompt 1 — To Jordan (no jargon):**
> "Jordan asks: 'So where are we keeping the photos, and where are the orders?' Write 2–3 sentences explaining the storage plan in everyday language."

**Example acceptable response:** "We're keeping the photos in a kind of digital filing cabinet — you just drop them in and customers can view them. The order information goes somewhere that lets us search it, sort it, and update it quickly, like a really organized spreadsheet system."

**Prompt 2 — To Alex (technical vocabulary):**
> "Alex wants a one-paragraph technical summary. Use at least three vocabulary terms from this lesson."

**Example acceptable response:** "For media assets like menu photos, we'll use object storage — each photo is stored as an object in a bucket named `lunchrush-images`. For order and customer data, we'll use a relational database, which lets us query structured fields like customer name, timestamp, and delivery status efficiently."

---

### Three-Question Exit Assessment

*Read aloud or distribute.*

1. What is object storage best suited for? Give one example from LunchRush.
2. What makes a database a better choice than object storage for order records?
3. True or false: Object storage and databases can never be used together. Explain your answer.

**Answer key (instructor copy only — do not share with learners):**

1. Object storage is best suited for files that are stored and retrieved as whole units, such as photos, audio, or video. Example: LunchRush's menu photos (JPGs) stored in a bucket.
2. A database allows structured data to be searched, filtered, sorted, and updated. Order records contain structured fields (customer name, items, timestamp) that need to be queried — for example, finding all orders from the last hour. Object storage does not efficiently support this kind of query.
3. False. Object storage and databases are complementary. Many applications use both: media files in object storage, structured data in a database. The lesson simplifies the distinction to introduce the core concepts.

---

### Common Misconceptions and Corrective Feedback

| Misconception | Corrective response |
|---------------|---------------------|
| "Object storage is just like a folder on my computer." | Object storage is similar to a folder in that it holds files, but it is a flat structure (no nested buckets in most systems), is designed for internet-scale access, and is accessed via a URL or API rather than a file path. |
| "A database can do everything object storage can do, so why use both?" | Databases are optimized for structured, searchable data with relationships. Storing large binary files (photos, videos) in a database is technically possible but is generally inefficient and expensive at scale. Object storage is designed specifically for that use case. |
| "Once I put something in object storage, I can't change it." | You can delete and replace objects, and you can update an object's metadata. What you generally can't do is edit part of a file in place, the way you would update a row in a database. |

---

### Accessibility Adaptations

- All sorting cards can be used without color by relying on the card letter and text label.
- The two-column sort can be completed by writing card letters in two lists on paper rather than physically moving cards.
- For learners using screen readers, provide the sorting card list as a table in a plain-text document.
- The "explain it twice" task can be completed verbally if written output is a barrier; a partner or instructor can record the response.

---

### Jargon Journal — Lesson 2

Learners complete one entry for **Object storage** and one for **Database**. The template is in the learner workbook.

**Model entry for instructor reference (do not share with learners before they attempt it):**

*Object storage:*
- The technical term is: Object storage
- In my own words, it means: A way to save files in the cloud so they can be loaded later as a complete file, like a digital storage locker.
- At LunchRush, we would use it when: We need to store menu photos so customers can view them.
- One limitation of the analogy is: A storage locker holds one person's things; object storage can serve millions of users simultaneously.
- A question I still have is: Can object storage be used for backup copies of database data?

---

---

## LESSON 3 — HOW WILL OUR APPLICATION RUN?

---

### Objectives

By the end of this lesson, learners will be able to:

1. Describe the purpose of a virtual machine, a container, and serverless compute in beginner-friendly terms.
2. Use decision cards to compare at least three deployment options for a given scenario and state one trade-off for each.
3. Explain that *serverless* means the learner does not manage servers directly — not that no servers exist.
4. Explain the compute decision using both plain and technical language.

---

### Materials

- Learner workbook, Lesson 3 pages (or printed copies)
- Decision cards (3 option cards + 1 scenario card; included in the learner workbook)
- Optional: a whiteboard or flip chart to draw the analogy illustrations

No software, accounts, or internet access required.

---

### Timing

| Segment | Time |
|-------------------------------|--------|
| Opening story | 3 min |
| Exploratory task | 3 min |
| Vocabulary introduction | 7 min |
| Worked example | 2 min |
| Main activity (decision cards) | 7 min |
| Explain it twice | 3 min |
| Exit assessment | 3 min |
| Jargon journal (optional) | +5 min |
| **Total (without journal)** | **28 min** |

*Note: This lesson runs slightly over 25 minutes if the jargon journal is included. Consider splitting the jargon journal as homework or a follow-up activity.*

---

### Opening Story

*Read or paraphrase:*

> Alex tells the team: "Now that we know where the data lives, we need to decide where the application itself runs. The app is what customers see — the menu, the cart, the checkout."
>
> Riley asks: "Isn't it just on a computer somewhere?"
>
> Alex: "Technically, yes. But *which kind of computer arrangement* matters a lot for how much we pay, how much we manage, and how well it handles busy periods."
>
> Sam: "What are our choices?"
>
> Alex takes out three index cards and sets them on the table.

---

### Exploratory Task (Before Terminology)

**Say to learners:**

> "Imagine you are opening a small restaurant. You have three options for your kitchen:"
>
> 1. **Rent a whole restaurant space** — you get to control everything, but you're responsible for all maintenance.
> 2. **Rent a kitchen section in a shared food hall** — your section is separated from others, and the building manages heating and plumbing.
> 3. **Use a catering company** — you tell them what food to make; they handle all the equipment. You pay per dish.
>
> "Before I introduce any cloud vocabulary, write your answers to these questions:"
> - Which option gives you the most control?
> - Which option requires the least day-to-day management from you?
> - Which option makes the most sense if you don't know yet how many customers you'll have?

**Allow 2–3 minutes. Hold answers for comparison after vocabulary.**

---

### Vocabulary Introduction with Accurate Definitions

---

**Term 1: Virtual Machine (VM)** [DRAFT — verify against NIST or CNCF glossary]

> "A *virtual machine* is a software-based simulation of a physical computer. It runs an operating system and applications just like a physical machine, but it shares the underlying hardware with other virtual machines."
>
> "You manage the operating system, the software installed on it, and how it's configured — just as you would with a physical computer you own."

**Analogy:** "Think of a VM like renting an apartment in a large building. You have your own private space, your own locks, and you decide how to arrange your furniture. The landlord owns the building and handles the structural maintenance, but everything inside your unit is yours to manage."

**Analogy limitation:** "Unlike an apartment, a VM can be created, copied, or deleted in seconds. You can run dozens of VMs on a single physical server. The 'landlord' (cloud provider) manages the hardware but has no access to what's running inside your VM."

---

**Term 2: Operating System (OS)** [DRAFT]

> "An *operating system* is the software that manages a computer's hardware and provides services for other programs to run. When you use a VM, you choose which operating system to install and are responsible for keeping it updated and secure."

---

**Term 3: Container** ✓ Verified — *Understanding IBM Cloud Kubernetes Service — What are containers?*, IBM Cloud Kubernetes Service documentation, Nov 17 2026

> "A *container* packages an application and everything it needs to run — its code, settings, and dependencies — into a single portable unit. Containers share the host computer's operating system but are isolated from each other."
>
> "Because a container includes its own dependencies, it runs the same way whether it's on a developer's laptop or a cloud server."
>
> *IBM Cloud source definition:* "A container is an app that is packaged with all its dependencies so that the app can be moved between environments and run without changes. Unlike virtual machines, containers don't virtualize a device, its operating system, and the underlying hardware. Only the app code, run time, system tools, libraries, and settings are packaged inside the container. Containers run as isolated processes on compute hosts and share the host operating system and its hardware resources. This approach makes a container more lightweight, portable, and efficient than a virtual machine."

**Analogy:** "A container is like a shipping container on a cargo ship. Each container holds one specific shipment, fully packed. The ship (the host computer) carries many containers at once without knowing what's inside each one. The containers are standardized so they fit on any ship."

**Analogy limitation:** "Shipping containers are physically separate; software containers share the host operating system kernel. This sharing makes containers more efficient but also means they provide less isolation than virtual machines. It is not accurate to say containers are as isolated as VMs."

---

**Term 4: Container Image** ✓ Verified — *Understanding IBM Cloud Kubernetes Service — What are containers?*, IBM Cloud Kubernetes Service documentation, Nov 17 2026

> "A *container image* is the blueprint or template used to create a container. It is a read-only snapshot of everything the application needs. When you run an image, you get a running container."
>
> *IBM Cloud source definition:* "A container image is a package that includes the files, configuration settings, and libraries to run a container. An image is built from a text file called a Dockerfile. Dockerfiles define how to build the image and which artifacts to include in it."

---

**Term 5: Serverless** ✓ Verified — *Migrating IBM Cloud Functions to Code Engine*, IBM Cloud Code Engine documentation, Nov 17 2026

> "With *serverless compute*, you provide the code for a function or task. The cloud provider handles all the infrastructure: allocating resources, running the code when needed, and scaling automatically. You pay only for the time your code is actually running."
>
> **Important accuracy note:** Serverless does not mean there are no servers. Servers still exist and run your code. 'Serverless' means you do not provision, configure, or manage those servers yourself. The name describes your experience as the user, not the underlying reality.
>
> *IBM Cloud source:* "IBM Cloud® Code Engine is a fully managed, serverless platform that runs your containerized workloads… Functions-as-a-Service in Code Engine offers on-demand code execution with low cold start latency and rapid scale-out."

**Analogy:** "Serverless is like using a vending machine. You choose what you want, pay, and the machine handles everything — restocking, temperature control, the payment mechanism. You don't see any of that. You just get the result."

**Analogy limitation:** "A vending machine always has the same items. With serverless, you define your own 'items' (functions). Also, vending machines don't scale — if many people arrive at once, they wait. Serverless platforms can run many copies of your function simultaneously."

---

**Key accuracy points to state explicitly:**

1. Virtual machines, containers, and serverless are **not three mutually exclusive infrastructure layers**. Many applications use combinations. For example, a container might run inside a VM, or serverless functions might call a containerized service.
2. **No single option is always best.** The right choice depends on control requirements, team expertise, expected traffic patterns, budget, and the specific workload.
3. **Serverless is not free.** You pay per use, which can be very cost-effective for intermittent workloads and expensive for constant high-volume workloads.

---

### Worked Example

Say to learners:

> "Let's apply the analogy. Remember the kitchen options from the beginning? Here's how they map to cloud vocabulary:"

| Kitchen option | Cloud equivalent | Why |
|-------------------------------|-----------------|-----|
| Rent a whole restaurant space | Virtual Machine | You manage the OS and everything on it; full control, full responsibility. |
| Rent a kitchen section | Container | You bring your own packaged application; the host manages shared infrastructure. |
| Use a catering company | Serverless | You define the task (function); the provider handles all execution infrastructure. |

> "These are helpful analogies — but remember, they don't map perfectly. We're using them to build intuition, not to define the technology."

---

### Main Activity — Decision Cards

**Instructions (also in learner workbook):**

Each decision card describes LunchRush's ordering application from a different angle. Read each scenario and decide which compute option is the best starting point for LunchRush. You may choose the same option for more than one scenario.

**Scenario Card:**

> LunchRush is a small business just getting started online. Alex will manage the technical side but has limited time. Order volume is low during most of the day but spikes at noon. The team wants to minimize ongoing server management.

**Option Card 1 — Virtual Machine:**

- Control: You manage the operating system and all software.
- Setup time: Moderate — you provision the VM and install your app.
- Scaling: Manual or configured separately.
- Cost model: You pay for the VM while it is running, even when idle.
- Best suited for: Applications needing full OS control, legacy software, or specific configuration requirements.
- One trade-off: Requires OS updates and security patches.

**Option Card 2 — Container:**

- Control: You manage the application and its dependencies; the provider manages the host OS.
- Setup time: Requires building a container image first.
- Scaling: Faster than VMs; can be automated with an orchestration tool.
- Cost model: Pay for the compute resources used by your containers.
- Best suited for: Portable, consistent application packaging; teams already using container tools.
- One trade-off: Requires understanding how to build and manage container images.

**Option Card 3 — Serverless:**

- Control: You write the function; the provider handles everything else.
- Setup time: Often the fastest to get started.
- Scaling: Automatic — the provider scales up and down with demand.
- Cost model: Pay per execution and duration; idle time costs nothing.
- Best suited for: Event-driven tasks, intermittent workloads, and teams that want minimal infrastructure management.
- One trade-off: Less control over the runtime environment; may have execution time limits.

**Decision worksheet questions (in learner workbook):**

1. Which option would you recommend for LunchRush's ordering application? Circle: VM / Container / Serverless
2. Write one reason this option fits LunchRush's situation.
3. Write one trade-off your recommended option introduces.
4. Which option would you NOT recommend for LunchRush right now? Write one reason.

---

### Expected Responses

**Most supportable answer:** Serverless or Container — both are reasonable for a small business with intermittent traffic and limited management capacity.

**VM answer:** Acceptable if the learner notes a specific reason LunchRush would need full OS control. Unlikely for a first-time setup but not wrong.

**Key:** Accept any well-reasoned answer that cites the scenario and states a trade-off. Mark down only if no trade-off is mentioned or if the learner claims one option is "always best."

---

### "Explain It Twice" Task

**Prompt 1 — To Jordan (no jargon):**

> "Jordan asks: 'So how is our app going to run?' Write 2–3 sentences using no technical terms."

**Example acceptable response:** "The app runs on computers that are managed by a cloud company. We just upload our code and tell it what to do — we don't have to worry about maintaining the computers themselves. When it gets busy at noon, the system automatically handles the extra load."

**Prompt 2 — To Alex (technical vocabulary):**

> "Write a one-paragraph technical summary. Use at least three vocabulary terms from this lesson."

**Example acceptable response:** "For LunchRush's ordering application, I recommend starting with serverless compute. Because our order volume is intermittent and spikes at noon, the auto-scaling behavior of serverless reduces infrastructure management. We won't need to manage a virtual machine's operating system or build container images to get started. If we later need more control over the runtime environment, we can migrate to containers."

---

### Three-Question Exit Assessment

1. What is the difference between a virtual machine and a container? Use one sentence for each.
2. True or false: "Serverless" means the application runs without any servers. Explain your answer.
3. Name one situation where a virtual machine might be a better choice than serverless.

**Answer key (instructor copy only):**

1. A virtual machine simulates a full computer, including its own operating system, and you are responsible for managing that OS. A container packages an application and its dependencies but shares the host operating system, making it more lightweight.
2. False. Servers still exist and run the code. "Serverless" means you don't provision or manage those servers yourself — the cloud provider handles that. The term describes the user's experience, not the absence of physical hardware.
3. A VM is a better choice when the application requires a specific operating system version, needs custom kernel settings, runs legacy software that can't be containerized, or when the team needs full control over the runtime environment.

---

### Common Misconceptions and Corrective Feedback

| Misconception | Corrective response |
|---------------|---------------------|
| "Serverless has no servers." | Servers exist. The term means you don't manage them. The cloud provider provisions, scales, and maintains the servers; your responsibility ends at the function code. |
| "Containers are more secure than VMs because they're smaller." | Containers share the host OS kernel, which can mean a vulnerability in one container may affect others. VMs have stronger isolation because each has its own OS. Neither is universally "more secure" — security depends on configuration and context. |
| "One of these options is always the best." | There is no universally best choice. The right option depends on the specific application, team skills, expected traffic, budget, and control requirements. |
| "VMs, containers, and serverless are three separate levels you go through." | They are three different approaches to running code in the cloud. Many applications use more than one. For example, a serverless function might call an API running in a container, which runs on a VM. |

---

### Accessibility Adaptations

- Decision cards can be used without color. All distinctions are conveyed through text.
- Learners who prefer not to write can respond verbally to the "explain it twice" prompts.
- The worked example table can be reproduced as a simple list for screen reader compatibility.
- The analogy illustrations (VM = apartment, container = shipping container, serverless = vending machine) can be described verbally rather than drawn.

---

### Jargon Journal — Lesson 3

Learners complete entries for **Virtual machine**, **Container**, and **Serverless**. Template in the learner workbook.

**Model entry for instructor reference (do not share with learners before they attempt it):**

*Serverless:*
- The technical term is: Serverless
- In my own words, it means: A way to run code in the cloud where the provider handles all the server management. You write the function; they handle everything else.
- At LunchRush, we would use it when: We want the ordering app to handle the noon rush without us manually adding more servers.
- One limitation of the analogy is: The vending machine analogy doesn't capture that serverless has cold-start delays — the first request after a period of inactivity may take longer than expected.
- A question I still have is: How much does serverless actually cost compared to running a VM all day?

---

---

## LESSON 6 — WHO CAN CHANGE THE MENU?

---

### Objectives

By the end of this lesson, learners will be able to:

1. Distinguish authentication (verifying identity) from authorization (deciding what is permitted).
2. Create a permissions table that assigns appropriate access levels to four business characters based on a stated business policy.
3. Define *authentication*, *authorization*, *IAM*, *least privilege*, and *shared responsibility* using the jargon-journal template.
4. Explain the access-control decision using both plain and technical language.

---

### Materials

- Learner workbook, Lesson 6 pages (or printed copies)
- Permissions table template (in learner workbook)
- Role cards for Jordan, Sam, Riley, and Alex (in learner workbook)
- Access level key card: Read / Write / No access (in learner workbook)

No software, accounts, or internet access required.

---

### Timing

| Segment | Time |
|-------------------------------|--------|
| Opening story | 3 min |
| Exploratory task | 3 min |
| Vocabulary introduction | 6 min |
| Worked example | 2 min |
| Main activity (permissions table) | 6 min |
| Explain it twice | 3 min |
| Exit assessment | 3 min |
| Jargon journal (optional) | +5 min |
| **Total (without journal)** | **26 min** |

---

### Opening Story

*Read or paraphrase:*

> One morning, Jordan gets a message from a customer: "Hey — your menu says the soup special is $5, but the checkout charged me $8."
>
> Jordan checks the menu system and sees that the price was changed last night. Jordan asks the team: "Who changed this?"
>
> Sam says: "Not me. I only updated the description."
> Riley says: "I don't even know how to edit the menu."
> Alex looks at the logs and finds that someone with access to the pricing system changed it at 11 p.m.
>
> Jordan: "Wait — does everyone have access to everything?"
>
> Alex: "That's what we need to fix today."

---

### Exploratory Task (Before Terminology)

**Say to learners:**

> "Before I introduce any vocabulary, think about a real-world place that has different levels of access. For example: a hospital, a school, a hotel, or an office building."
>
> "Write your answers to these two questions:"
> 1. How does that place know who you are? (For example: a keycard, a badge, a password.)
> 2. Once they know who you are, how does the place decide what you're allowed to do or enter?

**Allow 2 minutes. The goal is to surface the intuitive difference between proving identity and being granted permission.**

Say: "You've just described two different ideas. Let's give them names."

---

### Business Policy for This Activity

**State this policy clearly before the activity begins. Post it visibly or include it on the worksheet.**

> **LunchRush Access Policy (fictional, for this activity):**
>
> - Jordan manages the whole business and must be able to view and change anything.
> - Sam manages menu content. Sam can add, edit, and remove menu items and photos, but cannot access financial records or change prices.
> - Riley manages deliveries. Riley can view order details and update delivery status, but cannot change menu items or financial data.
> - Alex maintains the technology systems. Alex can view and change technical configurations. Alex does not need to view customer payment information during normal operations.
>
> **Apply the principle of least privilege:** Give each person the minimum access needed to do their job.

---

### Vocabulary Introduction with Accurate Definitions

---

**Term 1: Authentication** ✓ Verified — *Enabling MFA in your account*, IBM Cloud IAM documentation, Nov 17 2026

> "*Authentication* is the process of verifying that someone is who they claim to be. The system checks credentials — something you know (a password), something you have (a phone with an authentication app), or something you are (a fingerprint)."
>
> *IBM Cloud source:* "Verify your identity by using two different verification methods. Methods for verification include email, text, or phone call." — IBM Cloud MFA documentation confirms authentication = identity verification through credentials.

**Analogy:** "Authentication is like showing your ID at the front door. The guard checks whether you are who you say you are."

**Analogy limitation:** "An ID card can be borrowed or forged. Digital authentication systems use additional signals — like a one-time code sent to your phone — to make impersonation harder. This is called multi-factor authentication (MFA), a stretch term for this lesson."

---

**Term 2: Authorization** ✓ Verified — *Platform and service access roles for permissions*, IBM Cloud IAM documentation, Nov 17 2026

> "*Authorization* is the process of deciding what an authenticated user is permitted to do. After the system confirms who you are, it checks what you are allowed to access or change."
>
> *IBM Cloud source:* "Roles… define exactly what actions that a user can complete." IAM policies specify a subject (user), a target (resource), and a role (what actions are allowed). Authorization is enforced through these policies after identity is confirmed.

**Analogy:** "If authentication is showing your ID at the door, authorization is the list of rooms your keycard opens. Your identity might be confirmed, but that doesn't mean you can enter every room."

**Analogy limitation:** "In a real building, the list of rooms is fixed to a physical keycard. In cloud systems, permissions are defined in policies that can be updated instantly and applied to many users at once."

---

**Term 3: Identity and Access Management (IAM)** ✓ Verified — *Getting started with IBM Cloud IAM*, IBM Cloud IAM documentation, Nov 17 2026

> "*Identity and access management*, or IAM, is the set of tools and policies used to manage who can access what in a system. IAM lets you define users, roles, and permissions, and enforce those definitions consistently across a system."
>
> *IBM Cloud source:* "IBM Cloud® Identity and Access Management (IAM) provides centralized, standards-based identity and access management with fine-grained access control to implement least-privilege access across your enterprise workloads and reduce your attack surface."

**Note:** IAM is a category of tools, not a single product. Major cloud providers all offer IAM services, but IAM concepts also apply to non-cloud systems.

---

**Term 4: Least Privilege** ✓ Verified — *Implementing least privileged access with fine-grained access control*, IBM Cloud IAM documentation, Nov 17 2026

> "The *principle of least privilege* means giving a user, system, or application only the access it needs to do its job — nothing more. This limits the damage that can occur if an account is misused or compromised."
>
> *IBM Cloud source:* "The principle of least privilege states that users should be granted only the minimum level of access necessary to complete their tasks." Benefits include: "Limiting user permissions reduces the potential damage from compromised credentials, insider threats, or accidental misuse."

**Analogy:** "A delivery driver gets a key that opens the loading dock, not the executive offices. They need the loading dock to do their job. The executive office key would be extra access they don't need."

**Analogy limitation:** "In cloud systems, 'least privilege' is a policy that must be deliberately designed and regularly reviewed. It doesn't happen automatically."

---

**Term 5: Shared Responsibility** ✓ Verified — *Shared responsibilities for Cloud Databases*, IBM Cloud Databases documentation, Nov 17 2026

> "In cloud computing, *shared responsibility* means that security obligations are divided between the cloud provider and the customer. The provider is typically responsible for securing the physical infrastructure, networking, and the platform itself. The customer is responsible for securing the data, applications, identities, and access controls they build on top of that platform."
>
> **Important accuracy note:** The cloud provider does not handle all security. Customer responsibilities vary depending on the type of service. With more managed services (such as serverless), the provider manages more. With IaaS (infrastructure as a service), the customer manages more. For this activity, LunchRush is responsible for designing and enforcing its own access policies.
>
> *IBM Cloud source:* "Cloud Databases is responsible for ensuring the security of data on disk and data in motion within our infrastructure. The Client is responsible for managing IBM Cloud passwords and database passwords, and keeping passwords secure. The Client is also responsible for configuring appropriate network security or isolation."

---

### Worked Example

Say to learners:

> "Let's fill in one row together using the business policy."

**Character: Riley**

| Resource | Riley's access |
|-------------------------------|---------------|
| Menu items (names, descriptions) | Read |
| Menu photos | Read |
| Order details (what was ordered) | Read |
| Delivery status (update) | Write |
| Menu prices | No access |
| Financial records | No access |
| Technical configuration | No access |

> "Riley needs order details and delivery status to do the job. She doesn't need to change menu items or see financial data. That's least privilege in action."

---

### Main Activity — Permissions Table

**Instructions (also in learner workbook):**

Using the business policy above, complete the permissions table for all four characters. For each cell, write one of three options:
- **R** = Read (can view but not change)
- **W** = Write (can view and change)
- **—** = No access

After completing the table, choose **two cells** where the access level was not obvious. Write one sentence for each explaining your reasoning.

**Resources to assign access for:**

| Resource | Jordan | Sam | Riley | Alex |
|---------------------------------|--------|-----|-------|------|
| Menu item names and descriptions| | | | |
| Menu photos | | | | |
| Menu item prices | | | | |
| Customer order details | | | | |
| Delivery status | | | | |
| Financial records | | | | |
| Technical system configuration | | | | |
| Customer payment information | | | | |

---

### Expected Responses

| Resource | Jordan | Sam | Riley | Alex |
|----------------------------------|--------|-----|-------|------|
| Menu item names and descriptions | W | W | R | R |
| Menu photos | W | W | R | R |
| Menu item prices | W | — | — | — |
| Customer order details | W | R | R | — |
| Delivery status | W | — | W | — |
| Financial records | W | — | — | — |
| Technical system configuration | R | — | — | W |
| Customer payment information | W | — | — | — |

**Notes:**
- Alex's access to customer payment information is **—** (no access) during normal operations, per the stated policy. Accept **R** if the learner provides a justification (e.g., Alex needs it for debugging with appropriate logging).
- Sam's access to customer order details may be **R** if justified (e.g., Sam needs to know which items are ordered most frequently for menu planning). Accept **R** with justification.
- Accept any answer that is internally consistent with the business policy and accompanied by a written reason. Do not mark down justified alternatives.

---

### "Explain It Twice" Task

**Prompt 1 — To Jordan (no jargon):**

> "Jordan wants to understand the new access plan. Write 2–3 sentences with no technical terms."

**Example acceptable response:** "Everyone on the team now has access only to the parts of the system they actually need to do their job. Sam can update the menu, Riley can update deliveries, and Alex can manage the technical setup — but no one has access to things outside their role unless it's necessary. This way, if anything goes wrong, the problem can be contained."

**Prompt 2 — To Alex (technical vocabulary):**

> "Write a one-paragraph technical summary. Use at least three vocabulary terms from this lesson."

**Example acceptable response:** "We've implemented an IAM policy based on the principle of least privilege. Authentication confirms each user's identity through their credentials. Authorization then determines their permitted actions based on their assigned role. Sam is authorized to write menu content but has no access to pricing or financial data. Riley is authorized to read order details and write delivery status updates. Alex is authorized to manage technical configuration but is not authorized to access customer payment information during normal operations. Under our shared responsibility model, the cloud provider secures the infrastructure; we are responsible for these access policies."

---

### Three-Question Exit Assessment

1. What is the difference between authentication and authorization? Use a real-world example for each.
2. What does the principle of least privilege mean? Give one example from LunchRush.
3. True or false: The cloud provider is responsible for making sure Sam can't change menu prices. Explain your answer.

**Answer key (instructor copy only):**

1. Authentication is verifying who someone is — for example, logging in with a password. Authorization is deciding what they're allowed to do — for example, only Jordan can change menu prices. Authentication happens first; authorization uses the confirmed identity to check permissions.
2. Least privilege means giving users only the access they need to do their job. Example: Riley can update delivery status but cannot change the menu or view financial records, because those are not part of Riley's role.
3. False. Under the shared responsibility model, the cloud provider secures the underlying platform. LunchRush is responsible for designing and enforcing its own access policies — including rules about who can change menu prices. This is the customer's responsibility, not the provider's.

---

### Common Misconceptions and Corrective Feedback

| Misconception | Corrective response |
|---------------|---------------------|
| "Authentication and authorization are the same thing." | They are related but distinct. Authentication answers "Who are you?" Authorization answers "What are you allowed to do?" You can be authenticated and still be denied access to specific resources. |
| "The cloud provider handles all security for us." | The cloud provider handles security *of* the infrastructure (physical hardware, network, platform). The customer handles security *in* the cloud: data, identities, access policies, and application code. The boundary depends on the service type. |
| "If you give someone less access, it's less convenient, so it's not worth it." | Least privilege is a security principle that limits the impact of mistakes, compromised accounts, or insider threats. The convenience trade-off is real but deliberate. |
| "IAM is a product you buy." | IAM is a category of functionality. Cloud providers include IAM tools in their platforms. Organizations also use third-party identity providers (such as LDAP or SAML-based systems) independently of cloud. |

---

### Accessibility Adaptations

- The permissions table can be completed using letters (R, W, —) rather than symbols, making it compatible with any text editor.
- Role cards and policy text should be available in a font size of at least 12pt.
- The table can be presented as a plain-text list (e.g., "Jordan — menu prices: Write") for learners who cannot use a grid format.
- The "explain it twice" task can be completed verbally if written output is a barrier.
- Color is not used to convey permission levels; letters are sufficient.

---

### Jargon Journal — Lesson 6

Learners complete entries for **Authentication**, **Authorization**, and **Least privilege**. Template in the learner workbook.

**Model entry for instructor reference (do not share with learners before they attempt it):**

*Least privilege:*
- The technical term is: Least privilege
- In my own words, it means: Only giving someone access to what they actually need — not everything "just in case."
- At LunchRush, we would use it when: Deciding that Sam can edit the menu but not see financial records, because Sam doesn't need financial access to do the job.
- One limitation of the analogy is: The delivery driver/key analogy assumes access is binary (you have the key or you don't). In cloud IAM, permissions can be much more granular — read-only, write, delete, or time-limited.
- A question I still have is: How often should a business review and update permissions?

---

*[DRAFT — All technical definitions in this guide require verification against official documentation (e.g., NIST SP 800-145, NIST SP 800-162, CNCF Glossary, CSA Security Guidance) before classroom use.]*
