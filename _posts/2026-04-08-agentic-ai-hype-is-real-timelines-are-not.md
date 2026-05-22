---
title: "The Agentic AI Hype Is Real. The Timelines Are Not."
date: 2026-04-08
categories:
  - AI
tags:
  - agents
  - architecture
  - LLMs
  - production
excerpt: "Everyone is shipping 'AI agents' right now. Having actually built them in production for three years, I have some thoughts on what's real and what's going to hurt people."
---

I've spent the last three years building multi-agent systems in production at Vertex — tax intelligence pipelines, audit defense, synthetic data generators. Four patent-pending inventions in the space. I am not standing in the way of the freight train.

I do want to talk about how fast it is actually moving, because the keynote version and the production version are not the same conversation.

```mermaid
graph LR
    I[Inflated<br/>expectations] --> D[Disillusionment]
    D --> P[Productivity<br/>plateau]
    P --> V[Real value]
```
_Figure: agentic AI follows the curve — the value at the end is real; the timeline isn't._

## The capability is genuinely there

The foundation models are good. GPT-4-class models can reason across complex multi-step problems, synthesize large document sets, write production code, and chain tool calls in ways that would have looked like science fiction five years ago. crewAI and AutoGen have matured. LangGraph gives you proper state management for non-trivial flows.

If you want an agent that researches a topic, drafts a report, validates sources, and formats the output — that works today. Well.

## Where reality bites

The keynote demos always show the agent "taking action." Submitting filings. Modifying records. Moving money. In tax, finance, and healthcare, you cannot have an agent autonomously do any of those without a verification layer in front of it. That's not a capability gap. It's the legal and operational reality of regulated domains, and pretending otherwise will get someone fired. Build for human-in-the-loop by default, not as the thing you'll add when compliance asks.

Reliability is the other thing the demos don't show. A single agent call has maybe a 2-3% failure rate on a complex task — hallucination, tool error, context-window weirdness. Chain five and that compounds. You need retry logic, fallback paths, observable failure states. The pretty demos have none of it, and that's why they don't survive contact with a real workload.

And the context windows. Yes, they're huge now. But large context isn't *coherent* context. I've watched 128K-window models quietly forget early constraints around the 90K-token mark. Chunk and retrieve. Don't just stuff the window and hope.

## What actually holds up

The pattern I keep coming back to: **small agents with clear contracts.** Not one big orchestrator trying to be everything. A pipeline of focused agents, each with one job, explicit inputs and outputs, and its own observability. Closer to microservices than monoliths.

The other one: treat your prompts like code. Version them, test them, review them before they go to production. I can't tell you how many production incidents I've seen that traced back to a prompt edit nobody reviewed because "it's just text."

## My honest take

We are in the awkward middle. Foundations are solid. Tooling is good. Patterns are still settling. The companies that win this cycle won't be the ones with the most impressive demos — they'll be the ones who figure out how to run agents reliably, observably, and safely at the scale a real business needs.

That's an engineering problem. Engineers who've been doing this for a few years have a real edge right now, and I'd rather spend that edge building things that actually work than shipping a demo that hallucinates a tax filing.

More soon.
