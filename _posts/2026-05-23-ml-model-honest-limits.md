---
title: "How I Built an ML Model That Knows Its Own Limits"
date: 2026-05-23
categories:
  - Engineering
  - AI
tags:
  - ml
  - xgboost
  - modeling
  - overfitting
  - fantasy-baseball
excerpt: "Train MAE 1.765. Test MAE 3.079. That gap is not a bug to hide — it's the whole point of the post. A model that knows what it doesn't know is more useful than one that pretends."
header:
  og_image: /assets/linkedin/linkedin-banner.png
  teaser: /assets/linkedin/linkedin-banner.png
---

The most useful number in the model I'm about to describe is the gap between two other numbers.

**Training MAE: 1.765 fantasy points. Test MAE: 3.079 fantasy points.**

If you've been around ML, you already know what that gap means. The model fits its training data tighter than it fits the world. It's overfit. The interesting question isn't whether overfitting is happening — it almost always is. The interesting question is: do you know it's happening, and can you explain why?

Most of the production "AI" I see in the wild can't.

## What I built

A daily player-performance predictor for fantasy baseball. XGBoost regression. The target: how many fantasy points a given MLB batter will score the next day. Scoring is the standard rotisserie shape — hits, doubles, triples, home runs, runs, RBIs, stolen bases, walks. About 150 batters in play on any given day.

The training data: 2,300+ real game logs from April 2026, engineered into 10 features per player-day:

- Rolling averages at 5, 10, and 20-game windows (trend detection)
- Standard deviations across the same windows (volatility)
- Trend deltas — recent average minus long-term average (momentum)
- Binary indicators for hot/cold streaks (categorical pattern)

Ten features. Hand-crafted. Domain-informed. That last part matters more than the algorithm choice.

## Why XGBoost

I'm not religious about XGBoost. I picked it for four boring reasons.

1. It handles mixed feature types without preprocessing gymnastics.
2. 200 trees train in seconds on a laptop.
3. Feature importance falls out of the model — I can tell you which inputs the model leaned on.
4. It is interpretable. I can sit a non-engineer down and walk them through why a prediction is what it is.

Neural networks would not have helped me here. 4,800 raw samples is not enough data to make a deep architecture stable. And the day someone asks "why did your model say 6 points?", "the gradients converged" is not an answer that survives the room.

## The validation choice that mattered

Here's where most fantasy-sports ML projects go wrong: they random-split their train/test data.

Random splits look great in notebooks and lie about reality. If your model is trained on data from May 15 and tested on data from April 20, you've leaked the future into the past. The reported accuracy is fiction. A model that has to actually predict tomorrow doesn't get to peek at next month.

So I did temporal validation. **Train on April 1–25. Test on April 25–May 2.** No shuffling. The test set is strictly later than the training set, the same way the deployed model would have to operate.

This is the choice that produced the train/test MAE gap. A random split would have hidden it. The discipline cost me the comfortable number and gave me the honest one.

## What the honest number means

Training MAE 1.765 says the model learned the patterns in the April training window. Test MAE 3.079 says the patterns don't fully generalize a week forward.

Why doesn't it generalize? Because my features are entirely about *the player*. They say nothing about:

- Who the player is facing (pitcher handedness, strength, ERA allowed)
- External factors (weather, rest, lineup position)
- Interaction effects (a hot hitter against a weak pitcher is a different distribution from a hot hitter against an ace)

About 40% of predictions land within ±2 FP — useful for relative ranking. But the worst errors are 15+ FP, and they cluster in exactly the games my features can't see: a slumping batter explodes against a Triple-A call-up. Of course my model missed it. It didn't know the Triple-A call-up was on the mound.

This is the 80/20 rule of ML stated plainly: 80% of accuracy comes from domain features, 20% from algorithm choice. Most teams I've seen invert that ratio and wonder why their pipeline doesn't get better in production.

## What I'd ship — and what I wouldn't

I would not ship this model as autonomous predictions. Not yet. What I would ship is the model *as a tool an analyst uses* — paired with Vegas lines, FanGraphs projections, and somebody who knows that Ohtani isn't on waivers no matter what the database says.

The next iteration adds opponent ERA/OPS-allowed, pitcher handedness matchups, and rest days. I expect that to close the train/test gap and beat the FanGraphs baseline that this version currently underperforms by about 10%. After that: weekly retrains, drift monitoring on prediction MAE, and an A/B against the baseline on real seasonal data.

## The point

I've sat in too many rooms where someone presented a 99% accurate model that was 99% leaked. The hardest skill in production ML is not improving the model. It's knowing — and saying out loud — what the model doesn't know.

A train/test gap on the slide is not a flaw. It's a tell that the engineer did the work.

Build carefully. Ship it anyway.
