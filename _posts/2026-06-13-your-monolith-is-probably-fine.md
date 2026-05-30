---
layout: post
title: "Your Monolith Is Probably Fine"
date: 2026-06-13
categories: [opinion]
tags: [architecture, decision-making, engineering-philosophy, hype-cycle]
excerpt: "Nobody has ever needed microservices. Plenty of people have needed what microservices happen to provide. The gap between those two sentences has cost more money than almost anything I've watched in 25 years."
header:
  image: /assets/headers/your-monolith-is-probably-fine.png
  og_image: /assets/headers/your-monolith-is-probably-fine.png
  teaser: /assets/headers/your-monolith-is-probably-fine.png
---

Nobody has ever needed microservices.

Plenty of people have needed what microservices happen to provide — independent deploys, team autonomy, a blast radius smaller than the whole company. Those are real problems with real solutions. But "we have a monolith" is not, by itself, one of those problems. The gap between "this is the trend" and "this is our problem" has cost more money than almost anything I've watched in 25 years of shipping software.

I've been doing this since Y2K was a genuine existential threat. I've sat through the whole parade. SOA was going to fix everything. Then it was an enterprise service bus, which mostly meant a very expensive place for messages to go and die. Then NoSQL, where a generation of teams threw away transactions they very much still needed because a conference talk told them relational was over. Then microservices. Now it's "agentic everything," and I say that as someone who builds agentic systems in production — the technology is real, and the way it's being sold is the same movie I've already seen six times.

The pattern never changes. A genuinely useful idea solves a real problem for a few companies operating at a scale most of us will never touch. It gets a name. The name gets a conference. The conference gets a hype cycle. And then it shows up in a planning meeting at a company with eight engineers and forty users, presented as a thing you *should* do, with no one in the room able to finish the sentence "...because right now we can't ___."

That blank is the whole job.

**If you can't fill in the blank with a specific pain you are feeling right now, you are buying a solution to someone else's problem.** And you'll pay for it in the currency that actually matters: the time of the people who have to operate the thing at 2 a.m.

I'm not anti-progress. I want to be clear about that, because skepticism gets misread as nostalgia and I have no interest in the old days. I've torn down plenty of monoliths. At Connect Your Care we took a monolithic J2EE system that ran the core business and pulled it apart into services, one bounded context at a time, and it helped drive an acquisition. (I wrote up the *how* of that separately — the slow, boring, never-break-production version.) But notice the order of operations. We had a specific, daily, measurable pain: one bad deploy could take the whole company's revenue down for a day, and every new feature took longer than the last. We didn't decompose because monoliths were uncool. We decomposed because *that* monolith, doing *that* job, had become the bottleneck. Same word, completely different situation from the next team's.

The boring truth is that a monolith you understand, that deploys reliably, that one or two people can hold in their heads, is one of the best architectures going. I've run pipelines doing 50 to 100 million transactions a day at sub-100ms p99, and the deciding factor was never how many repos we'd carved the thing into. It was whether the people on call understood what they were running. Distribution is a cost you pay for a benefit. If you don't need the benefit, you've just bought yourself a distributed system, which is to say you've turned every function call into a network call that can fail, lie, or arrive twice. Congratulations.

Here's the question I actually ask, and it's short enough to ask out loud in any meeting:

1. What can't we do today that this would let us do?
2. Who feels that pain, how often, and can they describe it without using the name of the technology?
3. If we do nothing for another six months, what specifically gets worse?

If the answers are vague — if they reach for "scalability" or "future-proofing" or "it's the industry standard" — that's not a yes. That's a trend wearing a requirement's clothes. The honest answer is sometimes "nothing gets worse, we just feel behind," and feeling behind is not an engineering problem. It's a marketing one, and it belongs to the people selling the conference, not to you.

I've led enough teams and cleaned up enough of these to have a strong prior: the most expensive decisions I've seen weren't the ones where someone picked the wrong tool. They were the ones where nobody could say what problem the tool was for, and everyone was too polite, or too worried about looking dated, to ask. So ask. Be the person who asks. It is the least glamorous and most valuable thing you can do in a planning meeting, and after a while people start asking it before you have to.

So, the next time someone tells you the monolith has to go: don't fight them. Just ask them to finish the sentence. Most of the time they can't, and you've both just saved a year.

More soon.
