---
title: "How I Built Decision Support for Audit Defense"
date: 2025-10-22
categories:
  - Engineering
  - AI
tags:
  - patents
  - tax tech
  - audit
  - decision support
excerpt: "Audit defense decisions were being made by gut feel and whoever had the most institutional memory in the room. I built a patent-pending model to change that."
header:
  og_image: /assets/linkedin/linkedin-banner.png
  teaser: /assets/linkedin/linkedin-banner.png
---

Tax audits are expensive. Not just the settlement amounts — the decision cost. Every audit finding requires a judgment call: do you contest it, settle it, or absorb it? Each path has different legal costs, time costs, settlement risks, and precedent implications.

At Vertex, we had customers — Fortune 500 companies — managing dozens or hundreds of open audit findings simultaneously. Each one is a decision. And most of those decisions were being made by humans using spreadsheets, gut feel, and whoever had the most institutional memory in the room.

That bothered me.

## The problem with the existing approach

The data existed to make better decisions. We had historical audit outcomes, settlement amounts, contest success rates by jurisdiction, by audit type, by company size. We had legal cost data. We had time-to-resolution data.

But it was scattered. And the signal was buried in noise.

The threshold question — "at what ROI does it make sense to contest vs. settle?" — isn't static. It shifts based on jurisdiction, auditor, audit type, current legal precedent, and the company's own risk tolerance. What's the right threshold for a $10K finding in California vs. the same finding in Texas? For a sales tax audit vs. an income tax audit? For a company with a 3% tax controversy budget vs. one with a 0.3% budget?

Nobody had a good answer. Everyone had an opinion.

## What I built

A patent-pending decision-support model that takes a stream of audit findings, the historical record, and the company's own risk posture and outputs a per-finding recommendation: contest, settle, or absorb — with a confidence score and the key factors driving the recommendation.

The patent is still pending, so I can't go deep on how the engine works under the hood. Happy to talk through the technique under NDA. What I can say: the model is designed to keep its recommendations current as new outcomes flow in and as the underlying distribution shifts. Recommendations age. Stale recommendations are worse than no recommendation, and the system is built to know the difference.

## What changed when we deployed it

The first thing that changed wasn't accuracy. It was conversations.

Instead of "I think we should contest this," teams started saying "the model is recommending contest at 87% confidence — here's why, do we agree?" That's a different conversation. It has data in it. It has an auditable reasoning trail.

The second thing: the model started surfacing findings that were being systematically under-contested because of human bias toward certain jurisdictions. Nobody meant to do it. It was just a pattern in how decisions had been made historically. The model saw it because it didn't have the same blind spots the humans had.

That's what good decision support tooling should do. Not replace the judgment — augment it. Make the implicit explicit. Surface the patterns that are invisible when you're making 200 decisions one at a time.

---

*Audit Management decision-support model is patent pending. Developed at Vertex Inc., 2025.*
