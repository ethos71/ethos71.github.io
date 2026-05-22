# TODO

What **you** need to do with @dom from week to week and feature to
feature. Things @dom is doing on its own don't go here; only things
that need your decision, your brief, or your eyes.

Conventions: 🔴 this week, 🟡 next, 🟢 someday. Check off when done.

---

## 🔴 This Week

### Review the 4 new case-study posts (drafted 2026-05-22, dated forward)
- [ ] `_posts/2026-05-23-ml-model-honest-limits.md` — XGBoost / fantasy baseball
- [ ] `_posts/2026-05-30-voice-biometric-fraud.md` — **verify these details from memory:** "TARA Fraud Busters" team name, "Sapiens" rules engine, "$2.4B industry call-center fraud exposure", "20–40% adoption ceiling on opt-in security features." Each is plausible but not in `~/workspace/job/` source files. Confirm or soften.
- [ ] `_posts/2026-06-06-strangler-fig-modernization.md` — **verify:** "WebLogic" application server, "Puppet" infrastructure mgmt. J2EE/EJB → Spring Boot is sourced; these two stack details aren't.
- [ ] `_posts/2026-06-13-five-patents-four-years.md` — **structural question:** PATENTS.md counts the 5 as Data Cake + Doc Intel + Audit Mgmt + Red-Black Tree + AI Nexus, treating Robby as the framework that spawned 4 of them. Post conflates Audit Mgmt + RBT into one and lists Robby as the 5th. This matches existing blog convention but contradicts the @job source ledger. Decide which framing wins.

### Review the first weekly post (`_posts/2026-05-18-week-notes-toolkit-week.md`)
- [ ] Job-search framing ("between roles, deliberate about fit") — confirm tone or rewrite
- [ ] Kid stays as "my son / my kid" — say the word if his name goes in next week
- [ ] Closing sign-off "More next week." — lock in or change
- [ ] Anything in the post that should be private (especially `nyx-crm`, client work)

### Friday-ish brief (every week)
- [ ] Drop a few sentences before I write: family stuff, kid's Challenger week, work moments that matter
- [ ] Anything from your wife you want included — paste it here (I cannot access Facebook)

---

## 🟡 Feature Decisions (open)

- [ ] **Kid's name** in posts: anonymized (default) or named? — affects every future post
- [ ] **Wife's name / mentions:** anonymized (default) or "Lisa" / "my wife by name"?
- [ ] **Surgery context:** off-limits (default), oblique reference allowed, or speak about it directly when worth saying?
- [ ] **Closing sign-off:** "More next week." (default) or something else you want to make yours?

---

## 🟢 Site Audit Backlog (from `SITE_AUDIT_2026-05-09.md`)

- [ ] Decide Mort AI Nexus positioning — Option A / B / C from the audit
- [ ] Tags + categories index pages (your roadmap had this for Week 2)
- [ ] Share buttons on posts — currently off, audit recommends on
- [ ] Analytics decision — GA4 free vs. Plausible $9/mo vs. nothing
- [ ] `/contact/` page with email + LinkedIn + GitHub + "what I'm looking for"
- [ ] Per-post header images for older posts — **partial**: data-cake,
      mort-ai-nexus, robby, five-systems wired; agentic-hype, 25-years,
      senior-engineer-job-search, and the workshop post still need imagery.

## 🟢 Refresh follow-ups (2026-05-22)

- [ ] **Doc Intel patent post** — only patent without a unique hero image
      or inline diagram. Add a flowchart of the drift-detection pipeline,
      and a unique OG image.
- [ ] **RSS in nav** — currently in the main nav bar. RSS is a 2010-era
      affordance; consider moving to footer. `jekyll-feed` already emits
      `<link rel="alternate">` for auto-discovery.
- [ ] **Homepage tile order** — currently Robby / Data Cake / Mort in row 1,
      Voice-Bio / Strangler-Fig in row 2. Voice-Bio is the strongest
      quantitative line ($830B) — consider promoting it to row 1.
- [ ] **25-years callout flow** — the `.notice--info` wraps the punchline
      but the explanation paragraph below is now orphaned. Either pull
      the explanation INTO the notice, or add a transition.
- [ ] **Header-shape consistency** — patent posts mix `image:`/`og_image:`/
      `teaser:` shapes. Audit-tree and Doc Intel are header-light. Decide
      uniform pattern across patent posts.
- [ ] **Pagination on `/blog/`** — `_pages/blog.md` isn't an `index.*` file
      so `jekyll-paginate` v1 won't generate `/blog/page2/`. With 15 posts
      and `paginate: 5` the older-posts link will 404. Either drop pagination
      or accept the single-page grid (now uniform with default teaser).

---

## ✅ Done

- [x] 2026-05-18: `@dom` installed as blog operator (`.github/agents/dom.md`)
- [x] 2026-05-18: First weekly post (`_posts/2026-05-18-week-notes-toolkit-week.md`)
- [x] 2026-05-18: TODO.md established
- [x] 2026-05-22: `header.og_image` (plus `image`/`teaser`) on the 4 patent /
      hero-eligible posts pointing at the LinkedIn infographics
- [x] 2026-05-22: RSS link surfaced in nav (`_data/navigation.yml`)
- [x] 2026-05-22: Patents page links fixed to match `categories:` permalinks
      (`/engineering/ai/...` instead of bare `/YYYY/MM/DD/...`)
- [x] 2026-05-22: Workshop post — reconciled 200-vs-50 mismatch in body
- [x] 2026-05-22: Categories link added to top nav
