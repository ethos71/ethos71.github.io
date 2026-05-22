---
title: "Doc Intel: What Happens When Your Code and Docs Divorce"
date: 2026-01-28
categories:
  - Engineering
  - AI
tags:
  - patents
  - developer tooling
  - documentation
  - code quality
excerpt: "Documentation rot is the silent killer of engineering velocity. Doc Intel is my patent-pending system for detecting when your code and docs have gone their separate ways."
header:
  og_image: /assets/linkedin/linkedin-banner.png
  teaser: /assets/linkedin/linkedin-banner.png
---

Every engineering team I've ever been on has the same lie.

It's usually written on a README somewhere. Or in Confluence. Or in a comment block at the top of a service nobody touches anymore. It says what the system does. It was accurate once. But that was two sprints ago, and three engineers have since pushed changes without updating the docs because — let's be honest — nobody updates the docs.

Documentation rot is not a discipline problem. It's a systems problem. And I got tired of it.

## The problem in concrete terms

At Vertex, we had large, complex data pipelines. Tax calculation engines. Audit defense tooling. Systems that processed 50–100 million transactions a day for Fortune 500 clients. And we had documentation — internal wikis, inline comments, architectural decision records, README files.

The documentation was never actively wrong. It was *drifted*. Subtly out of sync in ways that were expensive to discover. A new engineer would read the docs, build a mental model, then spend two days confused before a senior engineer said "oh yeah, that changed about six months ago."

That's not a documentation problem. That's a confidence problem. The docs existed — you just couldn't trust them.

## What Doc Intel does

Doc Intel is a confidence scoring system that measures the degree of drift between source code and its documentation. As code evolves over time, Doc Intel continuously scores the health of the relationship between what the code *does* and what the docs *say it does*.

It looks at things like:
- Function signatures vs. their docstrings — are the parameters still accurate?
- Module-level descriptions vs. actual exported behavior
- Inline comments that reference conditions or logic that no longer exists
- API contracts described in docs vs. the actual current interface

The output is a per-file, per-function confidence score — plus aggregated health metrics at the module and repository level. It's not a linter. It's a signal. It tells you *where to look*, not just *that something is wrong*.

## Why I think this is worth a patent

The insight wasn't "compare code to docs." Tools have been trying that forever with varying success.

The insight was **confidence over time**. A doc that was accurate yesterday and slightly less accurate today has a different risk profile than a doc that hasn't been touched in two years and the code it describes has been rewritten three times. The trajectory matters. The rate of drift matters.

Here's what that drift looked like in one of the pipelines we instrumented — six months of activity on a single service:

**Code-vs-doc drift over six months**

| Month | Code commits | Doc commits | Drift ratio |
|---|---:|---:|---:|
| Month 1 | 42 | 14 | 3.0x |
| Month 2 | 51 | 12 | 4.2x |
| Month 3 | 67 | 9  | 7.4x |
| Month 4 | 58 | 6  | 9.7x |
| Month 5 | 74 | 4  | 18.5x |
| Month 6 | 81 | 3  | 27.0x |

Nobody noticed it happening. The team was shipping. Velocity looked great. The docs just quietly fell off the cliff. By month six, the README's mental model and the running service shared almost no overlap — and the only person who would have known was the senior engineer who was about to go on parental leave.


We built it so teams could surface documentation debt the same way they surface code coverage debt — as a quantifiable metric, tracked over time, integrated into the development workflow.

The first internal team to use it had a senior engineer say "I had no idea it had gotten this bad." That's when I knew we'd built something real.

---

*Doc Intel is patent pending. Developed at Vertex Inc., 2025.*
