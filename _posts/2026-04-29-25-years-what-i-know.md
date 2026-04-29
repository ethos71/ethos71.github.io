---
title: "25 Years In, Here's What I Actually Know About Building Systems"
date: 2026-04-29
categories:
  - Engineering
tags:
  - career
  - architecture
  - AI
  - leadership
excerpt: "After 25+ years shipping systems from COBOL mainframes to AI agents, here's the unvarnished truth about what makes software last — and what kills it."
---

I started writing software professionally when `Y2K` was a genuine existential threat and COBOL was
a sensible career choice. I've since shipped systems in Assembly, Java, JavaScript, Python, Go, and
things I'd rather not admit to in polite company.

Along the way I've learned a few things that no architecture book will tell you directly.

## 1. The database outlives everything

You will rewrite the application 4 times. The database schema you shipped in 2008 will still be
there in 2026, quietly haunting every new engineer who joins the team. Design your data model like
it's permanent. Because it basically is.

## 2. Observability is a feature, not a tax

Every system I've seen fail catastrophically — a $500M tax close pipeline, a fraud detection
service at JPMC, a healthcare enrollment platform — failed silently first. Nobody knew it was
broken until it was very broken. Build the dashboards before you build the features.

## 3. AI doesn't change the fundamentals, it raises the stakes

I hold 4 patent-pending AI inventions now. I've built LLM-backed audit defense tools, synthetic
data generators, and multi-agent systems. And the most important thing I've learned is this:
**AI doesn't eliminate the need for good system design — it punishes bad system design faster.**

A poorly-designed traditional service degrades gracefully. A poorly-designed AI service hallucinates
confidently.

## 4. The best engineers I've met are fundamentally teachers

At Vertex, I built and delivered the "Raise the Boats" curriculum — teaching 200+ engineers and
analysts how to use AI tools and build production agents. The engineers who resisted "wasting time
teaching" were consistently the ones whose work became a single point of failure.

Knowledge that lives in one person's head is technical debt you haven't put on the balance sheet yet.

## 5. Every great product I've shipped had a clear owner

Not a committee. Not a Jira board. One person who cared deeply and was empowered to make calls.
The HRCommand product at Connect Your Care drove an acquisition. The voice biometric fraud system
at JPMC hit 10 million accounts in 3 months. Both had clear owners.

---

I'm writing more here as I go. If any of this resonates, find me on
[LinkedIn](https://linkedin.com/in/dominick-campbell) or
[GitHub](https://github.com/ethos71).
