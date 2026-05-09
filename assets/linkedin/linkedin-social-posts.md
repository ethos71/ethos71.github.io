# LinkedIn Social Posts — Ready to Publish

Five posts, one per project. Each fits inside LinkedIn's character budget (no truncation in feed).
Pair each post with the matching infographic in `assets/linkedin/*.png`.

Posting cadence: one per week for 5 weeks. Tuesday or Wednesday morning, 8–10am ET, drives the highest senior-engineer engagement on LinkedIn.

---

## POST 1 — Robby (Multi-Agent SDLC)

**Image to attach:** `robby.png`

```
The "super chicken" problem is real.

Researchers studied flocks of chickens to find what made the most productive ones, then bred the highest individual producers together. Generation after generation of super chickens.

The result wasn't a super-productive super flock.
Most of the chickens were dead.
The super chickens had pecked the others to death.

I built Robby because I think Margaret Heffernan was right about teams — and I think AI can finally do something about it.

Robby is a multi-agent SDLC orchestrator I built and shipped at Vertex.

→ 70 skills
→ 15 specialized roles (architect, engineer, test, security, UX, PM, docs, …)
→ MCP-integrated with ArgoCD, GitHub Actions, Datadog
→ The running code is the source of truth — not the Jira board, not the Confluence doc

Robby is a head chef. Each role is a specialist. None of them tries to do everything.

Adopted across multiple teams. ~50 engineers trained on it through the "AI Curiosity Workshop" we ran in parallel.

The bet: an AI orchestrator can do the routing, so humans can do the work they actually love.

Full case study + how it's structured: https://ethos71.github.io/2026/02/19/robby-ai-sdlc-system.html

#AI #MultiAgent #Engineering #Leadership
```

---

## POST 2 — Mort AI Nexus (Patent Pending)

**Image to attach:** `mort-ai-nexus.png`

```
The 2018 Wayfair ruling broke sales tax compliance for every company doing business across state lines.

50 states. 50 different thresholds. Most companies discover they've crossed one when a state notice arrives — months later, with penalties stacked on top.

Per-state exposure: $100K–$500K.

I invented Mort AI Nexus to flip the discovery model. Patent pending.

→ Real-time transaction monitoring across 50 jurisdictional rule sets
→ Predicts approaching thresholds before you cross them
→ Triggers proactive registration workflows weeks ahead of the line
→ Pattern analysis informed by Wayfair + per-state nexus rules
→ Self-improves from confirmed crossings

The shift wasn't accuracy.
It was timing.

Customers stopped finding out about nexus exposure from state notices.
They started finding out from the platform.

Java, Spring Boot, AWS, real-time streaming, ML pattern analysis.

The patent story: https://ethos71.github.io/2026/01/14/mort-ai-nexus-patent.html

#TaxTech #AI #Patents #IndirectTax
```

---

## POST 3 — Voice Biometric at JPMorgan Chase

**Image to attach:** `voice-bio.png`

```
Knowledge-based authentication is broken.

Mother's maiden name. Last four of SSN. Birth city. Years of database breaches have handed the answers to attackers, and call centers became the soft underbelly of retail banking.

In 2018 I led development on JPMorgan Chase's voice biometric fingerprinting service.

The premise: customers authenticate by talking naturally during the call. No passphrase. The rep sees a confidence score before granting access.

Numbers from the first 90 days:

→ ~10 million JPMC accounts opted in
→ ~1,300 customers opted out
→ 20 seconds saved per authenticated call
→ 25 more customers serviced per rep per day
→ ~$830B in industry-wide fraud loss plateau across the cohort

The fraud-prevention math mattered. The customer-experience math is what made it stick.

Voice bio wasn't a security tool customers tolerated.
It was a security tool that made their day better.

That's the bar for production security UX, and it's the bar I take into every authentication problem I touch now.

Python · ML · biometrics · Sapiens rules engine · Angular dashboard

#Fintech #Authentication #Biometrics #FraudPrevention
```

---

## POST 4 — Data Cake (Patent Pending)

**Image to attach:** `data-cake.png`

```
You can't train tax AI on real customer transactions.

Regulated. Contractual. PII-bound. Every conversation about model training at a tax-tech company eventually hits the same wall: Legal says no.

So I invented Data Cake. Patent pending.

→ NLP service that learns the statistical properties of real tax data
→ Generates synthetic transactions that match those distributions
→ Deterministic rules engine enforces tax-law constraints (every synthetic transaction is a valid transaction)
→ No PII. No traceable link to real customers.

Models trained on Data Cake-generated data performed within 2% of models trained on real customer data.
Without ever touching real customer data.

What changed: model training stopped being a regulatory negotiation. New tax ML projects spin up in days instead of quarters.

Some bottlenecks aren't technical. They're contractual. The right architecture move is sometimes finding the path through the contracts, not around them.

Python · XGBoost · scikit-learn · NLP · rules engine

How it got built: https://ethos71.github.io/2025/12/11/how-data-cake-got-built.html

#AI #SyntheticData #MLEngineering #Patents
```

---

## POST 5 — Connect Your Care Decomposition

**Image to attach:** `connect-your-care.png`

```
The standard advice for a decade-old monolith is rip-and-replace.
The standard outcome is a multi-year project that ships nothing.

We didn't do that at Connect Your Care.

The HRCommand benefits-administration platform was a J2EE monolith on WebLogic, built up across 8+ years. It worked. It served customers. It also blocked every strategic initiative the company wanted to ship.

I led the architecture and I made one bet: strangler fig, not rewrite.

→ Identify bounded contexts inside the monolith
→ Build each one as a Spring Boot microservice
→ Route live traffic through a thin proxy with monolith fallback
→ Validate for two weeks
→ Peel the bounded context off the monolith
→ Repeat

Five-person team.
Never broke production.
Never took the platform down for a release.
Shipped new product surfaces on top of the new architecture along the way.

In 2021, United Health / Optum Financial acquired Connect Your Care.
The architecture work was a direct contributor to the acquisition thesis.

If you have a stable, profitable platform that needs to be modernized — and you can't break it — strangler fig is almost always the right call. Rip-and-replace looks bold and fails quietly.

Spring Boot · J2EE · WebLogic · React · Kubernetes · Figma-to-code

#Architecture #Engineering #Leadership #Microservices
```

---

## Posting tactics

- **Time:** Tuesday or Wednesday, 8–10am ET. Senior-engineer engagement peaks here.
- **Cadence:** One per week. Don't bunch them.
- **First-comment trick:** Drop the blog post link as a first comment instead of in the post body. LinkedIn deboosts external links in the post itself.
- **Tag:** No company tags (no @Vertex, no @JPMC) — those trigger compliance reviews you don't need. Hashtags are fine.
- **Reply to comments within the first hour.** That's the engagement signal LinkedIn weights.
- **If someone asks "how would this apply to X?" — answer at length. Long, technical replies become content of their own.**

## Reposting from this set

When all five are out, you have a content series. Title it: "Five Systems I Shipped." Pin the introductory blog post to your LinkedIn profile featured section. Use it as your conversation opener with recruiters.
