---
layout: post
title: "Forget the Thunderdome"
date: 2026-07-13
categories: [opinion]
tags: [job-search, open-source, ai, mcp, hiring-without-whiteboards]
excerpt: "Twenty-five years in, and the first thing the market handed me was a CoderPad link. So I stopped grinding and built the tool that ran my search instead. It's free now."
header:
  image: /assets/headers/forget-the-thunderdome.png
  og_image: /assets/headers/forget-the-thunderdome.png
  teaser: /assets/headers/forget-the-thunderdome.png
---

In May, after four years as a principal engineer at Vertex, I got laid off. Twenty-five years into this career, and the first thing the market handed me was a CoderPad link.

I want to be honest about how that feels. I've shipped pipelines that clear a hundred million transactions a day at sub-100ms p99. I've torn down monoliths without taking the business down with them, held four patent-pending AI inventions, taught fifty engineers how to build with LLMs. And the front door at company after company is a timed puzzle about inverting a binary tree — or worse, a chat with an AI screener that decides whether a human ever reads my name.

I wasn't going to out-grind a 24-year-old with three free months and every LeetCode pattern fresh in memory. So I stopped playing that game and built a different one.

The problem was never finding jobs. Job boards are full of postings that are expired, syndicated copies of syndicated copies, or ghosts kept alive for pipeline optics. The first thing I learned automating my own search: an HTTP 200 tells you the server is up. It tells you nothing about whether the job is real. So that became the first rule baked into the tool — validate a posting by reading it, never by its status code. The rule earned its keep in week one, on a listing that returned a clean 200 and had been dead for two months, still quietly collecting applications into a void. The machine reads the page, sees it's gone, and moves on. I didn't burn an afternoon writing a cover letter for a ghost.

The second thing I learned: the companies I actually wanted — the ones that interview engineers by talking to them about engineering — are findable. The hiring-without-whiteboards movement keeps a literal list. Greenhouse postings can be validated. Recruiter-sourced leads skip the cattle call entirely. You can target all of this. Most people don't, because doing it by hand is a part-time job on top of the job you're trying to get. So I made it the machine's job.

What came out of that is a small kit. A scraper and discovery pipeline that finds roles and scores them. A SQLite tracker that holds the whole pipeline on my own laptop — no SaaS, no living in someone else's database. A Gmail sync that reads recruiter email and sorts it into interview, offer, rejection. A cover-letter generator driven by a profile config, so every letter is grounded in my actual record instead of a template. A dashboard so I always knew who owed me a reply and who I owed one.

The part I care about most is that I wired the pieces so an agent could drive them — and not as a demo, but on my actual search. For a month, Claude and I ran the loop together: it discovered, validated, scored, and drafted; I decided. I'll be precise about how that works today, because the shipped repo is precise about it: the agent runs through the command line, calling the same commands I would. Native MCP endpoints — so any agent can wire in without shell access — are half-built and half-roadmap. I'd rather tell you that than sell you the finished version of a thing that's still cooking.

Here's how the search actually went. Eighty-six companies applied to. Twenty-nine that put me in front of an engineer instead of a screener bot. Four offers. I'm joining Verint as a senior engineer. I'm keeping the money out of this post, but the shape of it is the whole argument: the good doors are there, and you can find them without stepping into the dome.

So I'm giving the tool away. **The gauntlet is a filter that selects for free time, not for engineering ability** — and once you've said that out loud, it's hard to keep defending it. Every laid-off senior engineer staring down their first CoderPad in a decade deserves a better option than grinding nights against kids with nothing else on their plate. And the most honest argument against a broken process is a working alternative you can hand someone.

The repo is [github.com/ethos71/forget-the-thunderdome](https://github.com/ethos71/forget-the-thunderdome), MIT licensed. Clone it, fill in one YAML file with who you are and what you want, and run your own loop from the command line. Your data never leaves your machine — the pipeline is a SQLite file, the email token stays local, the profile is never committed.

I'm not going to pretend I fixed hiring. I found a better door by building one, and the thing that opened it is on GitHub now, yours to take. If you're a senior engineer tired of proving you can invert a binary tree for the four-hundredth time — you don't need the dome.
