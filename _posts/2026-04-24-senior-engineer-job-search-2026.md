---
title: "What a Senior Engineer's Job Search Actually Looks Like in 2026"
date: 2026-04-24
categories:
  - Career
tags:
  - job search
  - senior engineer
  - AI
  - hiring
excerpt: "I'm back on the market after four years at Vertex. Here's what's the same, what's completely different, and what I wish someone had told me before I started."
---

I haven't job searched since 2022. Four years. In tech, that's like coming back from an expedition to find the terrain has shifted.

I'm a Principal Engineer with 25+ years of experience, four patent-pending AI inventions, and a track record I'm genuinely proud of. And I'm also relearning how to do this whole thing.

A few things I've noticed in the first few weeks.

## The ATS problem is worse than you think

I knew ATS (Applicant Tracking Systems) were a thing. I didn't fully appreciate how aggressively they filter until I started actually testing my resume against job descriptions.

Here's the blunt reality: if your resume isn't formatted for machine parsing, a human may never read it. This is not an exaggeration. I rebuilt my resume from scratch in LaTeX specifically to get clean pdftotext output. I had a font artifact in my original version — the font's small-caps rendering was mapping the letter 'I' in "Principal" to a lowercase glyph in the extracted text. ATS was reading "PRiNCiPAL ENGiNEER." Nobody told me. I caught it because I checked.

Run `pdftotext` on your resume. Read what it outputs. That's what the system sees.

## The "AI will take your job" narrative is backwards for senior engineers right now

The engineers getting squeezed by AI right now are the ones who were doing things that were always a bit mechanical — boilerplate CRUD apps, basic data pipelines, junior-level ticket work. That's real, I'm not dismissing it.

But for senior engineers who can architect systems, evaluate tradeoffs, and lead teams through ambiguous problems? The demand is higher than I expected. Companies are building AI-powered products faster than they can find people who know how to build them responsibly.

The job descriptions I'm seeing for principal/staff roles are asking for things like: multi-agent system design, LLM observability, AI safety/reliability patterns, leading teams through an AI transformation. That's a narrow pool. I happen to be in it.

Know what your specific value is. Don't compete on breadth — compete on depth.

## The conversation that's changed

In 2022, most technical interviews at the senior level were about system design — scale, tradeoffs, distributed systems. That's still there. But now there's an overlay:

*How would you AI-enable this?* shows up everywhere. Which is fine. What's interesting is that the interviewers vary wildly in their own understanding. Some are genuinely sophisticated. Some are clearly fishing to see if you'll say "just add an LLM" to everything, which is the wrong answer they're looking for you not to give.

My advice: be honest about what AI is good at and where it fails. The interviewers who matter will respect that more than enthusiasm without nuance.

## What I'm looking for

I want to build something real. Not a proof-of-concept. Not an "AI strategy" document. A production system that solves a hard problem for people who need it solved.

Tax, compliance, fintech — I know those domains. But I'm open to any technically hard problem where the stakes are real and the team is serious.

If that's you, [find me on LinkedIn](https://linkedin.com/in/dominick-campbell).

More updates as this unfolds. I'm going to document this process — the good, the awkward, and the things that don't work — because I think more senior engineers should talk honestly about what job searching is actually like. We tend to only share the win announcement.

More soon.
