# LinkedIn Projects Section — Copy/Paste Content

Five entries to paste into the LinkedIn **Projects** section under Experience. Each one fits the LinkedIn project format (title / dates / link / description).

To add: LinkedIn → Profile → Add profile section → Recommended → Add projects.

---

## Project 1: Robby — Multi-Agent SDLC System

**Project name:** Robby — Multi-Agent SDLC Orchestration System

**Associated with:** Vertex Inc. (Principal Software Engineer)

**Dates:** Jun 2024 – May 2026

**Project URL:** https://ethos71.github.io/2026/02/19/robby-ai-sdlc-system.html

**Description:**

Designed and built a production multi-agent orchestration system that handles the entire software development lifecycle. Robby is a head-chef agent that routes incoming work to 15 specialized agent roles (architecture, engineering, testing, project management, security, UX, documentation, etc.) with 70 distinct skills. The code is the source of truth; agents read running code and produce specs, reviews, sprint plans, and stakeholder documentation.

Key wins:
• Adopted across multiple teams in Vertex's Data & Insights value stream
• Trained ~50 engineers via the AI Curiosity Workshop ("Raise the Boats")
• Removed process friction (Jira hygiene, status updates, design reviews) so engineers could focus on actual engineering

Tech: crewAI, AutoGen, LangChain, Langfuse, MCP, Vue.js, ArgoCD, GitHub Actions, Datadog

---

## Project 2: Mort AI Nexus — Multi-State Economic Nexus Detection

**Project name:** Mort AI Nexus — Real-Time Multi-State Tax Nexus Detection (Patent Pending)

**Associated with:** Vertex Inc. (Principal Software Engineer)

**Dates:** Jan 2024 – May 2026

**Project URL:** https://ethos71.github.io/2026/01/14/mort-ai-nexus-patent.html

**Description:**

Patent-pending AI system that detects multi-state economic nexus thresholds in real time, informed by the 2018 South Dakota v. Wayfair ruling. Each US state set its own thresholds (typically $100K revenue or 200 transactions per year); crossing a threshold creates immediate sales tax obligation, often discovered months later via state notices with stacked penalties.

Mort AI Nexus monitors transaction patterns in real time, predicts approaching thresholds, and triggers proactive registration workflows before crossing — shifting customers from reactive quarterly reviews to live nexus monitoring.

Per-state financial exposure: $100K–$500K. Outcome: customers stopped finding out about nexus exposure from state notices and started finding out from the platform, weeks before the line.

Tech: Java, Spring Boot, AWS, ML pattern analysis, real-time transaction streaming

---

## Project 3: Voice Biometric Fingerprinting at JPMorgan Chase

**Project name:** Voice Biometric Fingerprinting — Call-Center Authentication

**Associated with:** TekSystems for JP Morgan Chase

**Dates:** Feb 2018 – Feb 2019

**Description:**

Lead developer on JPMC's voice biometric fingerprinting service for retail-banking call-center authentication. Knowledge-based authentication (mother's maiden name, last four of SSN) had become a broken control after years of database breaches handed the answers to attackers.

Built a passive voice fingerprint service: the customer authenticates by talking naturally during the call, no passphrase required. The rep sees a confidence score before authenticating.

Deployment results in the first 90 days:
• ~10 million unique JPMC accounts opted in
• Only ~1,300 customers opted out
• Average authenticated call shortened by 20 seconds → 25 more customers serviced per rep per day
• ~$830B in industry-wide fraud loss plateau across the deployment cohort

Tech: Python, ML/biometrics, REST APIs, Sapiens rules engine, Angular dashboard, JavaScript

---

## Project 4: Data Cake — NLP Synthetic Tax Data Generation

**Project name:** Data Cake — NLP Synthetic Tax Data Generation (Patent Pending)

**Associated with:** Vertex Inc. (Principal Software Engineer)

**Dates:** Jul 2024 – May 2026

**Project URL:** https://ethos71.github.io/2025/12/11/how-data-cake-got-built.html

**Description:**

Patent-pending NLP service that generates realistic synthetic tax data by learning statistical properties from real customer transactions — without exposing PII. Real customer data is regulated and contractually restricted; naive synthetic data destroys the statistical properties tax models need.

The pipeline learns distributions over jurisdictions, transaction sizes, taxability codes, exemption patterns, and rare-event tails. A deterministic rules engine enforces tax-law constraints in the output so every synthetic transaction is a valid transaction (correct jurisdictional codes, plausible product types, valid certificates).

Outcome: removed the data-access bottleneck for AI model training. New tax ML projects spin up in days instead of quarters. Models trained on Data Cake performed within 2% of models trained on real data, without ever touching real customer information.

Tech: Python, XGBoost, scikit-learn, NLP, deterministic rules engine

---

## Project 5: Connect Your Care — Monolith to Microservices Decomposition

**Project name:** HRCommand — Strangler-Fig Decomposition of a J2EE Monolith

**Associated with:** Connect Your Care (Senior Software Engineer)

**Dates:** May 2019 – Apr 2021

**Description:**

Architect and lead engineer for the systematic incremental decomposition of Connect Your Care's HRCommand benefits-administration platform — a decade-old J2EE monolith on WebLogic — into Spring Boot microservices and a React frontend.

Used the strangler-fig pattern. Identified bounded contexts inside the monolith with the highest volatility or clearest data ownership boundary; built each one as a microservice; routed live traffic through a thin proxy with monolith fallback; validated for two weeks; then peeled the bounded context off the monolith. Repeated.

Five-person team. Never broke production. Never took the platform down for a release. Decomposed enough of the monolith — and shipped enough new product surfaces on top of the new architecture — to make the company an attractive acquisition target.

United Health / Optum Financial acquired Connect Your Care in 2021. The architecture work was a direct contributor to the acquisition thesis.

Tech: Spring Boot, J2EE, WebLogic, Puppet, React, Figma-to-code, Kubernetes
