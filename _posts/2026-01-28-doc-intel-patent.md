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

Doc Intel is a scoring system that measures how well a codebase's documentation actually matches the code it claims to describe. As the code evolves, Doc Intel continuously scores the health of the relationship between what the code *does* and what the docs *say it does*.

The output is a per-file, per-function score — plus aggregated health metrics at the module and repository level. It's not a linter. It's a signal. It tells you *where to look*, not just *that something is wrong*.

The patent is still pending, so I'm staying high-level on the mechanics. Happy to go into it under NDA.

## What teams did with it

The point wasn't a number on a dashboard. It was giving engineering teams a way to talk about documentation debt the same way they already talk about code coverage debt — quantifiable, tracked over time, integrated into the development workflow, brought up in PR review when it matters.

Nobody had noticed the drift accumulating on the pipelines we instrumented. The team was shipping. Velocity looked great. The docs had quietly fallen off the cliff, and the only person who would have known was the senior engineer who was about to go on parental leave.

The first internal team to run it had a senior engineer say "I had no idea it had gotten this bad." That's when I knew we'd built something real.

The shift it produced was simple: doc health stopped being an opinion. It became a number teams could see, trend, and own.

---

*Doc Intel is patent pending. Developed at Vertex Inc., 2025.*
