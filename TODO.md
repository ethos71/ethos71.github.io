# TODO

What **you** need to do with @dom from week to week and feature to
feature. Things @dom is doing on its own don't go here; only things
that need your decision, your brief, or your eyes.

Conventions: 🔴 this week, 🟡 next, 🟢 someday. Check off when done.

---

## 🔴 This Week

### Severance-agreement scrub (2026-05-22)
- [ ] **Audit patent URL slug** — body content scrubbed of novelty, but the post URL itself still
      contains `audit-red-black-tree-patent`. Renaming via `permalink:` in frontmatter would clean
      the URL but break any inbound links. Decide: rename + add a Jekyll redirect, leave the
      URL as a technical identifier only, or change the filename.
- [ ] **Verify the broader scrub** — read the 5 patent deep-dives, `patents.md`, the 5-patents
      meta post, sections 1/2/4 of `five-systems`, the homepage Robby tile, and `experience.md`.
      The pass removed: named data structures, specific signal inputs, component counts
      (70 skills / 15 roles), agent role lists, the kitchen-brigade architecture, the
      "confidence-over-time" framing, `XGBoost + scikit-learn` invention-context,
      `regional economic signals` and weather/housing/migration inputs, all 3 mermaid
      architecture diagrams (audit-tree / Mort pipeline / Robby brigade), the Data Cake
      `synthetic_row` schema, the Doc Intel drift table, the "Why a Red Black Tree"
      section, and the "within 2% of real-data models" claim.
      Kept: high-level problem framing, outcomes, patent-pending status, year ranges, Wayfair
      legal-context (public case law), JPMC and Connect Your Care content (not Vertex IP).

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

### Review the new weekly post (`_posts/2026-06-04-week-notes-fantasy-baseball.md`)
- [ ] **Naming call:** project referred to *only* as "fantasy baseball AI," never by repo
      name, per your instruction. The 2026-05-18 week-notes still calls it
      "fantasy-football XGBoost project" (wrong sport + names a tool) — decide whether
      to backfill that older post to match.
- [ ] **Header image:** post ships with the site-default OG/teaser banner; needs a
      bespoke `/assets/headers/week-notes-fantasy-baseball.png` to match the other posts.
- [ ] **Numbers sanity-check (all from this week's commits):** 77min→119s nightly job,
      13→0 CSV reads/writes, 8,061/8,386 players resolved, team_key ~10%→90%. Confirm
      none are more than you want public on a hobby project.
- [ ] Closer locked as "More next week."

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
- [x] 2026-06-13: Opinion post `_posts/2026-06-13-your-monolith-is-probably-fine.md`
      — trend-resistance / decision-discipline piece. Companion to the
      strangler-fig post (that one is the *how*; this is the *why/when*).
      Direct-committed per @dom workflow; review on your own timeline.


## 📋 @dom delegated tasks

<!-- Managed by `dom delegate`. @dom writes these; this bot implements, checks them off, and commits. `dom intake` lists your open ones. -->

- [x] `DOM-20260728-1` **(P3)** Hand-place .dom/BOSS.md (dom v2026.07.28 chain of command). You are the one bot with NO dom toolkit installed — Decision A (2026-07-12) skips dom install here because this repo is PUBLIC and .github/dom-bots.json would leak the private roster. That decision still stands; do NOT run install.sh. But BOSS.md is roster-free by construction and safe to publish, so copy it by hand from the dom repo (.dom/BOSS.md), change the `This bot:` line to this repo name, drop the `Self-check` section (no evals installed here), and add `.dom/*` + `!.dom/BOSS.md` to .gitignore. Before committing, re-read it and confirm it names no sibling bot and no local path. Purpose: an agent landing cold in this repo learns @dom is the boss and that @dom delegates rather than edits — today that is only inferable from a 454-line custom .github/agents/dom.md.
      ↳ verify: `grep -q "does not implement in this repo" .dom/BOSS.md && ! grep -Eiq "smartballz|thunderdome|plex|finsheit|choppa|/home/" .dom/BOSS.md && echo clean`
      ↳ set by @dom 2026-07-28 (owner @dom)
