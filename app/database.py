from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///./lunchrush.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ── Models ────────────────────────────────────────────────────────────────────

class Lesson(Base):
    __tablename__ = "lessons"
    id          = Column(Integer, primary_key=True, index=True)
    number      = Column(Integer, unique=True)
    title       = Column(String, nullable=False)
    challenge   = Column(Text, nullable=False)
    story       = Column(Text, nullable=False)
    full        = Column(Integer, default=0)   # 1 = fully developed
    terms       = relationship("Term", back_populates="lesson", order_by="Term.id")


class Term(Base):
    __tablename__ = "terms"
    id          = Column(Integer, primary_key=True, index=True)
    lesson_id   = Column(Integer, ForeignKey("lessons.id"))
    word        = Column(String, nullable=False)
    definition  = Column(Text, nullable=False)
    plain       = Column(Text, nullable=False)   # plain-language meaning
    lunchrush   = Column(Text, nullable=False)   # at LunchRush we use it when…
    analogy_limit = Column(Text, nullable=False) # where the analogy breaks
    essential   = Column(Integer, default=1)     # 1=essential, 0=stretch
    lesson      = relationship("Lesson", back_populates="terms")


# ── Seed data ─────────────────────────────────────────────────────────────────

LESSONS = [
    {
        "number": 1,
        "title": "What Does Our Online Business Need?",
        "challenge": "LunchRush wants customers to order online, but Jordan isn't sure what 'the cloud' actually means.",
        "story": "Jordan gathers the team. 'We need a website so people can order from us. But I keep hearing about the cloud — what does that even mean?' Alex smiles. 'Let me show you.'",
        "full": 0,
        "terms": [
            {
                "word": "Cloud computing",
                "definition": "Delivering computing services — storage, processing, and software — over the internet, on demand.",
                "plain": "Renting computer power and storage over the internet instead of buying your own machines.",
                "lunchrush": "Instead of buying a server for the office, LunchRush pays a cloud provider to run its website.",
                "analogy_limit": "Renting a car is a good analogy, but unlike a car you can scale cloud resources up or down in seconds.",
                "essential": 1,
            },
            {
                "word": "Client",
                "definition": "A device or application that requests services from a server.",
                "plain": "The customer's phone or laptop that opens the LunchRush website.",
                "lunchrush": "Every time a customer opens the app, their device is acting as a client.",
                "analogy_limit": "A client isn't always a human — automated systems also act as clients.",
                "essential": 1,
            },
            {
                "word": "Server",
                "definition": "A computer or program that provides services or data in response to client requests.",
                "plain": "The computer somewhere on the internet that holds LunchRush's menu and takes orders.",
                "lunchrush": "LunchRush's ordering application runs on a server that responds when customers click 'Order'.",
                "analogy_limit": "A server doesn't look like a desk computer — it's usually a rack-mounted machine in a data center.",
                "essential": 1,
            },
        ],
    },
    {
        "number": 2,
        "title": "Where Should Our Information Go?",
        "challenge": "LunchRush needs to store menu photos and organized order information.",
        "story": "Sam has 50 menu photos ready to upload. Riley needs to find any order in seconds during the lunch rush. Jordan asks Alex: 'Where do we keep all of this?' Alex answers with a question: 'Do you need to search inside the photos, or just display them?'",
        "full": 1,
        "terms": [
            {
                "word": "Object storage",
                "definition": "A data storage architecture that manages data as self-contained objects, each with its content and metadata.",
                "plain": "A place to store whole files — photos, videos, PDFs — that you drop in and retrieve as-is.",
                "lunchrush": "LunchRush stores menu photos in object storage so customers can load them quickly.",
                "analogy_limit": "Unlike a filing cabinet, object storage serves billions of files to thousands of users simultaneously.",
                "essential": 1,
            },
            {
                "word": "Bucket",
                "definition": "A named container in object storage that holds objects.",
                "plain": "A top-level folder in cloud storage where you group related files.",
                "lunchrush": "LunchRush creates a bucket called 'lunchrush-images' to hold all menu photos.",
                "analogy_limit": "Unlike folders, buckets usually can't be nested inside other buckets in most systems.",
                "essential": 1,
            },
            {
                "word": "Database",
                "definition": "An organized system for storing, managing, and retrieving structured information efficiently.",
                "plain": "A smart spreadsheet that lets you search, filter, sort, and update specific pieces of information fast.",
                "lunchrush": "LunchRush stores every order — customer name, items, time, address — in a database so Riley can search them.",
                "analogy_limit": "A spreadsheet is a rough analogy — real databases handle millions of rows and multiple users simultaneously.",
                "essential": 1,
            },
            {
                "word": "Object",
                "definition": "A unit of data in object storage, consisting of the file content plus metadata describing it.",
                "plain": "One file stored in the cloud, bundled with info about itself like its name and creation date.",
                "lunchrush": "Each menu photo is an object stored in LunchRush's image bucket.",
                "analogy_limit": "Objects aren't editable in place — you replace the whole object, unlike editing a row in a database.",
                "essential": 1,
            },
            {
                "word": "Storage",
                "definition": "Cloud services that hold data persistently — the data remains saved even when nothing is actively processing it.",
                "plain": "The place your information lives when it's not actively being used.",
                "lunchrush": "LunchRush needs storage for photos, order records, and business documents.",
                "analogy_limit": "Storage isn't the same as memory (RAM) — storage persists; RAM is temporary.",
                "essential": 1,
            },
        ],
    },
    {
        "number": 3,
        "title": "How Will Our Application Run?",
        "challenge": "LunchRush needs to decide how to run its ordering application in the cloud.",
        "story": "Alex places three index cards on the table. 'We have three options for how to run the app. Each one is a different trade-off between control and convenience.' Jordan leans in. 'Show me.'",
        "full": 1,
        "terms": [
            {
                "word": "Virtual machine",
                "definition": "A software-based simulation of a physical computer that runs its own operating system.",
                "plain": "A pretend computer running inside a real computer — it has its own OS and you manage everything on it.",
                "lunchrush": "LunchRush could run its app on a VM if it needs full control over the operating system.",
                "analogy_limit": "Unlike a physical computer, a VM can be created, copied, or deleted in seconds.",
                "essential": 1,
            },
            {
                "word": "Container",
                "definition": "A packaged unit containing an application and all its dependencies, sharing the host operating system.",
                "plain": "A box that holds your app and everything it needs to run, so it works the same anywhere.",
                "lunchrush": "LunchRush could package its ordering app as a container so it runs the same on any cloud provider.",
                "analogy_limit": "Unlike a shipping container, software containers share the host OS kernel — they're not fully isolated.",
                "essential": 1,
            },
            {
                "word": "Container image",
                "definition": "A read-only blueprint or template used to create a container, built from a Dockerfile.",
                "plain": "The recipe used to create a container — like a snapshot of everything the app needs.",
                "lunchrush": "LunchRush's developer builds a container image once; it can be used to launch many identical containers.",
                "analogy_limit": "An image is static — it's not running. A container is what you get when you run the image.",
                "essential": 1,
            },
            {
                "word": "Serverless",
                "definition": "A cloud model where the provider manages all server infrastructure; you provide code and pay per execution.",
                "plain": "You write the function, the cloud runs it when needed — you never touch a server.",
                "lunchrush": "LunchRush could use serverless to handle order notifications — the function only runs when an order arrives.",
                "analogy_limit": "Serverless doesn't mean no servers exist — it means YOU don't manage them. Servers still run your code.",
                "essential": 1,
            },
            {
                "word": "Operating system",
                "definition": "Software that manages a computer's hardware and provides services for applications to run.",
                "plain": "The foundation software (like Linux or Windows) that everything else runs on top of.",
                "lunchrush": "With a VM, LunchRush is responsible for keeping the operating system updated and secure.",
                "analogy_limit": "Containers don't each have their own OS — they share the host OS, which is a key difference from VMs.",
                "essential": 1,
            },
        ],
    },
    {
        "number": 4,
        "title": "How Does an Order Travel?",
        "challenge": "A customer submits an order and the correct service must receive it.",
        "story": "A customer types 'lunchrush.example' into their browser and clicks Order. Jordan watches over Alex's shoulder. 'What just happened?' Alex grins. 'A lot, actually.'",
        "full": 0,
        "terms": [
            {
                "word": "DNS",
                "definition": "Domain Name System — a directory that translates human-readable domain names into IP addresses.",
                "plain": "The internet's phone book — it looks up the address for a website name.",
                "lunchrush": "When a customer types 'lunchrush.example', DNS finds the actual server address behind that name.",
                "analogy_limit": "Unlike a phone book, DNS lookups happen in milliseconds and are distributed globally.",
                "essential": 1,
            },
            {
                "word": "HTTP",
                "definition": "Hypertext Transfer Protocol — the agreed format for requests and responses between clients and servers on the web.",
                "plain": "The language browsers and servers use to talk to each other.",
                "lunchrush": "When a customer's browser asks for the LunchRush menu, it sends an HTTP request.",
                "analogy_limit": "Not all APIs use HTTP — some use other protocols like WebSocket or gRPC.",
                "essential": 1,
            },
            {
                "word": "API",
                "definition": "Application Programming Interface — a defined way for one software service to request something from another.",
                "plain": "A set of rules that lets two apps talk to each other in a structured way.",
                "lunchrush": "The LunchRush app uses an API to send order data from the frontend to the backend.",
                "analogy_limit": "An API is not the same as the network — the network carries the data; the API defines the structure of the conversation.",
                "essential": 1,
            },
            {
                "word": "IP address",
                "definition": "A numerical label assigned to each device connected to a network, used to identify and locate it.",
                "plain": "A unique number that identifies a specific computer on the internet.",
                "lunchrush": "LunchRush's server has an IP address — DNS translates the domain name to this number.",
                "analogy_limit": "IP addresses can change — they're not permanently tied to a physical machine.",
                "essential": 1,
            },
            {
                "word": "Network",
                "definition": "A system of connected computers and devices that can communicate and share data with each other.",
                "plain": "The infrastructure of cables, routers, and wireless signals that lets computers talk to each other.",
                "lunchrush": "Every time a customer places an order, the data travels across the network to reach LunchRush's server.",
                "analogy_limit": "The internet isn't one network — it's millions of interconnected networks.",
                "essential": 1,
            },
        ],
    },
    {
        "number": 5,
        "title": "What Happens During the Lunch Rush?",
        "challenge": "More customers begin ordering at once and the app starts slowing down.",
        "story": "It's noon. Orders are pouring in. The app is crawling. Riley shouts across the room: 'People are calling to complain!' Alex pulls up a dashboard. 'We need more capacity — and we need it now.'",
        "full": 0,
        "terms": [
            {
                "word": "Scaling",
                "definition": "Increasing or decreasing computing resources to match changes in demand.",
                "plain": "Adding more horsepower when things get busy, reducing it when they slow down.",
                "lunchrush": "LunchRush scales up during the noon rush by running more copies of the ordering app.",
                "analogy_limit": "Scaling up doesn't fix every problem — if the database is the bottleneck, more app instances won't help.",
                "essential": 1,
            },
            {
                "word": "Load balancing",
                "definition": "Distributing incoming network requests across multiple application instances to prevent any one from being overwhelmed.",
                "plain": "A traffic director that sends each customer to whichever copy of the app is least busy.",
                "lunchrush": "LunchRush's load balancer routes incoming orders across three running instances of the app.",
                "analogy_limit": "A load balancer distributes requests but doesn't create capacity — you still need enough instances running.",
                "essential": 1,
            },
            {
                "word": "Application instance",
                "definition": "One running copy of an application.",
                "plain": "Think of it as one open restaurant — if it gets too busy, you open another one next door.",
                "lunchrush": "LunchRush normally runs one instance but spins up two more at noon when orders spike.",
                "analogy_limit": "Instances share the same database — if the database can't handle the load, more instances don't solve it.",
                "essential": 1,
            },
            {
                "word": "Orchestration",
                "definition": "Automated management of containers and services across multiple servers, including scaling and self-healing.",
                "plain": "A system that automatically starts, stops, and restarts containers so you don't have to do it manually.",
                "lunchrush": "If LunchRush grows, it might use an orchestration tool to automatically scale the app during peak hours.",
                "analogy_limit": "Orchestration manages containers — it's not the same as a load balancer, which distributes traffic.",
                "essential": 0,
            },
            {
                "word": "Kubernetes",
                "definition": "An open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.",
                "plain": "A popular tool that automatically manages and scales containers across many servers.",
                "lunchrush": "Kubernetes is one option for orchestrating LunchRush's containers — but it's not required for every application.",
                "analogy_limit": "Kubernetes is powerful but complex — not every small application needs it.",
                "essential": 0,
            },
        ],
    },
    {
        "number": 6,
        "title": "Who Can Change the Menu?",
        "challenge": "Staff members need different levels of access to business information.",
        "story": "A customer was charged the wrong price. Someone changed it at 11 p.m. — no one knows who. Jordan calls a team meeting. 'Does everyone on the team have access to everything?' The room goes quiet.",
        "full": 1,
        "terms": [
            {
                "word": "Authentication",
                "definition": "The process of verifying that someone is who they claim to be, using credentials like passwords or tokens.",
                "plain": "Proving you are who you say you are — like showing your ID at the door.",
                "lunchrush": "Before anyone can change the menu, they must log in to prove their identity.",
                "analogy_limit": "An ID card can be forged — digital systems use additional signals like one-time codes to make impersonation harder.",
                "essential": 1,
            },
            {
                "word": "Authorization",
                "definition": "The process of determining what an authenticated user is permitted to do or access.",
                "plain": "After you prove who you are, the system decides what you're allowed to do.",
                "lunchrush": "Sam is authenticated as a menu manager — but authorization means Sam can't access financial records.",
                "analogy_limit": "Authentication and authorization are often confused. You can be authenticated and still be denied access.",
                "essential": 1,
            },
            {
                "word": "IAM",
                "definition": "Identity and Access Management — the set of tools and policies used to manage who can access what in a system.",
                "plain": "The system that controls who can log in and what each person is allowed to do once they're in.",
                "lunchrush": "LunchRush uses IAM policies to define that Sam can edit menus but cannot change prices.",
                "analogy_limit": "IAM is a category of tools, not a single product. The concept applies beyond cloud systems too.",
                "essential": 1,
            },
            {
                "word": "Least privilege",
                "definition": "The principle of giving a user, system, or application only the minimum access it needs to perform its job.",
                "plain": "Give people exactly what they need — nothing more, nothing less.",
                "lunchrush": "Riley can update delivery status but cannot change the menu or see financial records — that's least privilege.",
                "analogy_limit": "Least privilege requires deliberate design and regular review — it doesn't happen automatically.",
                "essential": 1,
            },
            {
                "word": "Shared responsibility",
                "definition": "The division of security obligations between the cloud provider and the customer.",
                "plain": "The cloud company protects the infrastructure; you protect your data, accounts, and access policies.",
                "lunchrush": "The cloud provider keeps the servers secure. LunchRush is responsible for its own access rules — like who can change prices.",
                "analogy_limit": "What counts as the customer's responsibility varies by service type — more managed services shift more responsibility to the provider.",
                "essential": 1,
            },
        ],
    },
    {
        "number": 7,
        "title": "How Do We Release an Update?",
        "challenge": "LunchRush wants to add a new feature without breaking the live site.",
        "story": "Sam has designed a 'Meal of the Day' feature. The dev team is ready. But Jordan is nervous: 'What if it breaks the site while customers are ordering?' Alex says: 'That's exactly why we have a pipeline.'",
        "full": 0,
        "terms": [
            {
                "word": "Pipeline",
                "definition": "An automated sequence of steps that moves a code change from development to production.",
                "plain": "An assembly line for software — each change goes through build, test, and deploy steps automatically.",
                "lunchrush": "LunchRush's pipeline automatically tests the Meal of the Day feature before it goes live.",
                "analogy_limit": "A pipeline reduces risk but doesn't guarantee error-free releases — bugs can still slip through.",
                "essential": 1,
            },
            {
                "word": "Continuous integration",
                "definition": "The practice of automatically building and testing code every time a change is submitted.",
                "plain": "Every time a developer saves a change, the system automatically checks whether it still works.",
                "lunchrush": "When Alex pushes a code change, CI immediately builds and tests it.",
                "analogy_limit": "CI only tests what your tests cover — it can't catch problems your tests don't anticipate.",
                "essential": 1,
            },
            {
                "word": "Continuous delivery",
                "definition": "A practice where code is always in a deployable state; a human approves the final release to production.",
                "plain": "The app is always ready to go live — but a person still presses the final button.",
                "lunchrush": "LunchRush uses continuous delivery — Alex approves the Meal of the Day release before it goes live.",
                "analogy_limit": "Continuous delivery is not the same as continuous deployment — delivery still requires a human approval step.",
                "essential": 1,
            },
            {
                "word": "Deployment",
                "definition": "The process of releasing and running a new version of an application in a target environment.",
                "plain": "Putting the new version of the app live so customers can use it.",
                "lunchrush": "After approval, the pipeline deploys the Meal of the Day feature to LunchRush's production server.",
                "analogy_limit": "Deployment is not the same as development — it's the act of releasing, not building.",
                "essential": 1,
            },
            {
                "word": "Automation",
                "definition": "Using software to perform tasks that would otherwise require manual human action, consistently and repeatedly.",
                "plain": "Setting up the system to do repetitive steps on its own so humans don't have to.",
                "lunchrush": "LunchRush automates its build and test steps so Alex doesn't have to run them manually every time.",
                "analogy_limit": "Automation is reliable for predictable steps but can't substitute for human judgment on novel problems.",
                "essential": 1,
            },
        ],
    },
    {
        "number": 8,
        "title": "Why Are Orders Slow?",
        "challenge": "Customers are reporting slow or failed orders and the team needs to investigate.",
        "story": "It's Tuesday at noon. Orders are taking 12 seconds instead of 2. Customers are complaining. Riley pulls up the dashboard and sees a wall of numbers. 'What does all this mean?' Alex says: 'Let's look at what we know — and what we don't.'",
        "full": 0,
        "terms": [
            {
                "word": "Monitoring",
                "definition": "The continuous collection of signals — metrics, logs, and alerts — to track the health and performance of a system.",
                "plain": "Watching the system continuously so you notice problems as soon as they happen.",
                "lunchrush": "LunchRush's monitoring dashboard shows order times, server load, and error rates in real time.",
                "analogy_limit": "Monitoring shows you what's happening but not always why — investigation is still required.",
                "essential": 1,
            },
            {
                "word": "Metric",
                "definition": "A measured number recorded over time, used to track the performance or health of a system.",
                "plain": "A number that gets measured repeatedly over time — like order speed or error rate.",
                "lunchrush": "LunchRush tracks average order time as a metric — today it's 12 seconds instead of the normal 2.",
                "analogy_limit": "One metric alone doesn't explain a problem — you need multiple signals to understand what's happening.",
                "essential": 1,
            },
            {
                "word": "Log",
                "definition": "A timestamped record of events that occurred in a system, used for debugging and auditing.",
                "plain": "A diary the system keeps — every event gets written down with a timestamp.",
                "lunchrush": "LunchRush's logs show three timeout errors at 12:03 p.m. — a clue, but not proof of the root cause.",
                "analogy_limit": "Logs record what happened, not why — interpreting them still requires judgment.",
                "essential": 1,
            },
            {
                "word": "Alert",
                "definition": "An automatic notification triggered when a metric crosses a defined threshold.",
                "plain": "An alarm that goes off automatically when something looks wrong.",
                "lunchrush": "LunchRush sets an alert to notify Alex if average order time exceeds 5 seconds.",
                "analogy_limit": "An alert tells you a threshold was crossed — it doesn't diagnose the cause.",
                "essential": 1,
            },
            {
                "word": "Latency",
                "definition": "The time between sending a request and receiving a response.",
                "plain": "How long it takes to get an answer — the delay between asking and receiving.",
                "lunchrush": "LunchRush's latency spiked from 2 seconds to 12 seconds — something in the system is slowing down responses.",
                "analogy_limit": "High latency has many possible causes — network, database, server load, or external services. It's a symptom, not a diagnosis.",
                "essential": 1,
            },
        ],
    },
]


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
