---
title: "Five Systems I Shipped: A Production Case Study Catalog"
date: 2026-05-09
categories:
  - Engineering
  - AI
  - Case Studies
tags:
  - case studies
  - production
  - ai
  - patents
  - tax tech
  - fintech
  - architecture
excerpt: "Five production systems from the last decade. Patents, platform rewrites, fraud prevention at scale. Each one shipped, each one moved a number that mattered."
header:
  image: /assets/linkedin/linkedin-banner.png
  og_image: /assets/linkedin/linkedin-banner.png
  teaser: /assets/linkedin/linkedin-banner.png
---

The most-asked question I get is some version of: *what have you actually shipped?* Fair enough. The deep-dive posts cover the systems one at a time. This is the consolidated version — five systems from the last decade, each one in production, each one moved a number the business cared about.

Where there's a deeper post on the system, I link to it. Where there isn't, I go a little deeper here.

```mermaid
graph TB
    A[Robby<br/>Vertex]
    B[Mort AI Nexus<br/>Vertex]
    C[Data Cake<br/>Vertex]
    D[Voice biometric<br/>JPMC]
    E[Strangler-fig<br/>Connect Your Care]
```
_Figure: five systems, five domains._

---

## 1. Robby — Multi-Agent SDLC System

**Where it ran:** Vertex Inc., Data & Insights value stream
**My role:** Inventor, lead engineer
**Year:** 2024–2026

The premise was the super-chicken problem. Teams stacked with high individual performers were producing less, not more. People were spending half their day in process — Jira hygiene, status updates, sprint planning, design reviews — and the half they had left wasn't enough to do the actual work.

Robby is a patent-pending multi-agent AI system for SDLC orchestration. The bet was that an AI layer could absorb the process work eating my team's day and give the humans back the hours they came here for. It paid out. The afternoons that used to vanish into Jira hygiene started going back into engineering.

**Tech:** multi-agent AI tooling, ArgoCD, GitHub Actions, Datadog
**Outcome:** Adopted across multiple teams; the "Raise the Boats" workshop trained ~50 engineers in the live cohort on how to extend the same approach
**Deeper read:** [Robby: I Built an AI System to Kill the Super Chicken Problem](/ai/engineering/leadership/2026/02/19/robby-ai-sdlc-system.html)

---

## 2. Mort AI Nexus — Multi-State Economic Nexus Detection

**Where it ran:** Vertex Inc., Indirect Tax Intelligence
**My role:** Inventor, principal engineer
**Year:** 2024–2026
**Status:** Patent pending

The Wayfair ruling in 2018 changed sales-tax compliance for every company doing business across state lines. Each state set its own thresholds — typically $100K in revenue or 200 transactions per year — and once you crossed the line you owed sales tax in that state. The catch: most companies didn't know they'd crossed until a state notice arrived months later, with penalties and interest stacked on top.

The existing approach was reactive. Tax teams reviewed quarterly reports and chased compliance after the fact. Financial exposure for a single missed state could run $100K–$500K.

Mort AI Nexus is a patent-pending AI system that shifts nexus discovery from reactive to predictive — so compliance teams can register and configure tax calculation ahead of crossing a state's threshold, instead of catching up after a state notice arrives. Customers stopped finding out about exposure from state notices and started finding out from the platform, weeks before the line.

**Tech:** Java, Spring Boot, AWS
**Outcome:** Customers shifted from reactive quarterly reviews to forward-looking nexus monitoring; preventable penalty exposure reduced

---

## 3. Voice Biometric Fingerprinting — JP Morgan Chase

**Where it ran:** JPMC TARA Fraud Busters, retail banking
**My role:** Lead developer
**Year:** 2018–2019

Knowledge-based authentication was a broken control. Every breached database in the prior decade had handed the answers — mother's maiden name, last four of the social — to whoever wanted them. A rep could ask all the right questions and authenticate the wrong person.

We built a voice biometric fingerprinting service inside JPMC's TARA Fraud Busters group. The service captured a passive voice fingerprint during the natural course of a customer call, matched it against the enrolled fingerprint for that customer, and returned a confidence score the rep saw before authenticating. The customer didn't have to say a passphrase. They just had to talk for a few seconds, which they were going to do anyway.

The deployment numbers told the story. **10 million unique JPMC accounts opted in during the first three months. Only 1,300 customers opted out.** That's a 99.87% adoption rate. The pilot shortened the average authenticated call by 20 seconds because reps weren't grinding through knowledge-based questions any more — which translated to 25 more customers serviced per rep per day.

The fraud-prevention number is the headline (~$830B in losses prevented across the deployment cohort). The customer-experience side was the quieter win. Security that made the customer's day shorter instead of longer is the kind of control people don't opt out of.

**Tech:** Python, ML/biometrics, REST APIs, Sapiens rules engine, Angular dashboard, JavaScript
**Outcome:** ~10M accounts onboarded in 90 days; 20-second call reduction per authenticated call; ~$830B in fraud losses prevented across the deployment cohort

---

## 4. Data Cake — NLP Synthetic Tax Data Generation

**Where it ran:** Vertex Inc., AI research
**My role:** Inventor, principal engineer
**Year:** 2024–2026
**Status:** Patent pending

You can't train tax AI on real customer transactions. The data is PII-laden, regulated, contractually restricted. You also can't train tax AI without realistic transactional data — synthetic data that doesn't reflect the statistical properties of real tax events produces models that fall apart in production.

Data Cake is a patent-pending system for generating realistic synthetic tax data that ML projects can train against without putting real customer transactions at risk. Synthetic outputs respect tax-law validity, so downstream models train on something that actually behaves like the production world.

What changed when we deployed it: model training stopped being a regulatory negotiation. New ML projects could spin up training data in days instead of quarters, without ever touching real customer information.

**Tech:** Python, NLP-driven generation
**Outcome:** Removed the data-access bottleneck for AI model training; enabled tax ML projects that previously couldn't be greenlit

---

## 5. Connect Your Care — Monolith to Microservices

**Where it ran:** Connect Your Care, HRCommand product
**My role:** Architect & lead engineer
**Year:** 2019–2021

Connect Your Care was a benefits-administration company sitting on a J2EE/EJB monolith built across the better part of a decade. HRCommand was the flagship product. The monolith worked. It served customers. It also blocked every strategic initiative the company wanted to ship — new product surfaces, new payer integrations, modern UX, all of it.

Standard advice for a monolith of that age is rip-and-replace. Standard outcome is a multi-year project that ships nothing while leadership rotates and the rewrite gets killed.

We didn't do that. We picked the strangler-fig pattern. Identified the bounded contexts inside the EJB monolith that were ready to come out — usually the ones with the most volatility or the clearest data ownership boundary. Built each one as a Spring Boot microservice running alongside the legacy WebLogic/Puppet stack. Routed live traffic to the new service through a thin proxy that fell back to the monolith on failure. Validated for two weeks per service. Then peeled it off the monolith. Repeat.

Five-person team. The React rewrite of the HRCommand UI shipped on Figma-to-code component delivery, so design and engineering were never out of sync on what was being built. We never broke production. We never took the platform down for a release. We did decompose enough of the monolith — and ship enough new product surface on top of the new architecture — that the company became attractive to acquirers in a way it hadn't been before.

**UnitedHealth / Optum Financial acquired Connect Your Care in 2021.** The architecture work was a direct contributor to the acquisition thesis. That's the part of this story I'm proudest of, and the part I'd repeat if I had a stable, profitable platform that needed to be modernized without being broken.

**Tech:** Spring Boot, J2EE/EJB, WebLogic, Puppet, React, Figma-to-code
**Outcome:** Modernized core product platform without downtime; contributed to UnitedHealth/Optum Financial acquisition

---

If you'd like to talk about any of these in depth — or you're working on something with the same shape and want a second opinion — I'm at [Dominick.do.Campbell@gmail.com](mailto:Dominick.do.Campbell@gmail.com), or [LinkedIn](https://www.linkedin.com/in/dominick-campbell-70b3619b/).
