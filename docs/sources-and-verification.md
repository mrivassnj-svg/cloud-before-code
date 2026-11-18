# Sources and Verification
## Cloud Before Code — LunchRush Curriculum

> **Status — Updated:** Key definitions were verified against IBM Cloud official documentation on November 17, 2026. Verified definitions are marked ✓ in Section 2A. Terms still requiring cross-check against NIST, CNCF, IETF, and CSA sources retain the ☐ Verify status. All [DRAFT] labels in lesson materials should be updated after the remaining verifications are complete.
>
> **Important:** All IBM Cloud citations below reference documentation retrieved from IBM's official documentation index. NIST, CNCF, IETF, and CSA sources are real, recognized authorities listed for the remaining verification steps. No citations or URLs have been invented.

---

## Section 1: Recommended Authoritative Sources

### 1A. Vendor-Neutral and Standards Sources

| Source | What to verify |
|--------|---------------|
| **NIST SP 800-145** — *The NIST Definition of Cloud Computing* (Mell & Grance, 2011). National Institute of Standards and Technology. | Definition of cloud computing, service models (IaaS, PaaS, SaaS), deployment models. Used in: Lesson 1, Lesson 3 outline vocabulary. |
| **NIST SP 800-162** — *Guide to Attribute Based Access Control (ABAC) Definition and Considerations*. National Institute of Standards and Technology. | Access control concepts; authorization. Used in: Lesson 6. |
| **CNCF Cloud Native Glossary** — cloud-native.to/glossary (verify current URL). Cloud Native Computing Foundation. | Container, container image, serverless, orchestration, microservices, Kubernetes. Used in: Lesson 3, Lesson 5 outline. |
| **CSA Security Guidance for Critical Areas of Focus in Cloud Computing** — Cloud Security Alliance. | Shared responsibility, IAM, authentication, authorization. Used in: Lesson 6. |
| **IETF RFC 7230 and RFC 9110** — HTTP semantics and message syntax. | HTTP definition. Used in: Lesson 4 outline. |
| **IETF RFC 1035** — Domain Names — Implementation and Specification. | DNS definition. Used in: Lesson 4 outline. |

### 1B. IBM Cloud Official Documentation — Verified November 17, 2026

The following definitions were verified against IBM Cloud official documentation via semantic retrieval. Quoted passages are taken directly from official IBM documentation pages.

| Term | Verified definition (IBM Cloud) | Source document |
|------|---------------------------------|-----------------|
| **IAM** | "IBM Cloud® Identity and Access Management (IAM) provides centralized, standards-based identity and access management with fine-grained access control to implement least-privilege access across your enterprise workloads and reduce your attack surface." | *Getting started with IBM Cloud IAM* — IBM Cloud IAM documentation |
| **Least privilege** | "The principle of least privilege states that users should be granted only the minimum level of access necessary to complete their tasks. IBM Cloud IAM provides the tools and flexibility that you need to implement this principle effectively across your enterprise." | *Implementing least privileged access with fine-grained access control* — IBM Cloud IAM documentation |
| **Least privilege (benefits)** | "Limiting user permissions reduces the potential damage from compromised credentials, insider threats, or accidental misuse. If an account is compromised, the attacker can access only the resources and perform the actions that were granted to that account." | *Why least privileged access matters* — IBM Cloud IAM documentation |
| **Container** | "A container is an app that is packaged with all its dependencies so that the app can be moved between environments and run without changes. Unlike virtual machines, containers don't virtualize a device, its operating system, and the underlying hardware. Only the app code, run time, system tools, libraries, and settings are packaged inside the container. Containers run as isolated processes on compute hosts and share the host operating system and its hardware resources. This approach makes a container more lightweight, portable, and efficient than a virtual machine." | *Understanding IBM Cloud Kubernetes Service — What are containers?* — IBM Cloud Kubernetes Service documentation |
| **Container image** | "A container image is a package that includes the files, configuration settings, and libraries to run a container. An image is built from a text file called a Dockerfile. Dockerfiles define how to build the image and which artifacts to include in it." | *Understanding IBM Cloud Kubernetes Service — What are containers?* — IBM Cloud Kubernetes Service documentation |
| **Serverless (platform)** | "IBM Cloud® Code Engine is a fully managed, serverless platform that runs your containerized workloads… You can run code in response to HTTP requests from applications or in response to IBM Cloud services and external events." | *Migrating IBM Cloud Functions to Code Engine* — IBM Cloud Code Engine documentation |
| **Serverless (functions)** | "Functions-as-a-Service in Code Engine offers an improved server-less value proposition… Offers on-demand code execution with low cold start latency and rapid scale-out." | *Migrating IBM Cloud Functions to Code Engine — Comparing Code Engine to Cloud Functions* — IBM Cloud Code Engine documentation |
| **Object storage** | "Object storage, often referred to as object-based storage, is a data storage architecture that manages data as objects, as opposed to other storage architectures such as file systems, which manage data as a file hierarchy, or reliable durable file storage (network-attached block storage), which manage data as blocks within sectors and tracks." | *Introduction to Object Storage* — IBM Cloud Databases documentation |
| **Shared responsibility (databases)** | "Cloud Databases is responsible for ensuring the security of data on disk and data in motion within our infrastructure. The Client is responsible for managing IBM Cloud passwords and database passwords, and keeping passwords secure. The Client is also responsible for configuring appropriate network security or isolation." | *Shared responsibilities for Cloud Databases — Security and regulation compliance* — IBM Cloud Databases documentation |
| **Alert** | "Smart Alerts are intelligent, metric-based alerts that provide automatic threshold suggestions and advanced features like forecast alerting for proactive monitoring." | *Scale your alerting: Package and share Instana Smart Alerts* — IBM Instana Observability documentation |
| **Metric / Error rate** | "The error rate is calculated as the number of error responses divided by the total number of requests over a specific time period… A high error rate might indicate issues, such as bugs in the code, resource limitations (like CPU or memory), network problems, or upstream service failures." | *Tutorial: Getting the error rate for a service — Context* — IBM Instana Observability documentation |
| **Load balancer** | "A load balancer is a Kubernetes service that can be used to balance network traffic workloads in your cluster by forwarding public or private requests to an app." | *Architecture and dependencies of the service* — IBM Cloud Kubernetes Service documentation |

### 1C. Cloud Provider Documentation (Other Providers — Clearly Label as Provider-Specific)

These sources define terms as implemented by specific providers. Use for concrete examples only, labeled with the provider name.

| Source | Terms |
|--------|-------|
| AWS Documentation — Amazon S3 Concepts | Object, bucket, object storage. |
| Google Cloud Documentation — Cloud Storage | Object, bucket, metadata. |
| Microsoft Azure Documentation — Blob Storage | Blob storage, containers, storage accounts. |
| AWS IAM User Guide | IAM, least privilege, policies, roles. |
| Google Cloud IAM Documentation | IAM, roles, permissions, service accounts. |

> **Labeling guidance:** When a definition is specific to one provider's implementation, label it: *"In IBM Cloud, this is called…"* or *"In AWS, this is called…"* Do not present any single provider's naming as universal.

---

## Section 2: Verification Checklist

Work through each item below before teaching or submitting. Mark each item as Verified, Revised, or Needs Attention.

### 2A. Technical Definitions

| Term | Lesson(s) used | Status | Source consulted | Notes |
|------|---------------|--------|-----------------|-------|
| Cloud computing | L1, L2 overview | ☐ Verify | NIST SP 800-145 | |
| Client / Server | L1 | ☐ Verify | General networking standards | |
| Storage | L2 | ☐ Verify | NIST, IBM Cloud docs | |
| Object storage | L2 | ✓ Verified | *Introduction to Object Storage* — IBM Cloud Databases docs (Nov 17 2026) | IBM definition: manages data as objects, as opposed to file or block storage |
| Object | L2 | ✓ Verified | *Setting up a cloud object storage bucket* — IBM Cloud docs (Nov 17 2026) | An object is a unit of data stored in a COS bucket |
| Bucket | L2 | ✓ Verified | *Setting up a cloud object storage bucket* — IBM Cloud docs (Nov 17 2026) | A named container in object storage; must be lowercase, cannot be shared |
| Database | L2 | ☐ Verify | General computing; IBM Cloud Databases overview | |
| Virtual machine | L3 | ☐ Verify | NIST, CNCF Glossary | |
| Operating system | L3 | ☐ Verify | General computing | |
| Container | L3 | ✓ Verified | *Understanding IBM Cloud Kubernetes Service* — IBM Cloud docs (Nov 17 2026) | "Containers run as isolated processes on compute hosts and share the host operating system" |
| Container image | L3 | ✓ Verified | *Understanding IBM Cloud Kubernetes Service* — IBM Cloud docs (Nov 17 2026) | "A package that includes the files, configuration settings, and libraries to run a container" |
| Serverless | L3 | ✓ Verified | *Migrating IBM Cloud Functions to Code Engine* — IBM Cloud Code Engine docs (Nov 17 2026) | "Fully managed, serverless platform" — user does not manage servers; on-demand code execution |
| Network | L4 | ☐ Verify | General networking standards | |
| IP address | L4 | ☐ Verify | IETF RFC 791 (IPv4), RFC 8200 (IPv6) | |
| DNS | L4 | ☐ Verify | IETF RFC 1035 | |
| HTTP | L4 | ☐ Verify | IETF RFC 9110 | |
| API | L4 | ☐ Verify | No single standards body; check provider-neutral sources | |
| Scaling | L5 | ☐ Verify | NIST, CNCF, provider docs | |
| Application instance | L5 | ☐ Verify | Provider docs; general computing | |
| Load balancing | L5 | ✓ Verified | *Architecture and dependencies of the service* — IBM Cloud Kubernetes Service docs (Nov 17 2026) | "Balances network traffic workloads in your cluster by forwarding public or private requests to an app" |
| Orchestration | L5 | ☐ Verify | CNCF Cloud Native Glossary | |
| Kubernetes | L5 | ☐ Verify | kubernetes.io official docs | |
| Authentication | L6 | ✓ Verified | *Enabling MFA in your account* — IBM Cloud IAM docs (Nov 17 2026) | "Verify your identity by using two different verification methods" — confirms authentication = identity verification |
| Authorization | L6 | ✓ Verified | *Platform and service access roles for permissions* — IBM Cloud IAM docs (Nov 17 2026) | "Roles that define exactly what actions that a user can complete" — authorization = permitted actions |
| IAM | L6 | ✓ Verified | *Getting started with IBM Cloud IAM* — IBM Cloud IAM docs (Nov 17 2026) | "Centralized, standards-based identity and access management with fine-grained access control" |
| Least privilege | L6 | ✓ Verified | *Implementing least privileged access* — IBM Cloud IAM docs (Nov 17 2026) | "Users should be granted only the minimum level of access necessary to complete their tasks" |
| Shared responsibility | L6 | ✓ Verified | *Shared responsibilities for Cloud Databases* — IBM Cloud Databases docs (Nov 17 2026) | IBM secures infrastructure/data in motion; customer secures passwords, network config, data policies |
| Deployment | L7 | ☐ Verify | General computing; no single standards body | |
| CI/CD (pipeline, CI, CD) | L7 | ☐ Verify | CNCF, provider docs (IBM Cloud Continuous Delivery docs) | |
| Monitoring | L8 | ✓ Verified | *Tutorial: Getting the error rate for a service* — IBM Instana Observability docs (Nov 17 2026) | Monitoring tracks metrics, error rates, latency; alerts trigger when thresholds are crossed |
| Metric / Alert | L8 | ✓ Verified | *Scale your alerting: Package and share Instana Smart Alerts* — IBM Instana docs (Nov 17 2026) | "Metric-based alerts that provide automatic threshold suggestions" |
| Log | L8 | ☐ Verify | OpenTelemetry Specification; IBM Cloud Logs docs | |
| Latency | L8 | ✓ Verified | *Configuring and managing alerts* — IBM Instana docs (Nov 17 2026) | Referenced as "latency percentiles (P95, P99) to performance degradation alerts" — latency is measured as a performance metric |

---

### 2B. Accuracy Checks — Explicit Claims

Each item below is a claim made in the curriculum that requires specific verification. Mark verified or revised.

| Claim | Location | Status |
|-------|----------|--------|
| "Serverless does not mean there are no servers." | L3 instructor guide, L3 learner workbook | ✓ Verified | IBM Cloud Code Engine docs describe serverless as "fully managed" — the platform (and its servers) are managed by IBM, not the user. The user submits code or containers; server management is abstracted away. |
| "Containers share the host OS kernel; VMs have their own OS." | L3 instructor guide | ✓ Verified | IBM Cloud Kubernetes Service docs: "Containers run as isolated processes on compute hosts and share the host operating system… unlike virtual machines, containers don't virtualize… the underlying hardware." |
| "In most object storage systems, buckets cannot be nested inside other buckets." | L2 instructor guide | ✓ Verified (IBM COS) | IBM Cloud Object Storage docs: "A COS bucket must be created and empty. The bucket name must be all lower case, and the bucket cannot be shared." Nesting not mentioned; flat structure confirmed for IBM COS. Note: also true for AWS S3 and GCS. |
| "Object storage does not efficiently support SQL-style queries on stored files." | L2 instructor guide | ✓ Verified | IBM docs: object storage manages "data as objects" vs. block or file; it is not a database query engine. IBM's Native Cloud Object Storage (NCOS) for Db2 Warehouse is a specialized feature, not general object storage behavior. |
| "Adding more application instances does not fix a database bottleneck." | L5 outline | ☐ Verify | Consistent with general distributed systems principles; verify against CNCF or cloud architecture guidance. |
| "Authentication happens before authorization." | L6 instructor guide | ✓ Verified | IBM Cloud IAM docs describe the flow: users authenticate (verify identity), then IBM Cloud checks IAM access policies to determine what they are authorized to do. Authentication precedes authorization. |
| "The cloud provider secures the physical infrastructure; the customer secures data and identities." | L6 instructor guide | ✓ Verified | IBM Cloud Databases shared responsibility docs: "Cloud Databases is responsible for ensuring the security of data on disk and data in motion within our infrastructure. The Client is responsible for managing IBM Cloud passwords and database passwords…" Responsibility split confirmed; note it varies by service model. |
| "Continuous delivery requires a manual approval step before production." | L7 outline | ☐ Verify | Verify against CNCF or IBM Cloud Continuous Delivery docs. |
| "Continuous deployment automates the final release when tests pass." | L7 outline | ☐ Verify | Verify against CNCF or IBM Cloud Continuous Delivery docs. |

---

### 2C. Consistency Checks

| Check | Status | Notes |
|-------|--------|-------|
| Terminology is consistent across the instructor guide, learner workbook, and assessments. | ☐ Check | |
| Each vocabulary term introduced in a lesson appears in the corresponding assessment question (where applicable). | ☐ Check | |
| "Explain it twice" prompts in the learner workbook match the prompts described in the instructor guide. | ☐ Check | |
| Jargon-journal terms listed in the curriculum map match the terms assigned in each lesson. | ☐ Check | |
| No instructor answer keys appear in the learner workbook. | ☐ Check | |
| All analogy limitations are explicitly stated in the instructor guide. | ☐ Check | |
| Assessment questions address only objectives from Lessons 2, 3, and 6. | ☐ Check | |
| Pre-test and post-test questions are different but assess the same objectives. | ☐ Check | |
| All pilot tables and templates are blank (no invented data). | ☐ Check | |
| Future tense is used in the submission proposal for work and evaluation that has not occurred. | ☐ Check | |

---

### 2D. Accessibility Checks

| Check | Status | Notes |
|-------|--------|-------|
| No information is conveyed by color alone in any learner-facing document. | ☐ Check | |
| All activity cards and tables can be completed with text (letters) rather than symbols. | ☐ Check | |
| Font size in any printed materials is at least 12pt. | ☐ Check (applies at print time) | |
| "Explain it twice" and other written tasks can be completed verbally if needed. | ☐ Check | |
| Acronyms are spelled out on first use in every document. | ☐ Check | |
| Screen-reader-compatible plain-text alternatives are noted in the instructor guide. | ☐ Check | |

---

### 2E. Claims to Avoid — Final Check

Confirm that none of the following unsupported claims appear anywhere in the materials:

| Claim to avoid | Status |
|----------------|--------|
| "This curriculum is the first of its kind." | ☐ Confirm removed |
| "This curriculum has never been done before." | ☐ Confirm removed |
| "This curriculum is proven to be effective." | ☐ Confirm removed |
| "Studies show this teaching approach works." (without a cited study) | ☐ Confirm removed |
| Any invented participant scores, quotes, or pilot findings. | ☐ Confirm removed |
| Any invented citations or URLs. | ☐ Confirm removed |

---

## Section 3: How to Complete Verification

1. Open the authoritative source listed for a term.
2. Read the official definition.
3. Compare it to the definition in the instructor guide and learner workbook.
4. If the definition is accurate: mark ✓ Verified in the checklist and note the source and date.
5. If the definition needs adjustment: revise the relevant text in the instructor guide and workbook, mark ✓ Revised, and note what changed.
6. If a source is unavailable or the term is not covered: mark ⚠ Needs Attention and decide whether to remove the term, simplify the claim, or add a note to learners.

---

*[All [DRAFT] labels in the curriculum materials should be removed after verification is complete and replaced with a source citation.]*
