---
title: "How Data Cake Got Built: Inventing Synthetic Tax Data From Scratch"
date: 2025-12-11
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

We needed training data for several ML models we were building in the Data and Insights value stream at Vertex. Tax transaction data. Lots of it. The real stuff: company names, jurisdictions, amounts, tax codes, ERP identifiers. The kind of data that, if it left the building in the wrong shape, would be a very bad day for a lot of people.

Legal said no to real customer data. Security said no to real customer data. The right answer was: no real customer data.

So we had a problem. You can't train a model on nothing. And synthetic data, if it doesn't look like real data, just teaches your model to recognize fake patterns.

## What we actually built

Data Cake is a service that learns the statistical fingerprint of real tax transaction data and generates synthetic records that are statistically indistinguishable from the real thing — but contain no actual customer information.

The synthetic records carry the same shape as production data: jurisdictions, SIC codes, company-size profiles, ERP systems, taxable amounts, tax rates, filing periods. The generator preserves the joint structure of those fields — the way a real industry constrains a real jurisdiction, the way company size shifts the amount distribution, the way certain combinations that look plausible on paper are legally impossible in practice. The constraints chain.

The patent is still pending, so I'm staying high-level on the generator itself. Happy to walk through the technique under NDA.

## What surprised me building it

Two things.

First: the hardest part wasn't the ML. It was figuring out what "realistic" meant in the context of tax data. Tax data has deeply weird distributions. Jurisdiction-level tax rules create hard floors and ceilings on amounts. Certain industries only appear in certain states. Some combinations that are statistically plausible are legally impossible. Getting the constraints right took more domain knowledge than model tuning.

Second: once it worked, the use cases exploded beyond what we originally intended. We built it for model training. But it immediately became useful for:

- Safe demo data for customer pilots
- Load testing with realistic data distributions
- Onboarding new engineers who needed to work with production-shaped data without touching production
- QA environments that had previously been either too small to be meaningful or too real to be safe

That's the thing about solving a hard, real problem well — the solution tends to have more surface area than you planned for.

The bigger outcome: ML projects at Vertex stopped being a regulatory negotiation. We could move from "is there a path to data?" to "what model do we want to train?" — which is the conversation engineers should be having in the first place.

## On the patent process

Filing a patent as an engineer at a company is a strange experience. You write a lot of words that sound like English but aren't quite. You spend time explaining, in excruciating detail, why something that feels obvious to you isn't actually obvious. (The bar for "non-obvious" in patent law is different from what engineers mean when we say something is clever.)

It's worth doing. Not because patents are the point — they're not — but because the process of writing a patent application forces you to articulate your invention precisely enough that someone else could implement it. That's a clarifying exercise. I'd recommend it for any engineer who's built something genuinely novel.

Data Cake is pending. So are the other three. Watch this space.
