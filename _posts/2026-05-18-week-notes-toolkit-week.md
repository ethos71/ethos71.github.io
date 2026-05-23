---
title: "Week Notes — May 18: The Week the Toolkit Earned Its Keep"
date: 2026-05-18
categories:
  - Notes
  - Engineering
  - AI
tags:
  - dev log
  - dom
  - smartballz
  - job search
excerpt: "First of a weekly cadence. Less essay, more field notes — what shipped, what surprised me, where the week actually went."
---

## What I shipped

Most of the week went into **`dom`**, the AI cost-cutting toolkit. The premise is simple: most coding tasks don't need a $2 Opus call. Haiku at one cent does it, and a third of the time a local Ollama model does it for free. `dom` routes the task to the cheapest model that can actually do it. One curl command installs it into any project; an eval policy gates every change.

Three things landed this week:

1. **Polyglot smoke matrix.** Three full compose stacks proving the toolkit scaffolds any combination of UI × API × DB: React+Spring+H2, React+Python+H2, and Node+C#+Oracle+Ollama. Same Karate feature runs against all three and must return the literal string `hello world` end-to-end. Three different language runtimes, four database vendors, and one assertion. That's a contract.

2. **Edit-everywhere, today.** As of an hour ago, every stack now has a working edit button — UI fires a `PUT /hello`, the API tier proxies to the AI tier, the AI tier detects edit intent via a deterministic regex (no LLM for the parse — too expensive, too unreliable), and the underlying DB row gets updated. The byte-exact `hello world` contract still passes for any non-edit input. Five files, three languages, one consistent pattern.

3. **A `@dom` orchestrator agent** with hard rules about what it routes versus what it doesn't touch. It's the front door for "how do I do X in `dom`?" and it doesn't write code — that's the next agent down the chain.

`dom` is going to underwrite everything I build for the next year. I'd rather spend a Saturday once than $200/mo on tokens forever.

## What else moved

- **`@job`** got rebuilt. Scope cut to job-hunt only, outplacement and separation docs moved out, validated-only pipeline, dashboard cleanup. The agent was carrying too much; I trimmed it to the one thing it has to do.

- **`smartballz`**, my fantasy-football XGBoost project, got a silent-failure sweep — banned a class of broad-except handlers that were masking real DB errors as "bad credentials." Also fixed two actual model bugs (Ohtani showing on waivers when he shouldn't, mid-tier trade values flattening out). The kind of week where you stop and notice the model is wrong before the league does.

- **`nyx-crm`** got a CI shell-injection fix and a FastMCP server with 19 verification tools — branch protection, audit logs, AI-call routing, skill search, diff, prisma studio. Boring infrastructure week. Boring infrastructure is good.

If you're keeping score: that's four repos with substantive commits in seven days, all while running an active job search. The fact that I can do that is the toolkit doing its job.

## The other layer

I'm between roles. Anyone who's followed along knows that. Family stuff in the mix means I'm deliberate about fit right now — and "deliberate" doesn't mean "slow," it means I know exactly what I'm looking for and I won't sign for less. Senior engineering roles where the AI work is real, the team is serious, the problem is hard. Not AI-strategy-document jobs.

My kid had a great week at his Challenger sports program — the league for kids of all abilities. Every week I'm reminded that the people who run those programs are doing harder work than most engineering teams I've been on, with a fraction of the resources, and they show up cheerful every Saturday. I think about that a lot.

## What's next

Two threads. On the engineering side: `dom` gets a release tag this week and I start dogfooding it across all the side projects — already doing that, but now with versioned install instructions. On the job-search side: several real conversations in motion. Not naming names; the right ones are good shape.

If you're here from a posting or recruiter intro — what I write here is what I think.

More next week.
