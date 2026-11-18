# Curriculum Map
## Cloud Before Code — Eight-Lesson Overview

> **How to read this table:** Each row represents one lesson. "Essential terms" are vocabulary every learner is expected to know by the end of the lesson. "Stretch terms" are optional extensions for learners who want to go deeper. "Learner artifact" is the tangible product a learner produces. All times are estimates for the three fully developed lessons; outlines may vary in delivery.

---

| Lesson | Business Problem | Learning Objective | Essential Terms | Stretch Terms | Activity | Learner Artifact | Est. Time |
|--------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------|-----------|
| **1** | LunchRush wants customers to order online. | Describe what happens when a customer uses an online application and identify where the cloud fits in. | Cloud computing, Client, Server | Compute, Application, Data center | Draw a simple map of a customer, an application, and the information they exchange. | Annotated diagram | 15 min |
| **2** ★ | LunchRush needs to store menu photos and organized order information. | Distinguish object storage from a database; sort fictional business data into storage categories; justify each choice. | Storage, Object storage, Object, Bucket, Database | Structured data, Unstructured data, Query | Sort fictional business-data cards into storage categories and write a justification for each. | Completed sort worksheet + written justifications | 20–25 min |
| **3** ★ | LunchRush needs a way to run its ordering application. | Describe virtual machines, containers, and serverless compute; compare options using decision cards; state one trade-off for each. | Virtual machine (VM), Operating system (OS), Container, Container image, Serverless | Orchestration, Infrastructure as a Service (IaaS), Platform as a Service (PaaS) | Compare simplified deployment options using decision cards; select an option and defend the choice. | Completed decision-card worksheet + written defense | 20–25 min |
| **4** | A customer submits an order and the correct service must receive it. | Trace an order request through a simplified network diagram; identify the roles of DNS, HTTP, and APIs. | Network, IP address, Domain Name System (DNS), Hypertext Transfer Protocol (HTTP), Application programming interface (API) | REST, Endpoint, Packet | Arrange simplified request-and-response journey cards in the correct order. | Ordered journey diagram with labels | 15–20 min |
| **5** | More customers begin ordering at once during peak hours. | Explain what scaling means; describe how load balancing distributes requests; identify at least one limit of adding instances. | Scaling, Application instance, Load balancing | Orchestration, Kubernetes, Horizontal vs. vertical scaling | Use cards to model adding application instances and distributing requests across them. | Completed scaling model + reflection note | 15–20 min |
| **6** ★ | Staff members need different levels of access to business information. | Distinguish authentication from authorization; apply least-privilege principles to create a permissions table for four characters. | Authentication, Authorization, Identity and access management (IAM), Least privilege, Shared responsibility | Multi-factor authentication (MFA), Role-based access control (RBAC) | Create a permissions table that assigns appropriate access levels to Jordan, Sam, Riley, and Alex. | Completed permissions table + written justifications | 20–25 min |
| **7** | LunchRush introduces a new menu feature and needs to release it safely. | Describe a basic CI/CD pipeline; distinguish continuous delivery from continuous deployment; arrange pipeline stages in order. | Deployment, Automation, Pipeline, Continuous integration (CI), Continuous delivery | Continuous deployment, Rollback, Environment | Arrange change, build, test, approval (where applicable), deployment, and verification cards in a pipeline. | Ordered pipeline diagram + one-sentence explanation | 15–20 min |
| **8** | Customers report slow ordering. | Identify what logs, metrics, and alerts provide; distinguish observations from conclusions; list additional evidence needed. | Monitoring, Metric, Log, Alert, Latency | Tracing, Observability, Mean time to resolution (MTTR) | Review a fictional dashboard and short log excerpt; answer guided investigation questions. | Completed investigation worksheet | 15–20 min |

★ = Fully developed lesson pack

---

## Notes on Scope and Accuracy

- **Lesson 2:** The sorting activity reflects common simplified distinctions. Object storage and databases have overlapping capabilities in production systems; the activity states that the learner is making a simplified choice for a small business scenario.
- **Lesson 3:** Decision cards present trade-offs, not a single "correct" answer. VMs, containers, and serverless are not mutually exclusive layers; combinations are common.
- **Lesson 5:** Adding application instances addresses some bottlenecks (compute) but not all (database, network, external services). This limitation is stated in the lesson.
- **Lesson 6:** The permissions table uses a stated business policy. Justified alternatives from learners are acceptable when the scenario permits.
- **Lesson 7:** Continuous delivery requires a manual approval step before production; continuous deployment automates the final release. The pipeline cards reflect this distinction.
- **Lesson 8:** No single metric is treated as proof of a root cause. The activity asks learners to separate observations from conclusions and identify what additional evidence is needed.

---

## Jargon-Journal Terms by Lesson

| Lesson | Terms Assigned to Jargon Journal |
|--------|-----------------------------------|
| 1 | Cloud computing, Server |
| **2** | Object storage, Database |
| **3** | Virtual machine, Container, Serverless |
| 4 | API, DNS |
| 5 | Scaling, Load balancing |
| **6** | Authentication, Authorization, Least privilege |
| 7 | Pipeline, Continuous integration |
| 8 | Metric, Log |

*Lessons 2, 3, and 6 jargon-journal prompts are included in the learner workbook.*

---

*[DRAFT — verify term definitions against official documentation before classroom use.]*
