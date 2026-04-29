---
title: "Robby: I Built an AI System to Kill the Super Chicken Problem"
date: 2026-02-19
categories:
  - AI
  - Engineering
  - Leadership
tags:
  - agents
  - sdlc
  - robby
  - multi-agent
  - teams
  - crewai
excerpt: "Robby is a multi-agent SDLC system I've been building for years. It's not about replacing engineers. It's about removing the process friction that makes brilliant people miserable — and was my answer to Margaret Heffernan's TED talk on super chickens."
---

A few years ago I watched a TED talk that I haven't been able to stop thinking about.

[Margaret Heffernan: Forget the Pecking Order at Work](https://www.ted.com/talks/margaret_heffernan_forget_the_pecking_order_at_work).

The short version: researchers studied flocks of chickens to find what made the most productive ones. They identified the "super chickens" — the highest individual producers — and bred them together. Generation after generation of super chickens.

The result wasn't a super-productive super flock. Most of the chickens were dead. The super chickens had pecked the others to death.

She then draws the parallel to corporate teams. The companies that stack their teams with the highest individual performers — the alphas, the dominators, the super chickens — consistently underperform teams built for collaboration, social safety, and mutual contribution.

I built Robby because I believe she's right. And because I think AI can finally do something about it.

## What Robby is

Robby is a multi-agent system I've been building and refining for years that orchestrates the entire software development lifecycle using specialized AI agents in defined roles.

The core roles:

- **@arch** — Architecture agent. Reviews the codebase, generates architectural decision records, produces technical design documents, evaluates tradeoff proposals.
- **@eng** — Engineering agent. Writes code, reviews PRs, generates unit tests, produces implementation plans, handles the actual build work.
- **@pm** — Project management agent. Reads the codebase and outstanding work, generates planning documents, updates project trackers, drafts executive summaries, produces sprint reports.

The code is the source of truth. Not the Jira board. Not the Confluence doc. Not the PowerPoint someone made six months ago. The actual running code.

From that single source of truth, Robby can generate:

- **ORDs** (Operational Readiness Documents) for production deployments
- **PRRs** (Production Readiness Reviews) for engineering sign-off
- Technical design documents for teams picking up new work
- Planning documents for project managers
- Executive summaries for leadership
- DSU (daily standup) updates
- Story point estimates with rationale
- Confluence documentation, kept in sync with the code

Every one of those artifacts is something that smart engineers currently spend time doing that is not the thing they became engineers to do.

## The super chicken problem in software teams

Here's how the super chicken pattern manifests on engineering teams.

The alpha engineers — the ones who are technically brilliant and know it — tend to dominate the process work too. They run the standups. They weigh in on every story point. They write the architecture docs in their own voice, which encodes their assumptions and makes it hard for others to challenge them. They volunteer for the high-visibility work and route the unglamorous stuff to others.

The result: the team's knowledge and decision-making collapses into a few people. Everyone else becomes a supporting actor. The brilliant mid-level engineers who might have great ideas stop offering them because the dynamic punishes it.

This is a real problem. I've watched it happen. I've probably contributed to it.

## What Robby actually removes

Robby doesn't replace engineers. It removes the *friction* — the process overhead that consumes time and creates status games.

Nobody loves updating Jira. Nobody is passionate about formatting a PRR. Nobody went into software engineering because they wanted to write the "Current State" section of an operational readiness document for the fourth time this year.

But those things have to get done. And when they fall on people, they create:
- Resentment (because nobody wants to do them)
- Status dynamics (the person who controls the docs controls the narrative)
- Context loss (the docs drift from reality because nobody keeps them current)

When Robby handles them — **automatically, from the code, without anyone having to ask** — the team gets that time and energy back. The engineers can do engineering. The architects can think about architecture. The PMs can do actual product thinking instead of Jira hygiene.

## The coordination model

What made the multi-agent approach the right one here is the same reason it works in real teams: **specialization with shared context.**

@arch, @eng, and @pm each have different tools, different prompts, different evaluation criteria. But they share the same codebase, the same tickets, the same history. When @pm generates a sprint plan, it's informed by what @eng thinks is feasible. When @arch produces a design doc, @eng can flag implementability concerns. The agents review each other's outputs.

That's not how most agent demos work. Most show a single agent doing everything. Robby is built on the insight that **role separation produces better outputs** — the same way a team of specialists produces better software than one person doing everything.

## Why it's my life's work

I've been thinking about this problem since before I had the tools to solve it. I've watched too many good engineers leave teams — or leave the profession — because the process ate them alive. Because they spent 40% of their time in meetings, filling out forms, explaining their work to people who weren't going to read it anyway.

Robby is my answer to that. Not a complete answer. Not a finished product. But a real, working system that I've used on actual projects to generate actual artifacts that actual people found useful.

The goal was never to build a faster way to fill out Jira tickets. The goal was to give people back the part of the job they actually love — the hard thinking, the creative problem-solving, the craft — by automating away the part that nobody loves but everyone has to do.

If Heffernan is right that super chickens are the problem, then Robby is my attempt at the solution: a system that removes the conditions that create super chickens in the first place.

Less pecking. More building.

---

*I'm actively developing Robby and looking for teams who want to think seriously about what AI-augmented engineering actually looks like. [Find me on LinkedIn](https://linkedin.com/in/dominick-campbell).*
