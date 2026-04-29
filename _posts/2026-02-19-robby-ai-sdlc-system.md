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
excerpt: "Robby is a multi-agent SDLC system with 70 skills and 15 roles that handles everything from Jira to deployments. It's not about replacing engineers. It's about removing process friction so people can do what they love — and was my answer to the super chicken problem."
---

A few years ago I watched a TED talk that I haven't been able to stop thinking about.

[Margaret Heffernan: Forget the Pecking Order at Work](https://www.ted.com/talks/margaret_heffernan_forget_the_pecking_order_at_work).

The short version: researchers studied flocks of chickens to find what made the most productive ones. They identified the "super chickens" — the highest individual producers — and bred them together. Generation after generation of super chickens.

The result wasn't a super-productive super flock. Most of the chickens were dead. The super chickens had pecked the others to death.

She then draws the parallel to corporate teams. The companies that stack their teams with the highest individual performers — the alphas, the dominators, the super chickens — consistently underperform teams built for collaboration, psychological safety, and mutual contribution.

I built Robby because I believe she's right. And because I think AI can finally do something about it.

## What Robby is

Robby is a multi-agent orchestration system I've been building for years that handles the entire software development lifecycle. When I say entire, I mean it: **70 skills. 15 specialized roles.**

The code is the single source of truth. Not the Jira board. Not the Confluence doc. Not the PowerPoint someone made six months ago that is now actively misleading people. The running code.

From that source of truth, Robby coordinates a full kitchen of specialized agents.

## The Kitchen Metaphor

We called it the kitchen because that's what it is. Robby is the **head chef**.

When a project comes in, Robby doesn't try to do everything himself. He knows which chef to call. The **@test chef** has a full set of testing skills — TDD patterns, Cypress templates, integration test scaffolding, coverage analysis — and Robby hands him the ticket and says *make the soup*. The @test chef uses his skills like a chef uses recipes: proven patterns, applied with judgment to the specific ingredients in front of him.

The 15 roles cover the full SDLC:

- **@arch** — Architecture agent: ADRs, technical design docs, tradeoff analysis
- **@eng** — Engineering agent: implementation, PR review, code generation
- **@test** — Testing agent: TDD, Cypress, integration tests, coverage
- **@pm** — Project management: sprint planning, Jira hygiene, DSU updates, stakeholder docs
- **@pcx** — UX/product experience agent: design reviews, accessibility, user story refinement
- **@patent** — Patent agent: invention disclosure drafting, prior art analysis, technical claim support
- **@sec** — Security agent: vulnerability scanning, threat modeling, dependency audit
- **@data** — Data agent: schema design, migration planning, query review
- **@devops** — Deployment agent: pipeline review, infra-as-code, rollback planning
- **@docs** — Documentation agent: README generation, API docs, runbooks
- ...and more

Each role has a focused set of skills, prompt templates, and tool access. They share context. They review each other's outputs. No single agent does everything — the same reason a real kitchen doesn't have one person cooking, plating, expediting, and washing dishes.

## Robby Has a Phone on the Wall

The MCP server integration is how Robby stays connected to the real world. Think of it like the phone on the kitchen wall — when something goes wrong in the restaurant, the head chef doesn't go check himself. He picks up the phone.

Robby can pick up that phone and ask:

- **ArgoCD**: Is the deployment actually running? Did the sync fail?
- **GitHub Actions**: Did the CI pipeline pass? Which step failed and why?
- **Datadog**: Are there new errors in production since the last deploy? What's the error rate?
- **PagerDuty**: Is there an active incident? Is anyone paged?
- **Jira/Linear**: What's the current sprint state? What's blocked?

This is what makes Robby different from a code generation tool. It's not just generating artifacts — it's **aware of the system it's operating in**. When @devops generates a deployment plan, it checks ArgoCD first. When @eng closes a PR, it waits for the GH Action and checks Datadog for regression signals. The agents act with context, not in a vacuum.

## What Robby Actually Removes

Robby doesn't replace engineers. It removes the *friction* — the process overhead that consumes time and creates status games that nobody signed up for.

Nobody loves updating Jira. Nobody is passionate about formatting a PRR. Nobody went into software engineering because they wanted to write the "Current State" section of an operational readiness document for the fourth time this year.

But those things have to get done. And when they fall on humans, they create:
- **Resentment** — nobody wants to do them, so they pile up or get done badly
- **Status dynamics** — the person who controls the docs controls the narrative
- **Context loss** — docs drift from reality because nobody keeps them current

When Robby handles them — **automatically, from the code, without anyone having to ask** — the team gets that time back. Engineers do engineering. Architects think about architecture. PMs do actual product thinking. UX designers do UX.

The artifacts Robby generates automatically:
- **ORDs** (Operational Readiness Documents) for production deployments
- **PRRs** (Production Readiness Reviews) for engineering sign-off
- Technical design documents for teams picking up new work
- Planning documents for project managers
- Executive summaries for leadership
- Daily standup summaries — written from the actual code changes, not whoever remembers to type in Slack
- Story point estimates with rationale based on code complexity, not gut feel
- Confluence documentation, kept in sync with the codebase
- Invention disclosure drafts (yes, @patent helped me write my own patent applications)

## Robby Rivaled a $1.25 Billion Startup

Linear.app raised $82 million in June 2025 at a **$1.25 billion valuation**. 135 people. $100M ARR. The entire pitch is that Jira is broken and teams deserve better tooling.

They're not wrong about Jira being broken. But the Linear approach is still fundamentally: *give humans a better interface for doing the process work themselves.*

Robby's answer was different: **what if the agents just do the process work?** Not a better Jira. No Jira at all for the things that don't require human judgment.

I'm not saying Robby is a Linear killer — Linear is a great product and they've earned their valuation. But the problem spaces are adjacent, and the approaches reflect fundamentally different beliefs about where human attention should go.

## Amazon Just Validated the Whole Thesis

On April 28, 2026 — literally yesterday — Amazon announced it's targeting mass hiring automation with agentic software, with an explicit goal to "humanize AI" by making it handle the process work so humans can focus on what matters.

They've put **$200 million** into their AWS Generative AI Innovation Center specifically to move agentic AI from prototypes to production SDLC integration. Their Bedrock AgentCore platform, Agent Development Kit, and multi-agent orchestration tooling are all pointed in the same direction Robby has been pointing for years.

Amazon is a $2 trillion company. When they spend $200M validating your architecture, that's a signal worth noting.

## Why It's My Life's Work

The best engineers I've worked with became engineers because they love solving hard problems. They love the craft. They love the moment when a complex system clicks into place and does something elegant.

None of them love filling out Jira tickets. None of them love writing the Current State section of a document nobody will read. None of them signed up to spend 40% of their time in process theater.

The super chicken problem in software teams isn't just that the dominant engineers crowd out others. It's that the process overhead itself selects for the wrong things — the people who are good at playing the process game, not the people who are good at building software.

Robby is my answer. Not a complete answer. A direction. A bet that the best version of an engineering team is one where every person is spending their time on the part of the job that made them want to do this in the first place.

Less pecking. More building.

---

*I'm actively developing Robby and looking for teams who want to think seriously about what AI-augmented engineering actually looks like. [Find me on LinkedIn](https://linkedin.com/in/dominick-campbell).*

