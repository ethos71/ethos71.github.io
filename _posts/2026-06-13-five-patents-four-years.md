---
title: "5 Patents in 4 Years: Innovating Inside a Regulated Industry"
date: 2026-06-13
categories:
  - Engineering
  - AI
tags:
  - patents
  - innovation
  - fintech
  - regulated-industries
  - vertex
excerpt: "Regulated industries are where innovation is HARDER, not easier. That's exactly why the patents that ship there are the ones that count."
header:
  og_image: /assets/linkedin/linkedin-banner.png
  teaser: /assets/linkedin/linkedin-banner.png
---

There's a story people tell about regulated industries: that they're where innovation goes to die. Slow procurement. Compliance review on every commit. ERPs that haven't been touched since 2009.

The friction is real. The conclusion is wrong. Innovation in regulated industries isn't worse — it's *harder*, which is exactly why the work that ships there is the work that compounds. You don't get to bolt on an LLM wrapper and call it a product. The data is constrained, the decisions are audited, and the downstream consequences are real money and real penalties.

Between 2022 and 2026 at Vertex, I shipped five patent-pending AI/ML systems into exactly that environment.

---

## 1. Data Cake — Synthetic Tax Data from Real Statistical Properties

You can't train tax AI on real customer transactions — legal and security both veto, correctly. But synthetic data that doesn't match the real statistical shape of tax events produces models that fall apart in production.

Data Cake is an NLP-driven generator that learns distributions and rare-event tails from real customer data, then produces synthetic streams matching those properties without preserving any traceable link. XGBoost and scikit-learn for statistical modeling; a deterministic rules engine enforcing tax-law validity. The unlock wasn't accuracy — it was that ML projects stopped being a regulatory negotiation.

[How Data Cake Got Built](/engineering/ai/2025/12/11/how-data-cake-got-built.html)

---

## 2. Doc Intel — Detecting When Code and Docs Have Divorced

Every engineering team has the same lie written on a README. It was true once. Three engineers pushed changes without updating it, and now it actively misleads.

Doc Intel detects when documents and the systems they describe have drifted, syncs metadata across systems automatically, and maintains the relationships between code, configuration, and compliance artifacts. In a regulated setting — audit trails, SOX-relevant docs, tax-treatment justifications — drift between code and documentation isn't an annoyance. It's an audit finding waiting to happen.

[Doc Intel: What Happens When Your Code and Docs Divorce](/engineering/ai/2026/01/28/doc-intel-patent.html)

---

## 3. Audit Management Red-Black Tree Timber Model — Decision Support for Audit Defense

Fortune 500 tax teams routinely sit on dozens or hundreds of open audit findings. Each one is a decision — contest, settle, or absorb — with different legal costs, time costs, and precedent implications. Most of those calls were being made on spreadsheets and institutional memory.

The Red-Black Tree Timber Model treats the portfolio of findings as a self-balancing tree of decisions. Each node carries expected cost, settlement risk, and precedent weight; the tree stays balanced as findings are added or resolved. The output isn't a recommendation — it's a structured view humans act on. The hard part wasn't the algorithm. It was modeling the *decision*, not the data.

[Why I Built a Self-Balancing Tree to Make Audit Defense Decisions](/engineering/ai/2025/10/22/audit-red-black-tree-patent.html)

---

## 4. Mort AI Nexus — Predicting Economic Nexus Before You Cross It

After the 2018 *South Dakota v. Wayfair* ruling, every state set its own economic-nexus threshold — typically $100K in revenue or 200 transactions a year — and crossing the line obligated you to collect sales tax there. Per-state penalty exposure runs $100K–$500K.

Existing compliance tools were reactive. Mort AI Nexus shifts the horizon, combining transaction patterns, regional economic signals, and historical filing data to forecast a crossing weeks in advance. The change wasn't accuracy — it was timing. Customers stopped finding out from state notices and started finding out from the platform.

[Mort AI Nexus: Predicting Economic Nexus Before It Bites You](/engineering/ai/2026/01/14/mort-ai-nexus-patent.html)

---

## 5. Robby — Multi-Agent SDLC System

The other four patents are products. Robby is the operating system underneath the team that built them.

Robby is a multi-agent orchestration framework — **70 skills, 15 specialized roles**. A head-chef orchestrator routes work to specialist agents: architecture, testing, project management, security, UX. Each agent has focused tools and a narrow job. The running code is the source of truth, and the agents read it to produce specs, sprint plans, and reviews from there. The bet was that an AI orchestrator could absorb the process work eating half my team's day and free the humans to do the engineering they actually love. It paid out — and spawned the methodology that produced the other four patents.

[Robby: I Built an AI System to Kill the Super Chicken Problem](/ai/engineering/leadership/2026/02/19/robby-ai-sdlc-system.html)

---

## Why this is the work I'm proudest of

Five patent-pending inventions in four years sounds like a number. The thing it isn't is luck.

Each one started from a real problem in a regulated environment where the easy answer wasn't available. No customer data to train on. No way to escape the audit trail. No rip-and-replace allowed. The constraints were the design problem — and the patents are what fell out of solving the design problem honestly.

If you hear "regulated industry" and think "no innovation lives there," you're reading the situation backwards. The innovation that lives there is the kind that has to actually work — because if it doesn't, somebody's compliance team finds out, and then everybody's compliance team finds out.

That's the work I want to do more of.

Back to building.
