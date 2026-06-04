---
title: "Week Notes — June 4: Rebuilding the Fantasy Baseball AI"
date: 2026-06-04
categories:
  - Notes
  - Engineering
  - AI
tags:
  - dev log
  - react
  - fantasy-baseball
  - side project
excerpt: "The waiver recommender went quietly empty and never complained. Most of a week went into making the data pipeline stop lying — plus a real React front end and a model I left benched on purpose."
---

The waiver wire went empty and nothing complained about it.

That's the bug I hate most. My fantasy baseball AI — the thing I build on weekends to tell me who to start and which trade is a fleece — kept rendering a clean, confident, empty list of waiver targets. No error. No stack trace. A recommendation engine quietly recommending nothing.

The cause was dumb, the way these always are. The pipeline was writing to two places at once: a real database and a pile of CSV files left over from an earlier design. One job stopped writing the CSVs. The waiver code still read them. Empty file, empty list, no exception thrown. **A silent failure is worse than a loud one.** The loud one at least tells you to come look.

So most of the week went into ripping the CSVs out.

## One source of truth

The data path had thirteen spots where something read or wrote a CSV. It's now zero. Everything goes through the database, and I added a gate to the test suite that fails the build if a CSV ever creeps back in. That part matters more than the cleanup. A one-time fix that nothing enforces is a fix with an expiration date.

## The pipeline got honest about time

The nightly job that recomputes every lineup recommendation took seventy-seven minutes. This week it takes a hundred and nineteen seconds.

I'd love to tell you I found an elegant algorithm. I didn't. The job was running the full factor-analysis pass, then running most of it again a step later on the same data. I taught the second step to reuse what the first one already wrote. The fanciest optimization is usually noticing you're doing the work twice. That run now resolves 8,061 of 8,386 players to real projections instead of silently dropping the ones whose names don't match cleanly.

## Names are a terrible primary key

Match a player on his name and you're one accent or nickname away from dropping him silently. So the back half of the week moved the joins that feed recommendations off player names and onto stable IDs.

Underneath that was an older sin: a past identity bug had stamped three different fantasy teams onto one team ID. The repair is self-healing now — it overwrites the corrupted values from the authoritative roster instead of politely filling in the blanks, and coverage went from around ten percent to ninety. The nightly cron also stopped false-failing on "database is locked," which turned out to be three steps colliding with the midday stats scrape. The fix was a longer timeout. Patience, not cleverness.

## The front end is finally React

For a while the UI was server-rendered HTML held together by a Python framework I'd outgrown. It's now a real React app: twenty-eight pages covering rosters, trades, the waiver wire, draft prep, and live matchup projections, cold-loading in about a second and a half. The trade view has a proper evaluator; the roster page flags buy-low and sell-high targets off the skill-score percentiles.

I won't pretend a side project needed React. It didn't. But I wanted real client-side state and an honest API contract between the front and back ends, and I wanted my hands in the framework most of the people I interview with are using. Both things are true. I'll own it.

It also writes its own column now. A morning job drafts a weekly recap of the league — who's heating up, who you should be worried about — and the site serves it like any other page. The AI covering the league it also runs. That one makes me laugh.

## The model stayed benched

A couple of weeks ago I wrote here about the model's honest limits. This week I acted on it. There's a machine-learning ensemble in the codebase, fully built, and it loses: a plain blend of public projections and percentile skill scores beats it on the board. So it stays benched. Shipping the ML *because it's the ML* is exactly the trend-chasing I spend half my time talking other people out of, and it's a lot harder to take that advice when you're the one who wrote the losing model.

The boring projection that wins is the one in production.

More next week.
