---
title: "I Ran the AI Curiosity Workshop at Vertex. Here's What I Learned."
date: 2026-03-18
categories:
  - AI
  - Leadership
tags:
  - agents
  - teaching
  - crewai
  - autogen
  - vertex
excerpt: "Running the AI Curiosity Workshop — internally branded 'Raise the Boats' — at Vertex taught me more about how people actually learn AI than any framework documentation ever could."
---

When I pitched the idea internally, the reaction was roughly: *that's a lot of time to spend on something that isn't shipping features.*

I pushed anyway. By the time we wrapped, ~50 employees across engineering, product, data science, and — yeah — some finance folks had gone through the **AI Curiosity Workshop** (we called it "Raise the Boats" internally). I learned more from teaching it than I expected.

## The thing nobody told me about teaching AI

Most engineers I work with are smart. Like, genuinely sharp. But when I started the curriculum, I kept hitting the same wall: people understood what a large language model *was* in the abstract, but they couldn't picture what to actually *do* with it in the context of their day job.

That's not an intelligence problem. That's a framing problem.

The breakthrough came when I stopped starting with "here's how transformers work" and started with: *what's the thing in your week that makes you want to throw your laptop?* Then we'd build something that fixed that. Small. Concrete. Theirs.

By week two, people were building real things. One of our analysts built a tool that pre-drafted responses to our most common customer audit questions using RAG over our internal knowledge base. She'd never written a line of Python before. Took her four hours.

That's the thing about agents. The barrier isn't technical — it's imagination.

## What actually works in production (and what doesn't)

We used crewAI and AutoGen heavily. Both are solid. But I want to be honest about what I saw in real projects versus what the demos show you:

**What works:**
- Multi-agent pipelines for research + synthesis tasks (summarize → validate → format)
- RAG over structured internal data (policies, audit histories, transaction logs)
- Code review and doc drift detection (which became the Doc Intel patent, actually)

**What doesn't (yet):**
- Fully autonomous decision-making on anything with financial consequence
- Agents that "just handle it" without a human-in-the-loop step somewhere
- Anything where the failure mode is silent

The silent failure thing is the one I hammer on hardest in every session. A traditional service throws a 500. An agent confidently gives you a wrong answer with excellent grammar. Those are not the same failure mode and they don't get caught by the same monitoring.

## The unexpected win

The best outcome of the whole program wasn't the tools people built. It was the language.

After running it, teams started having different conversations. Instead of "we need a developer to build a script for this," it was "can we agent this?" Product managers were writing prompt templates. Data analysts were chaining tools together. The vocabulary changed, and with it, what felt possible.

That's what "raise the boats" means to me. Not that everyone becomes an ML engineer. That everyone's working at a higher waterline.

We're just getting started.
