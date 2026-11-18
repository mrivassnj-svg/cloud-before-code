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
        "story": (
            "Jordan is at the library with the team, flipping through a stack of printed order forms. "
            "'We need to let people order online,' Jordan says. 'But I keep hearing the word cloud — is that just a fancy word for the internet?' "
            "Alex pulls out a napkin sketch. 'Think about how you check your bank balance on your phone. "
            "Your phone doesn't hold your account — it asks a computer somewhere else, and that computer responds. "
            "That's essentially what a cloud-based app does. The heavy lifting happens on a computer you never see or touch.' "
            "Jordan stares at the napkin. 'So our menu and orders would live on someone else's computer?' "
            "'Rented space on someone else's computer,' Alex says. 'The same way you rent a mailbox at the post office instead of building your own.'"
        ),
        "exploratory": (
            "Before learning any vocabulary, think about how an ATM works. "
            "You walk up with a card, punch in a PIN, and cash comes out — but the ATM itself doesn't hold your money. "
            "Sketch or list the pieces involved: What device are you using? Where does your account information actually live? "
            "What connects your card to that information? "
            "Now think about a customer ordering from LunchRush online — which pieces are the same, and which are different?"
        ),
        "activity": (
            "Draw a simple diagram with three labeled boxes: Customer Device, App, and Information Store. "
            "Draw arrows showing what travels between them when a customer places an order. "
            "Label each arrow with what is being sent — for example: 'menu request', 'order details', 'confirmation'. "
            "Think of the Customer Device like a person at an ATM: it asks for something. "
            "Think of the Information Store like the bank's mainframe: it holds the real data and responds."
        ),
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
                "analogy_limit": (
                    "Renting a mailbox is a useful starting point, but unlike a mailbox, cloud resources can be "
                    "scaled up or down in seconds and thousands of copies can run simultaneously. "
                    "A mailbox is a fixed, single-purpose slot."
                ),
                "essential": 1,
            },
            {
                "word": "Client",
                "definition": "A device or application that sends requests to a server and receives responses.",
                "plain": "The customer's phone or laptop that opens the LunchRush website and sends orders.",
                "lunchrush": "Every time a customer opens the app, their device acts as a client — it asks the server for the menu and sends back the order.",
                "analogy_limit": (
                    "An ATM card is a useful image for a client, but a client isn't always a human with a device. "
                    "Automated systems, background jobs, and other servers also act as clients when they request data."
                ),
                "essential": 1,
            },
            {
                "word": "Server",
                "definition": "A computer or program that provides services, data, or resources in response to requests from clients.",
                "plain": "The computer somewhere on the internet that holds LunchRush's menu, takes orders, and sends back responses.",
                "lunchrush": "LunchRush's ordering application runs on a server that responds whenever a customer clicks 'Order Now'.",
                "analogy_limit": (
                    "A server isn't a desk computer — it's usually a rack-mounted machine in a data center, "
                    "often shared among many customers. Unlike a bank's vault, a single server can respond to "
                    "thousands of requests per second from people all over the world."
                ),
                "essential": 1,
            },
            {
                "word": "Compute",
                "definition": "The processing power used to run applications and perform calculations in the cloud.",
                "plain": "The raw processing muscle that runs the app — like the engine under the hood.",
                "lunchrush": "Every time a customer searches the menu or submits an order, LunchRush's compute resources do the work of processing that request.",
                "analogy_limit": (
                    "More compute doesn't always mean faster results — bottlenecks can occur in storage or network too. "
                    "Think of a hospital with more doctors but only one working elevator: adding staff doesn't fix the elevator."
                ),
                "essential": 0,
            },
            {
                "word": "Data center",
                "definition": "A facility housing large numbers of servers, networking equipment, and storage systems used to deliver cloud services.",
                "plain": "A large building full of computers that cloud providers use to run your applications.",
                "lunchrush": "When LunchRush uses a cloud provider, its app runs on servers inside the provider's data centers.",
                "analogy_limit": (
                    "A data center isn't a single building like a library branch — it can hold tens of thousands of servers "
                    "across multiple buildings worldwide, with backup power, climate control, and 24-hour physical security."
                ),
                "essential": 0,
            },
        ],
    },

    # ── LESSON 2 ──────────────────────────────────────────────────────────────
    {
        "number": 2,
        "title": "Where Should Our Information Go?",
        "challenge": "LunchRush needs to store menu photos and organized order information — and they're not the same kind of data.",
        "story": (
            "Sam spreads 50 printed menu photos across Jordan's desk alongside a stack of order receipts. "
            "'Where does all of this go online?' Sam asks. "
            "Alex picks up a photo and a receipt. 'Think about how a hospital manages records. "
            "MRI scan images and a patient's appointment history are both important — but they're stored differently. "
            "The images are huge files you retrieve whole, like pulling a folder from a filing room. "
            "The appointment history is structured data you search through constantly — who came in, when, what for. "
            "Same idea here: your photos and your order records need different kinds of storage.' "
            "Jordan points to the photos. 'So the photos go in the filing room?' "
            "'Exactly,' Alex says. 'And the orders go in a system built for searching.'"
        ),
        "exploratory": (
            "Think about a public library. It holds two very different kinds of things: "
            "physical books on shelves (you check one out whole — you don't read just a paragraph from the catalog) "
            "and a card catalog or database (you search by title, author, or subject to find exactly what you need). "
            "Before learning any vocabulary, write down: "
            "What would be a good place to keep a menu photo? What about a customer's order history? "
            "What's different about how you would use each one?"
        ),
        "activity": (
            "Sort the following 12 data items into two columns — Object Storage or Database — "
            "and write one sentence justifying each choice. "
            "Think of Object Storage as the library's physical shelves: whole items you retrieve as-is. "
            "Think of Database as the library's searchable catalog: structured records you query and filter. "
            "(A) Menu photo JPG, (B) Customer delivery address, (C) Jordan's welcome audio MP3, "
            "(D) Menu item prices, (E) Food safety certificate PDF, (F) Customer order history, "
            "(G) Delivery area video MP4, (H) Sandwich inventory count, (I) App logo PNG, "
            "(J) Driver delivery totals, (K) Business license scan, (L) Customer star ratings with comments."
        ),
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
                "analogy_limit": (
                    "Library shelves are a helpful image, but physical shelves have one copy per book. "
                    "Object storage can serve the same file to millions of users simultaneously from anywhere in the world, "
                    "and there is no limit on copies."
                ),
                "essential": 1,
            },
            {
                "word": "Object",
                "definition": "A unit of data in object storage, consisting of the file content plus descriptive metadata such as file type and creation date.",
                "plain": "One file stored in the cloud, bundled with info about itself — like its name, size, and when it was saved.",
                "lunchrush": "Each menu photo is one object stored in LunchRush's image bucket.",
                "analogy_limit": (
                    "Unlike a library book, which you can annotate or repair in place, "
                    "objects in object storage are not edited in place — to update a photo you replace the entire object. "
                    "You cannot change just one page."
                ),
                "essential": 1,
            },
            {
                "word": "Bucket",
                "definition": "A named container in object storage that holds a collection of objects.",
                "plain": "A top-level folder in cloud storage where you group related files — like a labeled drawer in a filing cabinet.",
                "lunchrush": "LunchRush creates a bucket called 'lunchrush-images' to hold all menu photos, and a separate bucket for documents.",
                "analogy_limit": (
                    "Unlike physical filing cabinet drawers, which can hold folders inside folders, "
                    "buckets in most object storage systems cannot be nested inside other buckets — the structure is flat. "
                    "Organization is managed through naming conventions, not subfolders."
                ),
                "essential": 1,
            },
            {
                "word": "Database",
                "definition": "An organized system for storing, managing, and retrieving structured information with support for searching, filtering, sorting, and updating.",
                "plain": "A smart, organized system that lets you search, filter, and update specific pieces of information quickly — like finding all orders from the last hour.",
                "lunchrush": "LunchRush stores every order in a database — customer name, items, delivery address, timestamp, and status — so Riley can search them instantly.",
                "analogy_limit": (
                    "A school's student information system is a closer analogy than a spreadsheet — real databases handle "
                    "millions of rows, enforce rules about data consistency, support many simultaneous users, and run "
                    "complex queries across tables. A spreadsheet breaks under that load."
                ),
                "essential": 1,
            },
            {
                "word": "Storage",
                "definition": "Cloud services that hold data persistently — meaning it stays saved even when nothing is actively processing it.",
                "plain": "The place your information lives when it's not actively being used or processed.",
                "lunchrush": "LunchRush needs storage for menu photos, order records, and business documents — different types for different needs.",
                "analogy_limit": (
                    "Storage is not the same as memory (RAM). Think of storage as a filing cabinet and RAM as "
                    "the papers spread out on your desk right now. When you leave the office, the desk is cleared "
                    "but the cabinet stays full. RAM is temporary; storage persists."
                ),
                "essential": 1,
            },
        ],
    },

    # ── LESSON 3 ──────────────────────────────────────────────────────────────
    {
        "number": 3,
        "title": "How Will Our Application Run?",
        "challenge": "LunchRush needs to decide how to run its ordering application — and the choice affects control, cost, and how much Alex has to manage.",
        "story": (
            "Alex places three index cards on the break room table. "
            "'Think about how you could set up a workspace when you start a new job,' Alex says. "
            "'Option one: rent a whole apartment. You control everything — paint the walls, change the locks — but you handle every repair yourself. "
            "Option two: rent a furnished room in a managed building. The landlord handles plumbing and electricity; you manage what's inside your room. "
            "Option three: use a co-working space by the hour. You show up, do your work, and leave. No lease, no maintenance — you only pay for the time you use.' "
            "Jordan leans in. 'Which one is best for us?' "
            "Alex shakes their head. 'That depends on how much control you need and how much maintenance you want to handle. Let me walk you through each one.'"
        ),
        "exploratory": (
            "Imagine you need a workspace for a new project. You have three options: "
            "(A) Rent an empty office suite — you control everything but must handle all IT, furniture, and maintenance yourself. "
            "(B) Rent a managed office suite — the building handles power, internet, and cleaning; you manage your own desk setup. "
            "(C) Book a hot desk at a co-working space — you pay per hour, there is no setup, and you can leave whenever the project ends. "
            "Before learning any cloud vocabulary, answer: "
            "Which gives the most control? Which requires the least day-to-day management? "
            "Which fits best if you are not sure how busy you will be?"
        ),
        "activity": (
            "Review the three option cards for Virtual Machine, Container, and Serverless. "
            "Read the scenario: LunchRush is a small business just starting online. Alex has limited time. "
            "Orders spike at noon but are low otherwise. The team wants minimal server management. "
            "Choose one option, write one reason it fits, write one trade-off it introduces, "
            "and write one option you would NOT choose and why. "
            "Think of the options as workspace choices: VM = empty office suite, Container = managed furnished room, "
            "Serverless = co-working hot desk."
        ),
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
                "analogy_limit": (
                    "An empty office suite is a useful image, but unlike renting a physical office, "
                    "a VM can be created, copied, snapshotted, or deleted in seconds — and dozens can share "
                    "a single physical server simultaneously. No physical office can do that."
                ),
                "essential": 1,
            },
            {
                "word": "Operating system",
                "definition": "Software that manages a computer's hardware resources and provides core services for applications to run.",
                "plain": "The foundation software — like Linux or Windows — that everything else runs on top of.",
                "lunchrush": "With a VM, LunchRush is responsible for keeping the operating system updated, patched, and secure.",
                "analogy_limit": (
                    "Think of the OS as the building's core utilities — electricity and plumbing. "
                    "Containers don't each get their own utilities; they share the building's infrastructure. "
                    "That shared OS kernel is a key difference from VMs, affecting both efficiency and security isolation."
                ),
                "essential": 1,
            },
            {
                "word": "Container",
                "definition": "A packaged unit containing an application and all its dependencies that shares the host operating system but runs in isolation.",
                "plain": "A box that holds your app and everything it needs to run, so it works exactly the same anywhere you deploy it.",
                "lunchrush": "LunchRush could package its ordering app as a container so it runs identically whether Alex tests it locally or deploys it to the cloud.",
                "analogy_limit": (
                    "A furnished rental room is a good analogy — your belongings are yours and your space is separated from neighbors, "
                    "but you share the building's plumbing and electricity. "
                    "Unlike a shipping container, software containers share the host OS kernel — "
                    "they provide process isolation but not full OS isolation like a VM does."
                ),
                "essential": 1,
            },
            {
                "word": "Container image",
                "definition": "A read-only blueprint used to create a container, built from a Dockerfile that specifies the app's code, dependencies, and configuration.",
                "plain": "The recipe used to create a container — a snapshot of everything the app needs, ready to be run anywhere.",
                "lunchrush": "LunchRush's developer builds a container image once; it can then be used to launch many identical, consistent containers.",
                "analogy_limit": (
                    "An image is like a floor plan for an apartment — static, not yet lived in. "
                    "A container is what you get when you actually move in and start using the space. "
                    "One floor plan can be used to build many identical apartments; one image can create many containers."
                ),
                "essential": 1,
            },
            {
                "word": "Serverless",
                "definition": "A cloud execution model where the provider manages all server infrastructure; you provide code and pay only per execution.",
                "plain": "You write the function and hand it to the cloud — it runs when needed, scales automatically, and you never touch a server.",
                "lunchrush": "LunchRush could use serverless to handle order notifications — the function only runs when an order arrives, costing nothing during quiet periods.",
                "analogy_limit": (
                    "A co-working hot desk is a useful image, but here is where the analogy stops being accurate: "
                    "serverless does NOT mean no servers exist — servers still run your code. "
                    "It means YOU don't provision, configure, or manage them. "
                    "The term describes your experience as a developer, not the physical reality underneath."
                ),
                "essential": 1,
            },
        ],
    },

    # ── LESSON 4 ──────────────────────────────────────────────────────────────
    {
        "number": 4,
        "title": "How Does an Order Travel?",
        "challenge": "A customer submits an order — but how does it find the right server, and how does the server know what to do with it?",
        "story": (
            "Jordan is watching over Alex's shoulder as a test order goes through. "
            "'I typed the address and hit enter. What just happened?' "
            "Alex grins. 'Think about how a letter gets delivered. You write an address, the post office looks up which sorting center handles that zip code, "
            "the letter moves through several hubs in a specific format, and finally arrives at the right door. "
            "Every piece of that — the address lookup, the routing rules, the standard envelope format — has a digital equivalent. "
            "What you just did triggered all of it in about two seconds.' "
            "Jordan stares at the screen. 'Two seconds for all that?' "
            "'Two seconds,' Alex says. 'Let me walk you through every step.'"
        ),
        "exploratory": (
            "Imagine you are mailing a package to a friend in another city. "
            "You write the address, the post office looks up the delivery route, the package moves through several sorting hubs, "
            "and your friend receives it. "
            "Before learning any vocabulary, describe what you think happens between a customer typing a website address "
            "and the order arriving at LunchRush's server. "
            "What needs to exist? What translates the human-readable address into a physical location? "
            "What format rules must the package follow to be accepted at each hub?"
        ),
        "activity": (
            "Arrange these six steps in the correct order, then label each one with the vocabulary term that best describes what is happening: "
            "(1) Customer types 'lunchrush.example' in browser, "
            "(2) Browser asks a directory service for the server's numeric address, "
            "(3) Directory returns the numeric address, "
            "(4) Browser sends a formatted request to that address, "
            "(5) Server receives the request and routes it to the order service, "
            "(6) Order service responds with a confirmation. "
            "Think of step 2 and 3 as the post office looking up a zip code. "
            "Think of step 4 as the standard envelope format both sides must follow. "
            "Note: this diagram is simplified — real network paths involve many more hops."
        ),
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
                "analogy_limit": (
                    "The internet isn't one network like a city's road system — it's millions of independently owned and operated "
                    "networks that agree to interconnect. No single company owns or controls it."
                ),
                "essential": 1,
            },
            {
                "word": "IP address",
                "definition": "A numerical label assigned to each device on a network, used to identify and locate it for communication.",
                "plain": "A unique number that identifies a specific computer on the internet — like a street address for data.",
                "lunchrush": "LunchRush's server has an IP address. DNS translates the human-readable domain name into this number so browsers can find it.",
                "analogy_limit": (
                    "Unlike a home street address, IP addresses can change. "
                    "Cloud servers often receive new IP addresses when restarted. "
                    "They are routing labels, not permanent identifiers tied to a physical location."
                ),
                "essential": 1,
            },
            {
                "word": "DNS",
                "definition": "Domain Name System — a distributed directory that translates human-readable domain names into IP addresses.",
                "plain": "The internet's directory service — you give it a name like 'lunchrush.example' and it finds the number (IP address) behind it.",
                "lunchrush": "When a customer types 'lunchrush.example', DNS looks up and returns the IP address of LunchRush's server so the browser knows where to connect.",
                "analogy_limit": (
                    "A phone book is a rough analogy, but DNS is not a single printed book — it is a distributed system "
                    "spread across thousands of servers worldwide. Lookups happen in milliseconds and results are cached "
                    "automatically to avoid repeating the same lookup for every request."
                ),
                "essential": 1,
            },
            {
                "word": "HTTP",
                "definition": "Hypertext Transfer Protocol — the standard format and rules for requests and responses between web clients and servers.",
                "plain": "The agreed language that browsers and web servers use to talk to each other — it defines how to ask for something and how to respond.",
                "lunchrush": "When a customer's browser asks for the LunchRush menu, it sends an HTTP GET request. When submitting an order, it sends an HTTP POST request.",
                "analogy_limit": (
                    "HTTP is like the standard form both sides must fill out to communicate — like using a government form at the DMV. "
                    "But not all services use this form: some use WebSocket for real-time updates, gRPC for high-performance calls, "
                    "or other protocols. HTTP is common for web apps but not universal."
                ),
                "essential": 1,
            },
            {
                "word": "API",
                "definition": "Application Programming Interface — a defined contract that specifies how one piece of software can request services or data from another.",
                "plain": "A set of rules that lets two apps talk to each other in a structured, predictable way.",
                "lunchrush": "LunchRush's frontend uses an API to send order data to the backend — the API defines exactly what format the order must be in and what response to expect.",
                "analogy_limit": (
                    "An API is not the same as the network — the network is the road; the API is the agreed-upon set of "
                    "forms and rules for what you send and what comes back. "
                    "You can have an API over many different transport mechanisms, not just HTTP."
                ),
                "essential": 1,
            },
        ],
    },

    # ── LESSON 5 ──────────────────────────────────────────────────────────────
    {
        "number": 5,
        "title": "What Happens During the Lunch Rush?",
        "challenge": "At noon, far more customers try to order at once than the app was set up to handle. Orders are slow or failing.",
        "story": (
            "It's 12:02 p.m. The dashboard turns red. Average order time has jumped from 2 seconds to 18. "
            "Riley's phone is ringing — customers are complaining. "
            "Jordan looks at Alex. 'What's happening?' "
            "Alex pulls up a graph. 'Imagine a city emergency room on a Monday morning. "
            "They have one triage nurse and suddenly 50 patients arrive at once. "
            "The nurse isn't slow — the system is overwhelmed. "
            "We have one copy of our app trying to serve 200 customers at once. "
            "We need to open more intake windows — and fast.'"
        ),
        "exploratory": (
            "Think about an airport security checkpoint during a holiday weekend. "
            "Normally two lanes are open and the line moves quickly. "
            "On Thanksgiving morning, 500 passengers arrive in an hour. "
            "Before learning any vocabulary, describe: What would the airport do to handle the rush? "
            "What if the problem wasn't the screening lanes but the baggage belt behind them breaking down? "
            "Now apply the same thinking to software: What would you do if your app suddenly had ten times as many users? "
            "What might that still not fix?"
        ),
        "activity": (
            "Use the following scenario to model scaling: "
            "LunchRush normally runs 1 application instance. At noon, 9 orders arrive per second. "
            "Each instance handles 3 orders per second. "
            "Draw a diagram showing: "
            "(1) The bottleneck with 1 instance — like an airport with one open security lane during a holiday rush. "
            "(2) How 3 instances plus a load balancer solves it — like opening 3 lanes with a staff member directing passengers. "
            "(3) One situation where adding more instances still wouldn't help — "
            "for example, if the baggage belt (database) is the real bottleneck, more lanes don't fix it."
        ),
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
                "plain": "Adding more capacity when things get busy, reducing it when they slow down — so you're not paying for capacity you don't need.",
                "lunchrush": "LunchRush scales horizontally during the noon rush by running three copies of the ordering app instead of one.",
                "analogy_limit": (
                    "Opening more airport security lanes is a good image for horizontal scaling, "
                    "but scaling an app doesn't fix every bottleneck. "
                    "If the database, network, or an external service is the constraint, more app instances won't help — "
                    "just as opening more lanes can't fix a broken baggage belt."
                ),
                "essential": 1,
            },
            {
                "word": "Application instance",
                "definition": "One running copy of an application, handling requests independently from other copies.",
                "plain": "One open lane processing requests — if the lane gets overwhelmed, you open another lane next to it.",
                "lunchrush": "LunchRush normally runs one instance but launches two more at noon when orders spike, so each instance handles a manageable share.",
                "analogy_limit": (
                    "Unlike physical checkout lanes at a store, application instances all share the same back-end database. "
                    "If the database can't handle the increased query load, adding more app instances can make the database problem worse."
                ),
                "essential": 1,
            },
            {
                "word": "Load balancing",
                "definition": "Distributing incoming network requests across multiple application instances to prevent any single one from being overwhelmed.",
                "plain": "A traffic director that routes each customer to whichever copy of the app is least busy — so no single instance gets swamped.",
                "lunchrush": "LunchRush's load balancer sits in front of three running instances and distributes incoming orders evenly across all three.",
                "analogy_limit": (
                    "Think of the load balancer as the airport staff member who directs passengers to the shortest line. "
                    "But a load balancer distributes traffic — it does not create capacity. "
                    "You still need enough instances running to handle the total load. Directing people to empty lines doesn't help if all lines are equally full."
                ),
                "essential": 1,
            },
            {
                "word": "Orchestration",
                "definition": "The automated management of containers or services across infrastructure, including starting, stopping, scaling, and recovering from failures.",
                "plain": "A system that automatically starts, stops, and restarts containers so you don't have to do it manually whenever demand changes.",
                "lunchrush": "If LunchRush grows, it might use an orchestration tool to automatically scale the app up at 11:45 a.m. every day before the rush.",
                "analogy_limit": (
                    "Think of an air traffic control system: it coordinates many flights across a shared airport without a human "
                    "manually directing each one. But orchestration manages containers — it is not the same as a load balancer, "
                    "which distributes traffic. They are complementary tools, not interchangeable."
                ),
                "essential": 0,
            },
            {
                "word": "Kubernetes",
                "definition": "An open-source container orchestration platform that automates deployment, scaling, and management of containerized applications across clusters of machines.",
                "plain": "A popular tool for automatically managing and scaling containers — like a smart operations manager for your app infrastructure.",
                "lunchrush": "Kubernetes is one option for orchestrating LunchRush's containers at scale — but it adds complexity and is not required for every application.",
                "analogy_limit": (
                    "Kubernetes is like a full-scale hospital management system: powerful for large institutions, "
                    "but overkill for a small clinic with two exam rooms. "
                    "Not every application needs it — small apps often do fine with simpler approaches. "
                    "The learning curve is steep."
                ),
                "essential": 0,
            },
        ],
    },

    # ── LESSON 6 ──────────────────────────────────────────────────────────────
    {
        "number": 6,
        "title": "Who Can Change the Menu?",
        "challenge": "Staff members need different levels of access to business information, but no one has formally decided who can do what.",
        "story": (
            "A customer calls to complain — they were charged the wrong price. "
            "Someone changed it at 11 p.m. and no one knows who. "
            "Jordan calls a team meeting. 'Does everyone have access to everything?' The room goes quiet. "
            "Sam: 'I only updated the description.' Riley: 'I don't even know how to edit the menu.' "
            "Alex checks the logs. The price change came from an account with full access. "
            "Jordan: 'We need to fix this today.' "
            "Alex nods. 'Think about how a hospital manages access. "
            "A nurse can read a patient's chart but can't prescribe medication — that's a doctor's permission. "
            "A billing clerk can view charges but can't see clinical notes. "
            "Everyone has an ID badge that proves who they are, and a separate set of permissions that determines what doors that badge will open. "
            "We need exactly that for LunchRush.'"
        ),
        "exploratory": (
            "Think about a large building you've been to — a hospital, an office building, a university campus, or a government facility. "
            "Answer two questions before learning any vocabulary: "
            "(1) How does that building confirm who you are before letting you in? "
            "(2) Once it knows who you are, how does it decide which rooms or areas you're allowed to access? "
            "Notice that these are two separate steps — knowing your identity and deciding your permissions are different decisions."
        ),
        "activity": (
            "Using the LunchRush Access Policy below, fill in the permissions table. "
            "Mark each cell R (read), W (write), or — (no access). "
            "Apply least privilege — give each person only what they need to do their job. "
            "Policy: Jordan can view and change anything. "
            "Sam manages menu content only — no financial records or prices. "
            "Riley views orders and updates delivery status — no menu or financial data. "
            "Alex manages technical configuration — no customer payment information during normal operations. "
            "After completing the table, choose two cells where you were unsure and write one sentence explaining your reasoning. "
            "Note: Some cells have defensible alternatives — if your choice differs from the suggested answer, justify it."
        ),
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
                "plain": "Proving you are who you say you are — like showing your ID badge at the hospital entrance before you're allowed past the lobby.",
                "lunchrush": "Before anyone on the LunchRush team can access the system, they must log in with their credentials to prove their identity.",
                "analogy_limit": (
                    "An ID badge can be borrowed or cloned. "
                    "Digital authentication systems add extra layers — like a one-time code sent to your registered phone — "
                    "to make impersonation much harder than borrowing a plastic card. "
                    "The badge analogy captures the concept but understates the security mechanisms involved."
                ),
                "essential": 1,
            },
            {
                "word": "Authorization",
                "definition": "The process of determining what an authenticated user is permitted to access or do within a system.",
                "plain": "After you prove who you are, the system checks what doors your badge will open — not every door is unlocked for everyone.",
                "lunchrush": "Sam is authenticated as a menu manager — but authorization means Sam can edit menu items and cannot access financial records.",
                "analogy_limit": (
                    "Authentication and authorization happen in sequence and are often confused. "
                    "You can be authenticated (identity confirmed) and still be denied access to specific areas. "
                    "A hospital nurse has a valid badge but cannot enter the pharmacy storage room — "
                    "authentication said 'yes, this is a nurse'; authorization said 'nurses don't have pharmacy access'."
                ),
                "essential": 1,
            },
            {
                "word": "IAM",
                "definition": "Identity and Access Management — the policies, tools, and processes used to manage who can access what in a system.",
                "plain": "The system that controls who can log in and what each person or service is allowed to do once they're in.",
                "lunchrush": "LunchRush uses IAM policies to define that Sam can edit menu content, Riley can update delivery status, and Alex can configure the technical systems.",
                "analogy_limit": (
                    "IAM is a category of functionality, not a single product. "
                    "Think of it as the entire access-management program at a university campus: "
                    "the badge system, the door-lock rules, the HR database that links roles to permissions — all of it together. "
                    "The concept applies to both cloud systems and traditional on-premises systems."
                ),
                "essential": 1,
            },
            {
                "word": "Least privilege",
                "definition": "The principle of granting users, systems, or applications only the minimum access necessary to perform their job — nothing more.",
                "plain": "Give people exactly what they need to do their job — and nothing extra. This limits the damage if an account is ever compromised.",
                "lunchrush": "Riley can update delivery status but cannot change the menu or view financial records — that's least privilege applied to a delivery coordinator role.",
                "analogy_limit": (
                    "A hospital's least-privilege model means a billing clerk can see charges but not clinical notes. "
                    "However, least privilege requires deliberate design and regular review — it doesn't happen automatically. "
                    "As roles change (a clerk gets promoted, a nurse changes departments), permissions need to be updated. "
                    "The hospital analogy implies the rules enforce themselves, but they don't without ongoing maintenance."
                ),
                "essential": 1,
            },
            {
                "word": "Shared responsibility",
                "definition": "The division of security obligations between the cloud provider and the customer, varying by service type.",
                "plain": "The cloud company protects the building and the locks; you protect what's inside your office and who has keys to it.",
                "lunchrush": "The cloud provider keeps LunchRush's servers physically secure and the platform patched. LunchRush is responsible for its own IAM policies — including who can change prices.",
                "analogy_limit": (
                    "An apartment building analogy: the landlord secures the front entrance and maintains shared utilities, "
                    "but you are responsible for who has the key to your unit. "
                    "However, what counts as the customer's responsibility varies by service type — "
                    "more managed services shift more infrastructure responsibility to the provider, "
                    "but the customer always owns their data and access controls. "
                    "The analogy understates how much this split changes depending on the service."
                ),
                "essential": 1,
            },
        ],
    },

    # ── LESSON 7 ──────────────────────────────────────────────────────────────
    {
        "number": 7,
        "title": "How Do We Release an Update?",
        "challenge": "LunchRush wants to add a new 'Meal of the Day' feature without taking the site down or breaking orders mid-rush.",
        "story": (
            "Sam has designed the new Meal of the Day feature. The code is written. "
            "But Jordan is nervous: 'What if it breaks the site while customers are ordering? Can we test it first?' "
            "Alex nods. 'Think about how a city government updates a major road. "
            "They don't close the highway on a Monday morning and start digging. "
            "They plan the work, test a small section, run quality checks, get a sign-off from the city engineer, "
            "and then open the new lanes only after everything passes inspection. "
            "That's what a deployment pipeline does for software — "
            "every change moves through a sequence of automatic checks before it goes live. "
            "We don't just push code and hope.'"
        ),
        "exploratory": (
            "Imagine a city is updating its voting registration system before an election. "
            "The team writes new code, tests it on a copy of the system, a supervisor reviews the results, "
            "and only then does the update go live. "
            "Before learning any vocabulary, describe: "
            "What steps would make you confident a software change is safe to release? "
            "What would you want to verify before it goes live? "
            "Who should have approval authority before a change reaches real users?"
        ),
        "activity": (
            "Arrange the following six pipeline stages in the correct order. "
            "Then draw two versions — one for continuous delivery (with a manual approval step) "
            "and one for continuous deployment (fully automated). "
            "Stages: Change code, Build, Run automated tests, Manual approval (use only where applicable), "
            "Deploy to production, Verify the release works. "
            "Think of the Manual approval step as the city engineer's sign-off before new road lanes open. "
            "After drawing both versions, write one sentence explaining the key difference between the two."
        ),
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
                "plain": "An assembly line of automatic checks. Each change must pass every station before it's allowed to go live.",
                "lunchrush": "LunchRush's pipeline automatically builds and tests the Meal of the Day feature before Alex approves it for release.",
                "analogy_limit": (
                    "A road construction quality-check sequence is a useful image, but unlike physical construction, "
                    "a software pipeline runs in minutes, not months. "
                    "It also reduces risk but does not guarantee error-free releases — "
                    "it only catches problems that your tests are designed to detect."
                ),
                "essential": 1,
            },
            {
                "word": "Continuous integration",
                "definition": "The practice of automatically building and testing every code change as soon as it is submitted to the shared codebase.",
                "plain": "Every time a developer saves a change, the system automatically checks whether the code still builds and passes tests.",
                "lunchrush": "When Alex pushes the Meal of the Day code, CI immediately builds it and runs all existing tests to check for regressions.",
                "analogy_limit": (
                    "CI is like the city's automated inspection sensors that check road surface quality after each pour of asphalt. "
                    "But CI only tests what your existing tests cover — "
                    "it cannot catch problems that no test anticipates, "
                    "just as sensors only measure what they are programmed to detect."
                ),
                "essential": 1,
            },
            {
                "word": "Continuous delivery",
                "definition": "A practice where code is always kept in a deployable state, but a human must approve the final release to production.",
                "plain": "The app is always ready to go live — but a person still makes the final decision to open the new lanes.",
                "lunchrush": "LunchRush uses continuous delivery — the pipeline prepares the Meal of the Day release, and Alex reviews and approves it before it goes live.",
                "analogy_limit": (
                    "Continuous delivery is NOT the same as continuous deployment. "
                    "Delivery preserves a human approval gate — like requiring the city engineer's signature. "
                    "Deployment removes that gate entirely and releases automatically once tests pass."
                ),
                "essential": 1,
            },
            {
                "word": "Deployment",
                "definition": "The process of releasing and running a new version of an application in a target environment such as production.",
                "plain": "Putting the new version of the app live so real customers can use it — like officially opening the new road lanes to traffic.",
                "lunchrush": "After Alex approves it, the pipeline deploys the Meal of the Day feature to LunchRush's production server automatically.",
                "analogy_limit": (
                    "Deployment is the opening ceremony, not the construction. "
                    "It is not the same as development — it is the act of releasing code that has already been built, "
                    "tested, and approved."
                ),
                "essential": 1,
            },
            {
                "word": "Automation",
                "definition": "Using software to perform tasks consistently and repeatedly without manual human intervention each time.",
                "plain": "Setting up the system to handle repetitive steps on its own — so humans focus on decisions, not clicking the same buttons every time.",
                "lunchrush": "LunchRush automates its build and test steps so Alex doesn't have to run them manually with every code change.",
                "analogy_limit": (
                    "Automation is reliable for well-defined, predictable steps — like automated toll collection on a highway. "
                    "But it cannot substitute for human judgment when something unexpected happens. "
                    "A toll booth sensor can't decide what to do if a truck is carrying an oversized load."
                ),
                "essential": 1,
            },
        ],
    },

    # ── LESSON 8 ──────────────────────────────────────────────────────────────
    {
        "number": 8,
        "title": "Why Are Orders Slow?",
        "challenge": "Customers are reporting slow orders. The team has data but needs to separate what they can observe from what they still need to investigate.",
        "story": (
            "It's Tuesday at 12:04 p.m. Orders are taking 12 seconds instead of 2. Riley's phone is ringing. "
            "Alex pulls up the dashboard: average order time is 12s, one server shows 91% CPU, "
            "and the logs show three timeout errors in the last 60 seconds. "
            "Jordan: 'So the server is broken?' "
            "Alex: 'Think about an ER doctor looking at a patient with a high fever. "
            "The fever is a real signal — something is wrong. "
            "But the fever alone doesn't tell you whether it's a virus, a bacterial infection, or a reaction to medication. "
            "You need more tests before you treat. "
            "High CPU is the fever. That is not the same as knowing why. Let's look at what the data actually tells us — and what it doesn't.'"
        ),
        "exploratory": (
            "Look at this fictional dashboard data: "
            "Average order time: 12 seconds (normal: 2 seconds). Server CPU: 91%. "
            "Error log: 3 timeout errors in the last 60 seconds. "
            "Before learning any vocabulary, write: "
            "(1) Three things you can say for certain based on this data — stick to what the numbers directly show. "
            "(2) One conclusion you cannot yet confirm — something you suspect but haven't proven. "
            "(3) Two additional pieces of information you would want before deciding what to fix. "
            "Think like a doctor reading a chart: what do you know, what do you suspect, and what test would you order next?"
        ),
        "activity": (
            "Using the fictional dashboard data above, complete this investigation worksheet. "
            "Think of yourself as a doctor reviewing a patient chart — distinguish observations from diagnoses: "
            "(1) List three observations — things the data shows directly, without interpretation. "
            "(2) Write one hypothesis — a possible explanation that fits the data but is not yet proven. "
            "(3) List two more data points you would want to collect before concluding anything. "
            "(4) Write one reason why high CPU alone is not enough to identify the root cause — "
            "just as a high fever alone doesn't tell a doctor which condition to treat."
        ),
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
                "analogy_limit": (
                    "A hospital's patient monitoring system is a good analogy — vital signs are tracked continuously. "
                    "But monitoring shows you what is happening, not why. "
                    "A rising heart rate on a monitor tells a nurse something changed; it doesn't tell them the cause. "
                    "Investigation is still required."
                ),
                "essential": 1,
            },
            {
                "word": "Metric",
                "definition": "A measured numerical value recorded over time, used to track the performance, health, or behavior of a system.",
                "plain": "A number that gets measured repeatedly over time — like order speed, error rate, or CPU usage.",
                "lunchrush": "LunchRush tracks average order time as a key metric — today it's 12 seconds instead of the normal 2, which triggered an investigation.",
                "analogy_limit": (
                    "A single metric is like a single lab result — useful, but rarely the full picture. "
                    "A doctor doesn't diagnose based on one number. "
                    "One metric alone rarely explains a problem — you need to look at multiple signals together."
                ),
                "essential": 1,
            },
            {
                "word": "Log",
                "definition": "A timestamped, sequential record of events that occurred in a system, used for debugging, auditing, and investigation.",
                "plain": "A diary the system keeps — every event gets written down with an exact timestamp so you can trace what happened and when.",
                "lunchrush": "LunchRush's logs show three timeout errors at 12:03 p.m. — a clue, but not proof of the root cause on its own.",
                "analogy_limit": (
                    "Think of logs like a nurse's handwritten shift notes: they record what was observed and when, "
                    "but they don't explain why something happened. "
                    "Interpreting logs still requires judgment and cross-referencing with other signals, "
                    "just as a doctor reads nursing notes alongside test results."
                ),
                "essential": 1,
            },
            {
                "word": "Alert",
                "definition": "An automatic notification triggered when a monitored metric crosses a defined threshold, prompting investigation or action.",
                "plain": "An alarm that fires automatically when something looks wrong — so you don't have to watch the dashboard all day.",
                "lunchrush": "LunchRush sets an alert to notify Alex immediately if average order time exceeds 5 seconds.",
                "analogy_limit": (
                    "An alert is like a fire alarm — it tells you that a threshold was crossed and you need to act, "
                    "but it doesn't tell you where the fire is or what caused it. "
                    "It is the start of an investigation, not the end."
                ),
                "essential": 1,
            },
            {
                "word": "Latency",
                "definition": "The time elapsed between sending a request and receiving a response — a key measure of system responsiveness.",
                "plain": "How long it takes to get an answer — the delay between asking and receiving.",
                "lunchrush": "LunchRush's order latency spiked from 2 seconds to 12 seconds — something in the system is slowing down responses significantly.",
                "analogy_limit": (
                    "High latency is a symptom, not a diagnosis — like a patient reporting that everything feels slow. "
                    "Many things can cause it: network congestion, database slowness, server overload, or slow external services. "
                    "Measuring latency tells you there is a problem; it does not tell you which part of the system to treat."
                ),
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
