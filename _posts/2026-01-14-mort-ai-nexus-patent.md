---
title: "Mort AI: Predicting Nexus Before It Bites You"
date: 2026-01-14
categories:
  - Engineering
  - AI
tags:
  - patents
  - tax tech
  - nexus
  - machine learning
excerpt: "Nexus threshold violations cost companies millions. The Mort AI Nexus Weather Economic Model predicts when you're about to cross — using economic indicators and weather patterns as leading signals."
---

If you're not in tax technology, "nexus" might sound obscure. It isn't. Nexus is the legal threshold that determines whether a business has sufficient presence in a state to owe taxes there. Cross the threshold, and you owe — retroactively, often with penalties.

After *South Dakota v. Wayfair* (2018), the Supreme Court expanded economic nexus to cover remote sales. Companies that never had a physical presence in a state suddenly discovered they'd been technically taxable there for years. The compliance exposure was enormous.

The question that nagged me: **can you see it coming?**

## What the existing tools got wrong

Most nexus monitoring tools are reactive. They watch your current transaction volume by state and alert you when you're close to a threshold. That's useful, but it's playing defense with a short horizon.

The problem is that nexus isn't just about what you sold last month. For mortgage-related nexus — which is what the Mort AI model specifically targets — the thresholds are influenced by things that happen *before* the transactions. Economic conditions. Regional housing market activity. Seasonal patterns. Migration trends.

A mortgage company's nexus exposure in a state is partly a function of what's happening in that state's economy and housing market *right now*. By the time the transactions show up in your ledger, you may already be past the threshold.

## The weather signal

The weather component is the one that gets the most questions, so let me address it directly.

Weather is a legitimate leading indicator for mortgage nexus because it correlates with regional housing market activity, which drives mortgage origination volume by geography. Cold winters in northern states correlate with suppressed spring buying seasons. Severe weather events affect property values, insurance costs, and ultimately transaction volumes in ways that lead the nexus exposure by weeks.

We're not predicting nexus from the weather. We're using weather-correlated economic signals as one input in a broader model that also includes housing price indices, employment data, migration patterns, and the company's own historical transaction trajectory.

The output is a state-by-state nexus risk forecast: probability of crossing threshold by horizon (30, 60, 90 days), with the driving factors ranked by contribution.

## What it's actually useful for

Beyond the prediction itself, the model is most valuable for **planning**.

Tax compliance teams can see 60–90 days out which states are likely to become nexus states. That's enough time to actually prepare — register with the state, set up the right tax calculations, brief the finance team. Instead of scrambling to retroactively file and pay penalties, you're walking in the front door.

We tested it against historical data first — backtesting against known nexus violations that had already occurred. It would have flagged 74% of them with a 45+ day warning window. That's not perfect. But it's dramatically better than finding out after the audit.

## The name

Mort is short for mortgage. The AI is the AI. The Nexus is the nexus. The Weather Economic Model is the model.

It's not the most elegant name. But it's accurate. And in patent applications, accuracy matters more than elegance.

---

*Mort AI Nexus Weather Economic Model is patent pending. Developed at Vertex Inc., 2025–2026.*
