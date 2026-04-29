---
title: "How Data Cake Got Built: Inventing Synthetic Tax Data From Scratch"
date: 2026-04-17
categories:
  - Engineering
  - AI
tags:
  - patents
  - synthetic data
  - machine learning
  - tax tech
excerpt: "The origin story of one of my patent-pending inventions — how a real problem with real stakes led to building a synthetic tax data generator using ML."
---

The problem started, like most good engineering problems, with something nobody wanted to touch.

We needed training data for several ML models we were building in the Data and Insights value stream at Vertex. Tax transaction data. Lots of it. The real stuff: company names, jurisdictions, amounts, tax codes, ERP identifiers. The kind of data that, if it left the building in the wrong shape, would be a very bad day for a lot of people.

Legal said no to real customer data. Security said no to real customer data. The right answer was: no real customer data.

So we had a problem. You can't train a model on nothing. And synthetic data, if it doesn't look like real data, just teaches your model to recognize fake patterns.

## What we actually built

Data Cake is an NLP service that learns the statistical properties of real tax transaction data and generates synthetic records that are statistically indistinguishable from the real thing — but contain no actual customer information.

The core is XGBoost for learning the distributions and scikit-learn for the feature engineering and pipeline. We capture things like: how often does a given SIC code appear with a given jurisdiction? What's the typical transaction amount range for a Fortune 500 manufacturing company vs. a regional retailer? What ERP systems cluster with what company sizes?

Then we sample from those learned distributions to generate new records that feel authentic. The synthetic records have the same statistical fingerprint as real data without any of the compliance risk.

## What surprised me building it

Two things.

First: the hardest part wasn't the ML. It was figuring out what "realistic" meant in the context of tax data. Tax data has deeply weird distributions. Jurisdiction-level tax rules create hard floors and ceilings on amounts. Certain industries only appear in certain states. Some combinations that are statistically plausible are legally impossible. Getting the constraints right took more domain knowledge than model tuning.

Second: once it worked, the use cases exploded beyond what we originally intended. We built it for model training. But it immediately became useful for:
- Safe demo data for customer pilots
- Load testing with realistic data distributions
- Onboarding new engineers who needed to work with production-shaped data without touching production
- QA environments that had previously been either too small to be meaningful or too real to be safe

That's the thing about solving a hard, real problem well — the solution tends to have more surface area than you planned for.

## On the patent process

Filing a patent as an engineer at a company is a strange experience. You write a lot of words that sound like English but aren't quite. You spend time explaining, in excruciating detail, why something that feels obvious to you isn't actually obvious. (The bar for "non-obvious" in patent law is different from what engineers mean when we say something is clever.)

It's worth doing. Not because patents are the point — they're not — but because the process of writing a patent application forces you to articulate your invention precisely enough that someone else could implement it. That's a clarifying exercise. I'd recommend it for any engineer who's built something genuinely novel.

Data Cake is pending. So are the other three. Watch this space.
