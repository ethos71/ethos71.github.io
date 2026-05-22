---
title: "Mort AI Nexus: Predicting Economic Nexus Before It Bites You"
date: 2026-01-14
categories:
  - Engineering
  - AI
tags:
  - patents
  - tax tech
  - nexus
  - machine learning
excerpt: "Nexus threshold violations cost companies $100K–$500K per state. Mort AI Nexus is my patent-pending model for forecasting when you're about to cross — before the state notice arrives."
header:
  image: /assets/linkedin/mort-ai-nexus.png
  og_image: /assets/linkedin/mort-ai-nexus.png
  teaser: /assets/linkedin/mort-ai-nexus.png
---

If you're not in tax technology, "nexus" might sound obscure. It isn't.

Nexus is the legal threshold that determines whether a business has sufficient presence in a state to owe sales tax there. Cross the threshold and you owe — retroactively, often with penalties.

After *South Dakota v. Wayfair* (2018), the Supreme Court expanded **economic nexus** to cover remote sales. Companies that never had a physical presence in a state suddenly discovered they'd been technically taxable there for years. Each state set its own threshold — typically $100K in revenue or 200 transactions per year ([here's the current state-by-state guide](https://www.salestaxinstitute.com/resources/economic-nexus-state-guide) from the Sales Tax Institute, if you want to see how spread out it is). Per-state exposure runs $100K–$500K.

The compliance machinery that exists to track this is mostly reactive. Tools watch your transaction volume by state and tell you when you're close to a threshold. That's defense with a short horizon.

The question that kept nagging me: **can you see it coming?**

## What the existing tools got wrong

Reactive monitoring works the way a smoke detector works. By the time it alarms, you already have a fire.

When a company crosses an economic nexus threshold, the obligation is immediate — but the discovery isn't. Most companies find out from a state notice arriving months after the crossing, with penalties and interest already attached. That gap between *event* and *discovery* is where the financial exposure lives.

The problem isn't visibility into current transactions. Companies have that. The problem is the **forward signal** — whether you're going to cross the threshold in a given state, weeks before the transaction volume itself tells you.

If you can read the leading signals well enough, you can see the crossing coming.

## What Mort AI Nexus does

Mort AI Nexus is a predictive model that forecasts threshold crossings on a state-by-state, horizon-by-horizon basis. The output is a probability of crossing each state's threshold within a forward window, with the contributing factors ranked. A compliance team using it sees something closer to *"Texas is likely to cross in the next several weeks; here's what's driving it."* — in time to do something about it.

The patent is still pending, so I'm staying high-level on what goes into the forecast and how the model weighs it. Happy to go deeper under NDA.

That's a different conversation than the one tax teams have today. It's actionable. It happens in time to act.

## What we measured

We backtested against historical nexus violations that had already occurred. The model would have flagged a meaningful majority of them well in advance of the actual crossing — enough lead time to register, configure, and brief the business before the obligation hit.

The bigger shift wasn't the accuracy number. It was the change in posture. Tax teams running Mort AI Nexus stopped scrambling to retroactively file and started planning ahead. Registration, calculation configuration, internal briefings — all of it could happen in time. The companies that adopted it shifted from defensive compliance to proactive compliance.

## What it's actually useful for

Beyond the prediction itself, the model's most valuable surface is **planning**.

Tax compliance teams now had real lead time on which states were likely to become nexus states. That's enough time to:

- Register with the state proactively
- Configure tax calculation in the right systems
- Brief finance, legal, and ops on the new obligation
- Avoid penalties entirely instead of scrambling to mitigate them

Instead of finding out from a state notice, they were finding out from the platform — weeks before the line.

That's the bar I think compliance tooling should aim for. Not "we'll tell you when you've broken the rule." Rather, "we'll tell you when you're going to."

---

*Mort AI Nexus is patent pending. Developed at Vertex Inc., 2025–2026.*
