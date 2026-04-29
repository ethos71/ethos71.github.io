---
title: "Why I Built a Self-Balancing Tree to Make Audit Defense Decisions"
date: 2025-10-22
categories:
  - Engineering
  - AI
tags:
  - patents
  - algorithms
  - tax tech
  - audit
excerpt: "The Audit Management Red Black Tree Timber Model started as a question: why are we making $50K decisions based on gut feel when we have the data to do better?"
---

Tax audits are expensive. Not just the settlement amounts — the decision cost. Every audit finding requires a judgment call: do you contest it, settle it, or absorb it? Each path has different legal costs, time costs, settlement risks, and precedent implications.

At Vertex, we had customers — Fortune 500 companies — managing dozens or hundreds of open audit findings simultaneously. Each one is a decision. And most of those decisions were being made by humans using spreadsheets, gut feel, and whoever had the most institutional memory in the room.

That bothered me.

## The problem with the existing approach

The data existed to make better decisions. We had historical audit outcomes, settlement amounts, contest success rates by jurisdiction, by audit type, by company size. We had legal cost data. We had time-to-resolution data.

But it was scattered. And the signal was buried in noise.

The threshold question — "at what ROI does it make sense to contest vs. settle?" — isn't static. It shifts based on jurisdiction, auditor, audit type, current legal precedent, and the company's own risk tolerance. What's the right threshold for a $10K finding in California vs. the same finding in Texas? For a sales tax audit vs. an income tax audit? For a company with a 3% tax controversy budget vs. one with a 0.3% budget?

Nobody had a good answer. Everyone had an opinion.

## Why a Red Black Tree

The Audit Management Red Black Tree Timber Model uses a self-balancing binary search tree to maintain and query ROI threshold recommendations in real time as new audit data flows in.

Here's the intuition: you're constantly inserting new data points — new outcomes, new settlements, new contest results. You need to query threshold recommendations fast. And the tree needs to stay balanced as the data distribution shifts, otherwise your query performance degrades and, more importantly, your recommendations skew toward stale data.

A red-black tree gives you O(log n) insert and query with guaranteed balance. The "Timber" part of the name refers to the model's ability to prune branches — historical data that no longer reflects current conditions gets rotated out of the active tree as the model detects distribution shift.

The output is a per-finding recommendation: contest, settle, or absorb — with a confidence score and the key factors driving the recommendation.

## What changed when we deployed it

The first thing that changed wasn't accuracy. It was conversations.

Instead of "I think we should contest this," teams started saying "the model is recommending contest at 87% confidence — here's why, do we agree?" That's a different conversation. It has data in it. It has an auditable reasoning trail.

The second thing: the model started surfacing findings that were being systematically under-contested because of human bias toward certain jurisdictions. Nobody meant to do it. It was just a pattern in how decisions had been made historically. The model saw it because it didn't have the same blind spots the humans had.

That's what good decision support tooling should do. Not replace the judgment — augment it. Make the implicit explicit. Surface the patterns that are invisible when you're making 200 decisions one at a time.

---

*Audit Management Red Black Tree Timber Model is patent pending. Developed at Vertex Inc., 2025.*
