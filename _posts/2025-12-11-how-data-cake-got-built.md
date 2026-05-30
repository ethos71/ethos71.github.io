---
title: "How Data Cake Got Built: Inventing Synthetic Tax Data From Scratch"
date: 2025-12-11
noindex: true
categories:
  - Engineering
  - AI
tags:
  - patents
  - synthetic data
  - machine learning
  - tax tech
excerpt: "The origin story of one of my patent-pending inventions — how a real problem with real stakes led to a synthetic tax data generator."
header:
  image: /assets/linkedin/data-cake.png
  og_image: /assets/linkedin/data-cake.png
  teaser: /assets/linkedin/data-cake.png
---

The problem started, like most good engineering problems, with something nobody wanted to touch.

We needed training data for several ML models we were building in the Data and Insights value stream at Vertex. Tax transaction data, lots of it — the kind of data that, if it left the building in the wrong shape, would be a very bad day for a lot of people.

Legal and security both said no to real customer data, and they were right to. PII in a tax pipeline isn't a thing you negotiate.

So we had a problem. You can't train a model on nothing. And synthetic data that doesn't behave like the real thing just teaches your model to recognize fake patterns.

```mermaid
graph LR
    R[Real customer<br/>transactions] -.blocked.-> M[ML model<br/>training]
    L[Legal &<br/>security] -.no.-> R
    S[Synthetic<br/>training data] --> M
```
_Figure: the data-access problem the patent addresses._

## What we actually built

Data Cake is a patent-pending service that removes the training-data bottleneck for tax ML without any real customer data ever leaving its system of record. The patent is pending, so I'm staying high-level on the mechanism.

The outcome was the part that mattered. ML projects at Vertex stopped being a regulatory negotiation. We went from "is there a path to data?" to "what model do we want to train?" That's the conversation engineers should be having in the first place.

## What surprised me building it

Two things.

First: the hardest part wasn't the ML. It was the domain. Tax is a heavily constrained world, and getting the constraints right took more work than getting the model right. As with most things, the constraints are the product.

Second: once it worked, the use cases exploded beyond what we originally intended. We'd built it for model training. It immediately became useful for safe demo data in customer pilots, for load testing with realistic distributions, for onboarding new engineers who needed production-shaped data without touching production, and for QA environments that had previously been either too small to be meaningful or too real to be safe.

Solutions to hard problems usually have more surface area than the original problem did.

## On the patent process

Filing a patent as an engineer at a company is a strange experience. You write a lot of words that sound like English but aren't quite. You spend time explaining, in excruciating detail, why something that feels obvious to you isn't actually obvious. The bar for "non-obvious" in patent law is different from what engineers mean when we say something is clever.

It's worth doing. Not because patents are the point — they're not — but because the process of writing a patent application forces you to articulate your invention precisely enough that someone else could implement it. That's a clarifying exercise. I'd recommend it for any engineer who's built something genuinely novel.

Data Cake is pending. So are the other three.
