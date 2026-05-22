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

## 1. Data Cake — Synthetic Training Data for a Regulated Industry

**Domain:** synthetic training-data generation for tax/ML in a PII-constrained environment.

You can't train tax AI on real customer transactions — legal and security veto, correctly. Data Cake is the patent-pending answer to that constraint, designed so ML projects inside a regulated industry can spin up training corpora without negotiating with compliance for a quarter. The unlock wasn't accuracy — it was that ML projects stopped being a regulatory negotiation.

[How Data Cake Got Built](/engineering/ai/2025/12/11/how-data-cake-got-built.html)

---

## 2. Doc Intel — Code / Documentation Drift Detection

**Domain:** developer tooling for regulated environments where stale documentation becomes an audit finding.

Every engineering team has the same lie written on a README. It was true once. Three engineers pushed changes without updating it, and now it actively misleads. Doc Intel is the patent-pending system that makes that drift visible and measurable — so docs stop being a trailing indicator of trust.

[Doc Intel: What Happens When Your Code and Docs Divorce](/engineering/ai/2026/01/28/doc-intel-patent.html)

---

## 3. Audit Management Timber Model — Decision Support for Audit Defense

**Domain:** decision support for Fortune 500 tax-audit defense portfolios.

Fortune 500 tax teams routinely sit on dozens or hundreds of open audit findings. Each one is a decision — contest, settle, or absorb — with different legal costs, time costs, and precedent implications. Most of those calls were being made on spreadsheets and institutional memory. The patent-pending Timber Model turns that decision portfolio into something teams can reason about systematically. The hard part wasn't the algorithm — it was modeling the *decision*, not the data.

[Why I Built a Decision-Support Model for Audit Defense](/engineering/ai/2025/10/22/audit-red-black-tree-patent.html)

---

## 4. Mort AI Nexus — Economic Nexus Forecasting

**Domain:** predictive multi-state economic-nexus compliance for the post-*Wayfair* sales-tax landscape.

After the 2018 *South Dakota v. Wayfair* ruling, every state set its own economic-nexus threshold and crossing the line obligated you to collect sales tax there. Per-state penalty exposure runs $100K–$500K. Existing compliance tools were reactive. Mort AI Nexus is the patent-pending system that shifts that horizon forward — customers stopped finding out from state notices and started finding out from the platform.

[Mort AI Nexus: Predicting Economic Nexus Before It Bites You](/engineering/ai/2026/01/14/mort-ai-nexus-patent.html)

---

## 5. Robby — Multi-Agent SDLC Tooling

**Domain:** multi-agent AI tooling for software-development-lifecycle orchestration.

The other four patents are products. Robby is the operating system underneath the team that built them — a patent-pending multi-agent system for SDLC orchestration, built to remove the process friction eating half my team's day so the humans could spend their time on the work they actually came here for. It paid out, and the methodology behind it is what produced the other four patents.

[Robby: I Built an AI System to Kill the Super Chicken Problem](/ai/engineering/leadership/2026/02/19/robby-ai-sdlc-system.html)

---

## Why this is the work I'm proudest of

Five patent-pending inventions in four years sounds like a number. The thing it isn't is luck.

Each one started from a real problem in a regulated environment where the easy answer wasn't available. No customer data to train on. No way to escape the audit trail. No rip-and-replace allowed. The constraints were the design problem — and the patents are what fell out of solving the design problem honestly.

If you hear "regulated industry" and think "no innovation lives there," you're reading the situation backwards. The innovation that lives there is the kind that has to actually work — because if it doesn't, somebody's compliance team finds out, and then everybody's compliance team finds out.

That's the work I want to do more of.

Back to building.
