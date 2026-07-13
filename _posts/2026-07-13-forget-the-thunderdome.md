---
title: "Forget the Thunderdome"
date: 2026-07-13
categories: [opinion]
tags: [job-search, open-source, ai, mcp, hiring-without-whiteboards]
excerpt: "Twenty-five years in, and the first thing the market handed me was a CoderPad link. So I stopped grinding and built the tool that ran my search instead. It's free now."
---

Somebody at Vertex once asked me, straight-faced, what the responsibilities of a Principal Engineer were. I told them the truth: I'm the janitor. I clean up everyone else's mess. Four years, and that was more or less the job.

The mess was almost never mine. A reporting need a competent team solves in-house in a quarter became a bloated BI platform nobody wanted — point-and-click, drowning in features our customers never asked for. Nobody wanted the pie charts. The one thing we actually needed, reliable automated testing of our reports, it flatly couldn't do, so we tested by hand forever and that sinkhole landed on my desk to babysit. I sat across from "architects" who couldn't define a cloud primitive if you spotted them the first three letters — one turned in his big contribution as three boxes on a slide: UI, API, database. That was the deliverable. And the process theater on top of it: I was once ordered to hand-triage thousands of Snyk findings just to *estimate* how long fixing them would take — an exercise that took longer than the fixes. Ninety-nine percent were one-line version bumps. That's not rigor. That's a burndown chart cosplaying as engineering.

Here's the part that actually matters, though. Every one of my four patent-pending inventions started with someone above me saying "don't do that." Every one. I built them anyway, on my own time, and walked them to legal myself. Legal took one look and wanted to move fast to lock them down — and *then*, suddenly, the same people who'd waved the ideas off found the time of day. If I'd listened to my "bosses," I'd have exactly zero patents to my name. The lesson stuck: when you know the work is right, you stop asking the room for permission. You route around it and build the thing.

I bring all that up because it's the whole reason this story ends well. In May 2026, that same company laid me off. Twenty-five years into this career, and the first thing the market handed me was a CoderPad link.

I want to be clear about what that feels like. I've shipped pipelines that clear a hundred million transactions a day. I've torn down monoliths without taking the business down with them, held four patents pending, taught fifty engineers how to build with LLMs. And the front door at company after company is a timed puzzle about inverting a binary tree — or worse, a chat with an AI screener that decides whether a human ever reads my name. I wasn't going to out-grind a 24-year-old with three free months and every LeetCode pattern fresh in memory.

So I did the only thing I know how to do with a broken process. I routed around it and built something that worked.

## The problem was never finding jobs

It was finding the right doors. Job boards are full of postings that are expired, syndicated copies of syndicated copies, or ghosts kept alive for pipeline optics. The first thing I learned automating my own search: an HTTP 200 tells you the server is up. It tells you nothing about whether the job is real. So that became the first rule baked into the tool — validate a posting by reading it, never by its status code. The rule earned its keep in week one, on a listing that returned a clean 200 and had been dead for two months, still quietly collecting applications into a void. The machine reads the page, sees it's gone, and moves on. I didn't burn an afternoon writing a cover letter for a ghost.

The second thing I learned: the companies I actually wanted — the ones that interview engineers by talking to them about engineering — are findable. The hiring-without-whiteboards movement keeps a literal list. Greenhouse postings can be validated. Recruiter-sourced leads skip the cattle call entirely. You can target all of it. Most people don't, because doing it by hand is a part-time job on top of the job you're trying to get. So I made it the machine's job.

## What I built

A scraper and discovery pipeline that finds roles and scores them. A SQLite tracker that holds the whole pipeline on my own laptop — no SaaS, no living in someone else's database. A Gmail sync that reads recruiter email and sorts it into interview, offer, rejection. A cover-letter generator driven by a profile config, so every letter is grounded in my actual record instead of a template. A dashboard so I always knew who owed me a reply and who I owed one.

The part I care about most is that I wired the pieces so an agent could drive them — and not as a demo, but on my actual search. For a month, Claude and I ran the loop together: it discovered, validated, scored, and drafted; I decided. I'll be precise about how that works today, because the shipped repo is precise about it: the agent runs through the command line, calling the same commands I would. Native MCP endpoints — so any agent can wire in without shell access — are half-built, half-roadmap. I'd rather tell you that than sell you the finished version of a thing that's still cooking.

## How it went

Eighty-six companies applied to. Twenty-nine that put me in front of an engineer instead of a screener bot. Four offers. I'm joining Verint as a senior engineer. I'm keeping the money out of this post, but the shape of it is the whole argument: the good doors are there, and you can find them without ever stepping into the dome.

## Why I'm giving it away

The gauntlet is a filter that selects for free time, not for engineering ability — and once you've said that out loud, it's hard to keep defending it. Every laid-off senior engineer staring down their first CoderPad in a decade deserves a better option than grinding nights against kids with nothing else on their plate. And the most honest argument against a broken process is a working alternative you can hand someone.

The repo is [github.com/ethos71/forget-the-thunderdome](https://github.com/ethos71/forget-the-thunderdome), MIT licensed. Clone it, fill in one YAML file with who you are and what you want, and run your own loop from the command line. Your data never leaves your machine — the pipeline is a SQLite file, the email token stays local, the profile is never committed.

I'm not going to pretend I fixed hiring. I found a better door by building one, and the thing that opened it is on GitHub now, yours to take. If you're a senior engineer tired of proving you can invert a binary tree for the four-hundredth time — you don't need the dome.
