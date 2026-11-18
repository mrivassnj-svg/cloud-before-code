from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///./lunchrush.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ── Models ────────────────────────────────────────────────────────────────────

class Lesson(Base):
    __tablename__ = "lessons"
    id            = Column(Integer, primary_key=True, index=True)
    number        = Column(Integer, unique=True)
    title         = Column(String, nullable=False)
    challenge     = Column(Text, nullable=False)
    story         = Column(Text, nullable=False)
    exploratory   = Column(Text, nullable=False, default="")   # pre-vocab task
    activity      = Column(Text, nullable=False, default="")   # main activity
    explain_plain = Column(Text, nullable=False, default="")   # explain-it-twice prompt (plain)
    explain_tech  = Column(Text, nullable=False, default="")   # explain-it-twice prompt (tech)
    exit_q1       = Column(Text, nullable=False, default="")
    exit_q2       = Column(Text, nullable=False, default="")
    exit_q3       = Column(Text, nullable=False, default="")
    full          = Column(Integer, default=1)
    terms         = relationship("Term", back_populates="lesson", order_by="Term.id")


class Term(Base):
    __tablename__ = "terms"
    id            = Column(Integer, primary_key=True, index=True)
    lesson_id     = Column(Integer, ForeignKey("lessons.id"))
    word          = Column(String, nullable=False)
    definition    = Column(Text, nullable=False)
    plain         = Column(Text, nullable=False)
    lunchrush     = Column(Text, nullable=False)
    analogy_limit = Column(Text, nullable=False)
    essential     = Column(Integer, default=1)
    lesson        = relationship("Lesson", back_populates="terms")


# ── Seed data ─────────────────────────────────────────────────────────────────

LESSONS = [
    # ── LESSON 1 ──────────────────────────────────────────────────────────────
    {
        "number": 1,
        "title": "What Does Our Online Business Need?",
        "challenge": "LunchRush wants customers to order online, but Jordan isn't sure what 'the cloud' actually means.",
        "story": "Jordan gathers the team around the counter. 'We need a website so people can order from us. But I keep hearing about the cloud — what does that even mean? Is it just the internet?' Alex smiles. 'Not exactly. Let me show you what actually happens when someone opens a website.'",
        "exploratory": "Before learning any vocabulary, think about what needs to exist for you to order food online. Sketch or list the pieces: What device do you use? Where does the menu live? What takes your order? What connects them?",
        "activity": "Draw a simple diagram with three boxes: Customer Device, App, and Information Store. Draw arrows showing what travels between them when a customer places an order. Label each arrow with what is being sent — for example: 'menu request', 'order details', 'confirmation'.",
        "explain_plain": "Jordan asks: 'So what exactly is the cloud?' Explain in 2–3 sentences using no technical terms.",
        "explain_tech": "Alex wants a one-paragraph technical summary. Use the terms: cloud computing, client, and server.",
        "exit_q1": "What is the difference between a client and a server?",
        "exit_q2": "Why might a small business use cloud computing instead of buying its own server?",
        "exit_q3": "True or false: The cloud is the same thing as the internet. Explain your answer.",
        "full": 1,
        "terms": [
            {
                "word": "Cloud computing",
                "definition": "Delivering computing services — storage, processing, and software — over the internet, on demand, typically with pay-as-you-go pricing.",
                "plain": "Renting computer power and storage over the internet instead of buying and maintaining your own machines.",
                "lunchrush": "Instead of buying a physical server for the office, LunchRush pays a cloud provider to run its website and store its data.",
                "analogy_limit": "Renting a car is a useful analogy, but unlike a car you can scale cloud resources up or down in seconds and run thousands of copies simultaneously.",
                "essential": 1,
            },
            {
                "word": "Client",
                "definition": "A device or application that sends requests to a server and receives responses.",
                "plain": "The customer's phone or laptop that opens the LunchRush website and sends orders.",
                "lunchrush": "Every time a customer opens the app, their device acts as a client — it asks the server for the menu and sends back the order.",
                "analogy_limit": "A client isn't always a human with a device — automated systems and other servers also act as clients.",
                "essential": 1,
            },
            {
                "word": "Server",
                "definition": "A computer or program that provides services, data, or resources in response to requests from clients.",
                "plain": "The computer somewhere on the internet that holds LunchRush's menu, takes orders, and sends back responses.",
                "lunchrush": "LunchRush's ordering application runs on a server that responds whenever a customer clicks 'Order Now'.",
                "analogy_limit": "A server doesn't look like a desk computer — it's usually a rack-mounted machine in a data center, often shared among many customers.",
                "essential": 1,
            },
            {
                "word": "Compute",
                "definition": "The processing power used to run applications and perform calculations in the cloud.",
                "plain": "The raw processing muscle that runs the app — like the engine under the hood.",
                "lunchrush": "Every time a customer searches the menu or submits an order, LunchRush's compute resources do the work of processing that request.",
                "analogy_limit": "More compute doesn't always mean faster results — bottlenecks can occur in storage or network too.",
                "essential": 0,
            },
            {
                "word": "Data center",
                "definition": "A facility housing large numbers of servers, networking equipment, and storage systems used to deliver cloud services.",
                "plain": "A large building full of computers that cloud providers use to run your applications.",
                "lunchrush": "When LunchRush uses a cloud provider, its app runs on servers inside the provider's data centers.",
                "analogy_limit": "A data center isn't a single computer — it can hold tens of thousands of servers across multiple buildings worldwide.",
                "essential": 0,
            },
        ],
    },

    # ── LESSON 2 ──────────────────────────────────────────────────────────────
    {
        "number": 2,
        "title": "Where Should Our Information Go?",
        "challenge": "LunchRush needs to store menu photos and organized order information — and they're not the same kind of data.",
        "story": "Sam has 50 menu photos ready to upload. Riley needs to find any order in seconds during the lunch rush. Jordan asks Alex: 'Where do we keep all of this?' Alex answers with a question: 'Do you need to search inside the photos, or just display them whole?' Jordan pauses. 'Just display them.' 'And the orders?' 'Search them constantly.' Alex nods. 'Then they go in different places.'",
        "exploratory": "Think about two kinds of information: a photo of a sandwich, and a record of who ordered it, when, and for how much. Before learning any vocabulary, write down: What would be a good place to keep each one? What's different about how you'd use them?",
        "activity": "Sort the following 12 data items into two columns — Object Storage or Database — and write one sentence justifying each choice: (A) Menu photo JPG, (B) Customer delivery address, (C) Jordan's welcome audio MP3, (D) Menu item prices, (E) Food safety certificate PDF, (F) Customer order history, (G) Delivery area video MP4, (H) Sandwich inventory count, (I) App logo PNG, (J) Driver delivery totals, (K) Business license scan, (L) Customer star ratings with comments.",
        "explain_plain": "Jordan asks: 'So where are we keeping the photos, and where are the orders?' Explain the storage plan in 2–3 sentences with no technical terms.",
        "explain_tech": "Alex wants a one-paragraph technical summary. Use at least three terms: object storage, bucket, and database.",
        "exit_q1": "What is object storage best suited for? Give one example from LunchRush.",
        "exit_q2": "What makes a database a better choice than object storage for order records?",
        "exit_q3": "True or false: Object storage and databases can never be used together. Explain your answer.",
        "full": 1,
        "terms": [
            {
                "word": "Object storage",
                "definition": "A data storage architecture that manages data as self-contained objects, each consisting of the file content plus metadata.",
                "plain": "A place to store whole files — photos, videos, PDFs — that you drop in and retrieve exactly as they are.",
                "lunchrush": "LunchRush stores all 50 menu photos in object storage so customers can load them quickly as complete image files.",
                "analogy_limit": "Unlike a filing cabinet, object storage can serve billions of files to millions of users simultaneously from anywhere in the world.",
                "essential": 1,
            },
            {
                "word": "Object",
                "definition": "A unit of data in object storage, consisting of the file content plus descriptive metadata such as file type and creation date.",
                "plain": "One file stored in the cloud, bundled with info about itself — like its name, size, and when it was saved.",
                "lunchrush": "Each menu photo is one object stored in LunchRush's image bucket.",
                "analogy_limit": "Objects aren't edited in place — to update a photo you replace the entire object, unlike updating a single field in a database.",
                "essential": 1,
            },
            {
                "word": "Bucket",
                "definition": "A named container in object storage that holds a collection of objects.",
                "plain": "A top-level folder in cloud storage where you group related files — like a drawer labeled 'menu photos'.",
                "lunchrush": "LunchRush creates a bucket called 'lunchrush-images' to hold all menu photos, and a separate bucket for documents.",
                "analogy_limit": "Unlike folders on your computer, buckets in most object storage systems cannot be nested inside other buckets — the structure is flat.",
                "essential": 1,
            },
            {
                "word": "Database",
                "definition": "An organized system for storing, managing, and retrieving structured information with support for searching, filtering, sorting, and updating.",
                "plain": "A smart, organized system that lets you search, filter, and update specific pieces of information quickly — like finding all orders from the last hour.",
                "lunchrush": "LunchRush stores every order in a database — customer name, items, delivery address, timestamp, and status — so Riley can search them instantly.",
                "analogy_limit": "A spreadsheet is a rough analogy — real databases handle millions of rows, multiple simultaneous users, and complex queries far beyond what a spreadsheet can manage.",
                "essential": 1,
            },
            {
                "word": "Storage",
                "definition": "Cloud services that hold data persistently — meaning it stays saved even when nothing is actively processing it.",
                "plain": "The place your information lives when it's not actively being used or processed.",
                "lunchrush": "LunchRush needs storage for menu photos, order records, and business documents — different types for different needs.",
                "analogy_limit": "Storage is not the same as memory (RAM) — storage persists across restarts; RAM is temporary and cleared when a process ends.",
                "essential": 1,
            },
        ],
    },

    # ── LESSON 3 ──────────────────────────────────────────────────────────────
    {
        "number": 3,
        "title": "How Will Our Application Run?",
        "challenge": "LunchRush needs to decide how to run its ordering application — and the choice affects control, cost, and how much Alex has to manage.",
        "story": "Alex places three index cards on the table. 'We have three options for running the app. Each is a different trade-off between control and convenience.' Jordan leans forward. 'Which one is best?' Alex shakes their head. 'That depends on what matters most to you. Let me walk you through each one.'",
        "exploratory": "Imagine you're opening a small restaurant and have three kitchen options: (A) Rent a full kitchen space — you control everything but handle all maintenance. (B) Rent a section in a shared food hall — your section is yours, but the building handles plumbing and power. (C) Use a catering company — you describe the dishes, they handle all equipment. Before learning any cloud vocabulary, answer: Which gives the most control? Which requires the least day-to-day management? Which fits best if you're not sure how busy you'll be?",
        "activity": "Review the three option cards for Virtual Machine, Container, and Serverless. Read the scenario: LunchRush is a small business just starting online. Alex has limited time. Orders spike at noon but are low otherwise. The team wants minimal server management. Choose one option, write one reason it fits, write one trade-off it introduces, and write one option you would NOT choose and why.",
        "explain_plain": "Jordan asks: 'So how is our app going to run?' Explain in 2–3 sentences with no technical terms.",
        "explain_tech": "Write a one-paragraph technical summary using at least three terms: virtual machine, container, or serverless.",
        "exit_q1": "What is the difference between a virtual machine and a container? One sentence each.",
        "exit_q2": "True or false: 'Serverless' means the application runs without any servers. Explain your answer.",
        "exit_q3": "Name one situation where a virtual machine might be a better choice than serverless.",
        "full": 1,
        "terms": [
            {
                "word": "Virtual machine",
                "definition": "A software-based simulation of a physical computer that runs its own operating system and applications.",
                "plain": "A pretend computer running inside a real computer — it has its own OS and you're responsible for everything on it.",
                "lunchrush": "LunchRush could run its ordering app on a VM if it needs full control over the operating system configuration.",
                "analogy_limit": "Unlike a physical computer, a VM can be created, copied, snapshotted, or deleted in seconds — and dozens can run on a single physical server.",
                "essential": 1,
            },
            {
                "word": "Operating system",
                "definition": "Software that manages a computer's hardware resources and provides core services for applications to run.",
                "plain": "The foundation software — like Linux or Windows — that everything else runs on top of.",
                "lunchrush": "With a VM, LunchRush is responsible for keeping the operating system updated, patched, and secure.",
                "analogy_limit": "Containers don't each have their own OS — they share the host OS kernel, which is a key difference from VMs and affects both efficiency and isolation.",
                "essential": 1,
            },
            {
                "word": "Container",
                "definition": "A packaged unit containing an application and all its dependencies that shares the host operating system but runs in isolation.",
                "plain": "A box that holds your app and everything it needs to run, so it works exactly the same anywhere you deploy it.",
                "lunchrush": "LunchRush could package its ordering app as a container so it runs identically whether Alex tests it locally or deploys it to the cloud.",
                "analogy_limit": "Unlike a shipping container, software containers share the host OS kernel — they provide process isolation but not full OS isolation like a VM does.",
                "essential": 1,
            },
            {
                "word": "Container image",
                "definition": "A read-only blueprint used to create a container, built from a Dockerfile that specifies the app's code, dependencies, and configuration.",
                "plain": "The recipe used to create a container — a snapshot of everything the app needs, ready to be run anywhere.",
                "lunchrush": "LunchRush's developer builds a container image once; it can then be used to launch many identical, consistent containers.",
                "analogy_limit": "An image is static and not running — a container is what you get when you actually run the image. One image can create many containers.",
                "essential": 1,
            },
            {
                "word": "Serverless",
                "definition": "A cloud execution model where the provider manages all server infrastructure; you provide code and pay only per execution.",
                "plain": "You write the function and hand it to the cloud — it runs when needed, scales automatically, and you never touch a server.",
                "lunchrush": "LunchRush could use serverless to handle order notifications — the function only runs when an order arrives, costing nothing during quiet periods.",
                "analogy_limit": "Serverless does NOT mean no servers exist — servers still run your code. It means YOU don't provision, configure, or manage them. The term describes your experience, not the underlying reality.",
                "essential": 1,
            },
        ],
    },

    # ── LESSON 4 ──────────────────────────────────────────────────────────────
    {
        "number": 4,
        "title": "How Does an Order Travel?",
        "challenge": "A customer submits an order — but how does it find the right server, and how does the server know what to do with it?",
        "story": "A customer types 'lunchrush.example' into their phone and taps Order. Jordan watches over Alex's shoulder. 'What just happened?' Alex grins. 'A lot, actually — and it all happened in about two seconds. Let me walk you through every step.'",
        "exploratory": "Imagine you're mailing a letter to a friend. You write the address, the post office looks up the route, the letter travels through several sorting centers, and your friend receives it. Before learning any vocabulary, describe what you think happens between a customer typing a website address and the order arriving at LunchRush's server. What needs to exist? What translates the address into a location?",
        "activity": "Arrange these six steps in the correct order, then label each one with the vocabulary term that describes what's happening: (1) Customer types 'lunchrush.example' in browser, (2) Browser asks a directory service for the server's address, (3) Directory returns a numeric address, (4) Browser sends a formatted request to that address, (5) Server receives the request and routes it to the order service, (6) Order service responds with a confirmation.",
        "explain_plain": "Jordan asks: 'How does a customer's order actually get to us?' Explain the journey in 2–3 sentences with no technical terms.",
        "explain_tech": "Write a one-paragraph technical summary using at least three terms: DNS, HTTP, and API.",
        "exit_q1": "What does DNS do? Why is it needed?",
        "exit_q2": "What is an API? Give one example of how LunchRush uses one.",
        "exit_q3": "Name one difference between HTTP and an API.",
        "full": 1,
        "terms": [
            {
                "word": "Network",
                "definition": "A system of connected devices and infrastructure that enables communication and data transfer between computers.",
                "plain": "The infrastructure of cables, routers, and wireless signals that lets computers anywhere in the world talk to each other.",
                "lunchrush": "Every time a customer places an order, the data travels across the network — from their phone, through the internet, to LunchRush's server.",
                "analogy_limit": "The internet isn't one network — it's millions of independently owned and operated networks that agree to interconnect.",
                "essential": 1,
            },
            {
                "word": "IP address",
                "definition": "A numerical label assigned to each device on a network, used to identify and locate it for communication.",
                "plain": "A unique number that identifies a specific computer on the internet — like a street address for data.",
                "lunchrush": "LunchRush's server has an IP address. DNS translates the human-readable domain name into this number so browsers can find it.",
                "analogy_limit": "IP addresses can change — they're not permanently tied to a physical machine. Cloud servers often get new IP addresses when restarted.",
                "essential": 1,
            },
            {
                "word": "DNS",
                "definition": "Domain Name System — a distributed directory that translates human-readable domain names into IP addresses.",
                "plain": "The internet's phone book — you give it a name like 'lunchrush.example' and it finds the number (IP address) behind it.",
                "lunchrush": "When a customer types 'lunchrush.example', DNS looks up and returns the IP address of LunchRush's server so the browser knows where to connect.",
                "analogy_limit": "Unlike a phone book, DNS lookups happen in milliseconds, are distributed across thousands of servers worldwide, and are cached to avoid repeated lookups.",
                "essential": 1,
            },
            {
                "word": "HTTP",
                "definition": "Hypertext Transfer Protocol — the standard format and rules for requests and responses between web clients and servers.",
                "plain": "The agreed language that browsers and web servers use to talk to each other — it defines how to ask for something and how to respond.",
                "lunchrush": "When a customer's browser asks for the LunchRush menu, it sends an HTTP GET request. When submitting an order, it sends an HTTP POST request.",
                "analogy_limit": "Not all APIs use HTTP — some use WebSocket for real-time communication, gRPC for high-performance services, or other protocols. HTTP is common but not universal.",
                "essential": 1,
            },
            {
                "word": "API",
                "definition": "Application Programming Interface — a defined contract that specifies how one piece of software can request services or data from another.",
                "plain": "A set of rules that lets two apps talk to each other in a structured, predictable way — like a waiter who carries requests between the kitchen and the customer.",
                "lunchrush": "LunchRush's frontend uses an API to send order data to the backend — the API defines exactly what format the order must be in and what response to expect.",
                "analogy_limit": "An API is not the same as the network — the network carries the data, but the API defines the structure and meaning of the conversation. You can have an API over many different transport mechanisms.",
                "essential": 1,
            },
        ],
    },

    # ── LESSON 5 ──────────────────────────────────────────────────────────────
    {
        "number": 5,
        "title": "What Happens During the Lunch Rush?",
        "challenge": "At noon, far more customers try to order at once than the app was set up to handle. Orders are slow or failing.",
        "story": "It's 12:02 p.m. The dashboard lights up red. Average order time has jumped from 2 seconds to 18. Riley's phone is ringing — customers are complaining. Jordan looks at Alex. 'What's happening?' Alex pulls up a graph. 'We have one copy of the app trying to serve 200 customers at once. We need more lanes on this road — and we need them fast.'",
        "exploratory": "Think about a grocery store with one checkout lane. Fifty customers arrive at once. What would the store do to handle the rush? What if the problem wasn't the checkout lanes but the stockroom running out of bags? Before learning any vocabulary, describe: What would you do if your app suddenly had ten times as many users? What might that not fix?",
        "activity": "Use the following scenario to model scaling: LunchRush normally runs 1 application instance. At noon, 9 orders arrive per second. Each instance handles 3 orders per second. Draw a diagram showing: (1) the problem with 1 instance, (2) how 3 instances plus a load balancer solves it, (3) one situation where adding more instances still wouldn't help.",
        "explain_plain": "Jordan asks: 'Why was everything so slow, and what did we do about it?' Explain in 2–3 sentences with no technical terms.",
        "explain_tech": "Write a one-paragraph technical summary using at least three terms: scaling, application instance, and load balancing.",
        "exit_q1": "What is the difference between horizontal scaling and vertical scaling?",
        "exit_q2": "What does a load balancer do? Why is it needed when you have multiple instances?",
        "exit_q3": "Name one situation where adding more application instances would NOT solve a performance problem.",
        "full": 1,
        "terms": [
            {
                "word": "Scaling",
                "definition": "Increasing or decreasing computing resources to match changes in demand — either by adding more instances (horizontal) or by upgrading existing ones (vertical).",
                "plain": "Adding more horsepower when things get busy, reducing it when they slow down — so you're not paying for capacity you don't need.",
                "lunchrush": "LunchRush scales horizontally during the noon rush by running three copies of the ordering app instead of one.",
                "analogy_limit": "Scaling up doesn't fix every bottleneck — if the database, network, or an external service is the constraint, more app instances won't help.",
                "essential": 1,
            },
            {
                "word": "Application instance",
                "definition": "One running copy of an application, handling requests independently from other copies.",
                "plain": "Think of it as one open restaurant — if it gets too busy, you open another location next door to share the load.",
                "lunchrush": "LunchRush normally runs one instance but launches two more at noon when orders spike, so each instance handles a manageable share.",
                "analogy_limit": "Instances share the same database — if the database can't handle the increased query load, adding more app instances can make the database problem worse.",
                "essential": 1,
            },
            {
                "word": "Load balancing",
                "definition": "Distributing incoming network requests across multiple application instances to prevent any single one from being overwhelmed.",
                "plain": "A traffic director that routes each customer to whichever copy of the app is least busy — so no single instance gets swamped.",
                "lunchrush": "LunchRush's load balancer sits in front of three running instances and distributes incoming orders evenly across all three.",
                "analogy_limit": "A load balancer distributes traffic but doesn't create capacity — you still need enough instances running to handle the total load.",
                "essential": 1,
            },
            {
                "word": "Orchestration",
                "definition": "The automated management of containers or services across infrastructure, including starting, stopping, scaling, and recovering from failures.",
                "plain": "A system that automatically starts, stops, and restarts containers so you don't have to do it manually whenever demand changes.",
                "lunchrush": "If LunchRush grows, it might use an orchestration tool to automatically scale the app up at 11:45 a.m. every day before the rush.",
                "analogy_limit": "Orchestration manages containers — it's not the same as a load balancer, which distributes traffic. They are complementary, not interchangeable.",
                "essential": 0,
            },
            {
                "word": "Kubernetes",
                "definition": "An open-source container orchestration platform that automates deployment, scaling, and management of containerized applications across clusters of machines.",
                "plain": "A popular tool for automatically managing and scaling containers — like a smart operations manager for your app infrastructure.",
                "lunchrush": "Kubernetes is one option for orchestrating LunchRush's containers at scale — but it adds complexity and is not required for every application.",
                "analogy_limit": "Kubernetes is powerful but has a steep learning curve. Not every application needs it — small apps often do fine with simpler approaches.",
                "essential": 0,
            },
        ],
    },

    # ── LESSON 6 ──────────────────────────────────────────────────────────────
    {
        "number": 6,
        "title": "Who Can Change the Menu?",
        "challenge": "Staff members need different levels of access to business information, but no one has formally decided who can do what.",
        "story": "A customer calls to complain — they were charged the wrong price. Someone changed it at 11 p.m. and no one knows who. Jordan calls a team meeting. 'Does everyone on the team have access to everything?' The room goes quiet. Sam: 'I only updated the description.' Riley: 'I don't even know how to edit the menu.' Alex checks the logs. The price was changed by an account with full access. Jordan: 'We need to fix this today.'",
        "exploratory": "Think of a place with different access levels — a hospital, office building, school, or hotel. Answer two questions before learning any vocabulary: (1) How does that place confirm who you are? (2) Once it knows who you are, how does it decide what you're allowed to do or enter?",
        "activity": "Using the LunchRush Access Policy below, fill in the permissions table. Mark each cell R (read), W (write), or — (no access). Apply least privilege — give each person only what they need. Policy: Jordan can view and change anything. Sam manages menu content only — no financial records or prices. Riley views orders and updates delivery status — no menu or financial data. Alex manages technical config — no customer payment info during normal operations. After completing the table, choose two cells where you were unsure and write one sentence explaining your reasoning.",
        "explain_plain": "Jordan wants to understand the new access plan. Explain in 2–3 sentences with no technical terms.",
        "explain_tech": "Write a one-paragraph technical summary using at least three terms: authentication, authorization, IAM, least privilege, or shared responsibility.",
        "exit_q1": "What is the difference between authentication and authorization? Give a real-world example of each.",
        "exit_q2": "What does the principle of least privilege mean? Give one example from LunchRush.",
        "exit_q3": "True or false: The cloud provider is responsible for making sure Sam can't change menu prices. Explain your answer.",
        "full": 1,
        "terms": [
            {
                "word": "Authentication",
                "definition": "The process of verifying that someone is who they claim to be, using credentials such as passwords, tokens, or biometrics.",
                "plain": "Proving you are who you say you are — like showing your ID at the door before you're allowed in.",
                "lunchrush": "Before anyone on the LunchRush team can access the system, they must log in with their credentials to prove their identity.",
                "analogy_limit": "An ID card can be borrowed or forged. Digital authentication systems add extra signals — like a one-time code sent to your phone — to make impersonation much harder.",
                "essential": 1,
            },
            {
                "word": "Authorization",
                "definition": "The process of determining what an authenticated user is permitted to access or do within a system.",
                "plain": "After you prove who you are, the system checks what you're allowed to do — not everything is open to everyone.",
                "lunchrush": "Sam is authenticated as a menu manager — but authorization means Sam can edit menu items and cannot access financial records.",
                "analogy_limit": "Authentication and authorization are often confused because they happen in sequence. You can be authenticated (identity confirmed) and still be denied access to specific resources.",
                "essential": 1,
            },
            {
                "word": "IAM",
                "definition": "Identity and Access Management — the policies, tools, and processes used to manage who can access what in a system.",
                "plain": "The system that controls who can log in and what each person or service is allowed to do once they're in.",
                "lunchrush": "LunchRush uses IAM policies to define that Sam can edit menu content, Riley can update delivery status, and Alex can configure the technical systems.",
                "analogy_limit": "IAM is a category of functionality, not a single product. The concept applies to both cloud systems and traditional on-premises systems.",
                "essential": 1,
            },
            {
                "word": "Least privilege",
                "definition": "The principle of granting users, systems, or applications only the minimum access necessary to perform their job — nothing more.",
                "plain": "Give people exactly what they need to do their job — and nothing extra. This limits the damage if something goes wrong.",
                "lunchrush": "Riley can update delivery status but cannot change the menu or view financial records — that's least privilege applied to a delivery coordinator role.",
                "analogy_limit": "Least privilege requires deliberate design and regular review — it doesn't happen automatically. As roles change, permissions need to be updated.",
                "essential": 1,
            },
            {
                "word": "Shared responsibility",
                "definition": "The division of security obligations between the cloud provider and the customer, varying by service type.",
                "plain": "The cloud company protects the infrastructure; you protect your data, applications, and access policies. Both have responsibilities.",
                "lunchrush": "The cloud provider keeps LunchRush's servers physically secure and the platform patched. LunchRush is responsible for its own IAM policies — including who can change prices.",
                "analogy_limit": "What counts as the customer's responsibility varies by service type — more managed services shift more infrastructure responsibility to the provider, but the customer always owns their data and access controls.",
                "essential": 1,
            },
        ],
    },

    # ── LESSON 7 ──────────────────────────────────────────────────────────────
    {
        "number": 7,
        "title": "How Do We Release an Update?",
        "challenge": "LunchRush wants to add a new 'Meal of the Day' feature without taking the site down or breaking orders mid-rush.",
        "story": "Sam has designed a new feature — a daily special that appears at the top of the menu. The dev team has written the code. But Jordan is nervous: 'What if it breaks the site while customers are ordering? Can we test it first?' Alex says: 'That's exactly why we have a pipeline. We don't just push code and hope. Every change goes through a sequence of steps automatically.'",
        "exploratory": "Imagine you're updating a printed menu at a restaurant. You draft the change, someone checks for errors, a manager approves it, and then you print and distribute the new menus. Before learning any vocabulary, describe: What steps would make you confident a software change is safe to release? What would you want to verify before it goes live?",
        "activity": "Arrange the following six pipeline stages in the correct order, then draw two versions — one for continuous delivery (with a manual approval step) and one for continuous deployment (fully automated). Stages: Change code, Build, Run automated tests, Manual approval (use only where applicable), Deploy to production, Verify the release works. After drawing both, write one sentence explaining the key difference between the two.",
        "explain_plain": "Jordan asks: 'How do we release new features safely?' Explain in 2–3 sentences with no technical terms.",
        "explain_tech": "Write a one-paragraph technical summary using at least three terms: pipeline, continuous integration, and continuous delivery.",
        "exit_q1": "What is a CI/CD pipeline? Describe it in one sentence.",
        "exit_q2": "What is the main difference between continuous delivery and continuous deployment?",
        "exit_q3": "True or false: A pipeline guarantees no bugs will reach production. Explain your answer.",
        "full": 1,
        "terms": [
            {
                "word": "Pipeline",
                "definition": "An automated sequence of steps — build, test, approve, deploy — that moves a code change from development to production.",
                "plain": "An assembly line for software. Each change goes through automatic checks before it's allowed to go live.",
                "lunchrush": "LunchRush's pipeline automatically builds and tests the Meal of the Day feature before Alex approves it for release.",
                "analogy_limit": "A pipeline reduces risk but doesn't guarantee error-free releases — it only catches problems that your tests are designed to detect.",
                "essential": 1,
            },
            {
                "word": "Continuous integration",
                "definition": "The practice of automatically building and testing every code change as soon as it is submitted to the shared codebase.",
                "plain": "Every time a developer saves a change, the system automatically checks whether the code still builds and passes tests.",
                "lunchrush": "When Alex pushes the Meal of the Day code, CI immediately builds it and runs all existing tests to check for regressions.",
                "analogy_limit": "CI only tests what your existing tests cover — it cannot catch problems that no test anticipates.",
                "essential": 1,
            },
            {
                "word": "Continuous delivery",
                "definition": "A practice where code is always kept in a deployable state, but a human must approve the final release to production.",
                "plain": "The app is always ready to go live — but a person still makes the final decision to press the button.",
                "lunchrush": "LunchRush uses continuous delivery — the pipeline prepares the Meal of the Day release, and Alex reviews and approves it before it goes live.",
                "analogy_limit": "Continuous delivery is NOT the same as continuous deployment. Delivery preserves a human approval gate; deployment removes it.",
                "essential": 1,
            },
            {
                "word": "Deployment",
                "definition": "The process of releasing and running a new version of an application in a target environment such as production.",
                "plain": "Putting the new version of the app live so real customers can use it.",
                "lunchrush": "After Alex approves it, the pipeline deploys the Meal of the Day feature to LunchRush's production server automatically.",
                "analogy_limit": "Deployment is not the same as development — it's the act of releasing code that's already been built and tested.",
                "essential": 1,
            },
            {
                "word": "Automation",
                "definition": "Using software to perform tasks consistently and repeatedly without manual human intervention each time.",
                "plain": "Setting up the system to handle repetitive steps on its own — so humans focus on decisions, not clicking the same buttons.",
                "lunchrush": "LunchRush automates its build and test steps so Alex doesn't have to run them manually with every code change.",
                "analogy_limit": "Automation is reliable for well-defined, predictable steps — but it can't substitute for human judgment when something unexpected happens.",
                "essential": 1,
            },
        ],
    },

    # ── LESSON 8 ──────────────────────────────────────────────────────────────
    {
        "number": 8,
        "title": "Why Are Orders Slow?",
        "challenge": "Customers are reporting slow orders. The team has data but needs to separate what they can observe from what they still need to investigate.",
        "story": "It's Tuesday at 12:04 p.m. Orders are taking 12 seconds instead of 2. Riley's phone is ringing. Alex pulls up the dashboard: average order time is 12s, one server shows 91% CPU, and the logs show three timeout errors in the last 60 seconds. Jordan: 'So the server is broken?' Alex: 'The server is under stress. That's not the same as knowing why. Let's look at what the data actually tells us — and what it doesn't.'",
        "exploratory": "Look at this fictional dashboard data: Average order time: 12 seconds (normal: 2 seconds). Server CPU: 91%. Error log: 3 timeout errors in the last 60 seconds. Before learning any vocabulary, write: (1) Three things you can say for certain based on this data. (2) One conclusion you cannot yet confirm. (3) Two additional pieces of information you would want before deciding what to fix.",
        "activity": "Using the fictional dashboard data above, complete this investigation worksheet: (1) List three observations — things the data shows directly. (2) Write one hypothesis — a possible explanation that fits the data but isn't yet proven. (3) List two more data points you would want to collect. (4) Write one reason why high CPU alone is not enough to identify the root cause.",
        "explain_plain": "Jordan asks: 'What's wrong with our app right now?' Explain what you know and don't know in 2–3 sentences with no technical terms.",
        "explain_tech": "Write a one-paragraph technical summary using at least three terms: monitoring, metric, log, alert, or latency.",
        "exit_q1": "What is the difference between a metric and a log?",
        "exit_q2": "What is latency? How is it being measured in the LunchRush scenario?",
        "exit_q3": "Why is one elevated metric not enough to identify the root cause of a performance problem?",
        "full": 1,
        "terms": [
            {
                "word": "Monitoring",
                "definition": "The continuous collection and review of signals — metrics, logs, and alerts — to track the health and performance of a system over time.",
                "plain": "Watching the system continuously so you notice problems the moment they start, not after customers complain.",
                "lunchrush": "LunchRush's monitoring dashboard shows order times, server CPU load, and error rates in real time so Alex can spot problems immediately.",
                "analogy_limit": "Monitoring shows you what is happening — it doesn't tell you why. Investigation is still required to find root causes.",
                "essential": 1,
            },
            {
                "word": "Metric",
                "definition": "A measured numerical value recorded over time, used to track the performance, health, or behavior of a system.",
                "plain": "A number that gets measured repeatedly over time — like order speed, error rate, or CPU usage.",
                "lunchrush": "LunchRush tracks average order time as a key metric — today it's 12 seconds instead of the normal 2, which triggered an investigation.",
                "analogy_limit": "One metric alone rarely explains a problem — you need to look at multiple signals together to understand what's happening.",
                "essential": 1,
            },
            {
                "word": "Log",
                "definition": "A timestamped, sequential record of events that occurred in a system, used for debugging, auditing, and investigation.",
                "plain": "A diary the system keeps — every event gets written down with an exact timestamp so you can trace what happened and when.",
                "lunchrush": "LunchRush's logs show three timeout errors at 12:03 p.m. — a clue, but not proof of the root cause on its own.",
                "analogy_limit": "Logs record what happened, not why — interpreting them still requires judgment and cross-referencing with other signals.",
                "essential": 1,
            },
            {
                "word": "Alert",
                "definition": "An automatic notification triggered when a monitored metric crosses a defined threshold, prompting investigation or action.",
                "plain": "An alarm that fires automatically when something looks wrong — so you don't have to watch the dashboard all day.",
                "lunchrush": "LunchRush sets an alert to notify Alex immediately if average order time exceeds 5 seconds.",
                "analogy_limit": "An alert tells you a threshold was crossed — it doesn't diagnose the cause. It's the start of an investigation, not the end.",
                "essential": 1,
            },
            {
                "word": "Latency",
                "definition": "The time elapsed between sending a request and receiving a response — a key measure of system responsiveness.",
                "plain": "How long it takes to get an answer — the delay between asking and receiving.",
                "lunchrush": "LunchRush's order latency spiked from 2 seconds to 12 seconds — something in the system is slowing down responses significantly.",
                "analogy_limit": "High latency has many possible causes — network congestion, database slowness, server overload, or slow external services. It is a symptom, not a diagnosis.",
                "essential": 1,
            },
        ],
    },
]


# ── Database init ──────────────────────────────────────────────────────────────

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(Lesson).count() == 0:
        for ld in LESSONS:
            lesson = Lesson(
                number=ld["number"],
                title=ld["title"],
                challenge=ld["challenge"],
                story=ld["story"],
                exploratory=ld["exploratory"],
                activity=ld["activity"],
                explain_plain=ld["explain_plain"],
                explain_tech=ld["explain_tech"],
                exit_q1=ld["exit_q1"],
                exit_q2=ld["exit_q2"],
                exit_q3=ld["exit_q3"],
                full=ld["full"],
            )
            db.add(lesson)
            db.flush()
            for td in ld["terms"]:
                term = Term(
                    lesson_id=lesson.id,
                    word=td["word"],
                    definition=td["definition"],
                    plain=td["plain"],
                    lunchrush=td["lunchrush"],
                    analogy_limit=td["analogy_limit"],
                    essential=td["essential"],
                )
                db.add(term)
        db.commit()
    db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
