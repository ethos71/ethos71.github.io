# Site Audit — 2026-05-09

Deep-dive review of `ethos71.github.io`. Findings split by priority. Items marked **[FIXED IN THIS COMMIT]** are applied; the rest are recommendations.

---

## 🚨 CRITICAL — Data integrity / consistency issues

These are the kind of things a recruiter will catch when they cross-reference your resume, blog, and LinkedIn. Fix before promoting any new traffic.

### 1. "200 people" vs "~50 people" — workshop attendance contradiction **[FIXED]**

- `index.md` claims "personally taught **200+ employees**"
- `about.md`, `experience.md`, the resume PDF, and the actual workshop blog post all say **~50 employees**
- The post URL slug `2026-03-18-teaching-200-people-to-build-ai-agents` even has the wrong number — but the post body itself says ~50

**Fix applied:** index.md updated to ~50. URL slug left alone (changing it breaks any inbound links).

### 2. About-page career table — Donegal placed in wrong year **[FIXED]**

- The table puts Donegal Insurance (2019) **after** Connect Your Care (2019–2021)
- Actual order: Donegal was Feb–May 2019, *before* Connect Your Care started in May 2019
- This is the kind of detail that flags as résumé fudging when LinkedIn doesn't match

**Fix applied:** Donegal moved before Connect Your Care in the table.

### 3. Misleading fraud claim — "$830B caught in fraud" **[FIXED]**

- `about.md` says voice biometric "caught $830B in fraud at JPMC"
- Reality (per resume + experience page + the new case study): $830B is the *industry-wide fraud-loss plateau correlated with the deployment cohort*, not what JPMC caught
- A recruiter who Googles "$830B JPMC fraud" will not find that claim and will assume embellishment

**Fix applied:** about.md rephrased to accurate framing.

### 4. Mort AI Nexus — positioning split across pages **[FLAGGED — needs your call]**

There's a tension across pages:
- **Patents page** + **old blog post** describe it as **mortgage-related nexus** with weather + economic indicators as leading signals (`Mort` = mortgage)
- **Resume** + **new case study post** describe it as **multi-state economic nexus detection (sales tax / Wayfair)**

Both descriptions reflect aspects of what was built, but they don't match. **You need to decide the positioning:**

- **Option A — Mortgage-specific.** Realign resume + case study to match patents page (mortgage nexus + weather/economic features). Most accurate to the original invention.
- **Option B — Generalize.** Update patents page to match the resume positioning (multi-state economic nexus broadly). Bigger TAM in marketing, but loses the unique "weather + economic features" hook.
- **Option C — Both.** Lead the patents page with: "Originally targeting mortgage-nexus compliance with weather + economic features as leading signals; architecture generalizes to multi-state economic nexus broadly." Most honest, mild loss of marketing crispness.

I'd recommend **Option C**. It's accurate and lets you pitch broadly without claiming what you didn't build. Tell me which option and I'll execute.

### 5. "Shipped $500M+ in products" claim **[FLAGGED]**

`index.md` and `about.md` both make this claim. It's vague and brittle — if a recruiter asks "what does $500M mean?" you need a defensible answer (revenue from products you led? customer-impact dollar value? cost-savings?).

**Recommendation:** Either tighten with a specific framing ("Led products generating $X in customer-spend savings" or "Led platform serving $X in customer transaction volume") or drop the number. Vague big-numbers hurt more than help with senior-engineer recruiters.

---

## ⭐ HIGH-IMPACT — Improvements with strong ROI

### 6. No OpenGraph image for link previews **[FIXED — site-wide default]**

When a blog post is shared on LinkedIn, Twitter, Slack, etc., the link preview shows... nothing. No image, no preview thumbnail. This dramatically reduces click-through.

**Fix applied:**
- Added `og_image` default in `_config.yml`
- Added `header.og_image` to the new five-systems case study post (uses one of the LinkedIn infographics)

Recommendation: Pick a hero image for each existing post too. The infographics in `assets/linkedin/` are great for this — `robby.png` for the Robby post, `mort-ai-nexus.png` for the Mort post, etc.

### 7. Patents page doesn't link to the deep-dive blog posts **[FIXED]**

Each of the 4 patents has a dedicated blog post, but the patents page never links to them. Visitors who want the technical depth have no path.

**Fix applied:** Added "Read the deep dive" link under each patent.

### 8. Tech-stack ordering on `index.md` is dated **[FIXED]**

The current order leads with cloud and languages. AI/ML buried at top of the list but the *order within AI/ML* leads with crewAI/AutoGen — solid. But the `Languages` line lists "C#/.NET, COBOL" prominently, which makes the resume read as "older stack engineer" rather than "AI-modern engineer."

**Fix applied:** Reordered to lead with AI/ML + Cloud-native, demoted COBOL to "(prior career)" framing.

### 9. Experience page doesn't cross-link to relevant blog posts **[FIXED]**

When you describe Robby in `experience.md`, there's a whole post about it. No link. Same for the workshop, the patents, and the case studies.

**Fix applied:** Added inline blog-post links to relevant bullets.

### 10. No `social_image` per post for the existing patents posts **[RECOMMENDED]**

The new five-systems post is fixed. The old Mort/Doc Intel/Audit Tree/Data Cake posts still have no preview images. **Recommendation:** Add `header.og_image` front matter to each of the 4 patent posts pointing to the matching infographic in `assets/linkedin/`.

---

## 🎯 MEDIUM — Polish & SEO

### 11. No favicon **[RECOMMENDED]**

Browser tabs show the default Jekyll/minimal-mistakes icon. A custom favicon (16x16, 32x32, 180x180 apple-touch-icon) is a small detail that signals quality.

### 12. No tags/categories index **[RECOMMENDED]**

Minimal-mistakes supports `_pages/tags.md` and `_pages/categories.md` with a simple include. Right now you can't browse by topic.

### 13. No Twitter/X handle in `_config.yml` **[RECOMMENDED]**

`twitter.username:` is blank. If you don't post on X, leave it. If you do, set it for proper Twitter card metadata.

### 14. No analytics **[RECOMMENDED — your call]**

`analytics:` is commented out. If you want to know which posts are getting traffic from LinkedIn, set up either Google Analytics 4 or Plausible. Plausible is a paid service ($9/mo) with better privacy posture; GA4 is free.

### 15. Comments and share buttons disabled on posts **[CONSIDER]**

Currently posts have `comments: false` and `share: false` in defaults. Comments are correctly disabled (a personal portfolio doesn't need them). But **share buttons could drive significant traffic back to LinkedIn** when readers want to repost a piece. Consider enabling.

### 16. `_pages/blog.md` is empty content **[OPTIONAL]**

The blog index page just has front matter and no intro copy. A 1-2 sentence intro at the top ("I write about engineering at scale, AI in production, and the gap between what gets pitched and what ships.") gives the page some character.

### 17. No 404 page **[RECOMMENDED]**

A custom `404.html` is one of those small touches. Minimal-mistakes ships with a default but you can override with personality.

---

## 📐 LOW PRIORITY — Nice to have

### 18. `_pages/contact.md` doesn't exist
Email is in the sidebar (`_config.yml` author section), but a dedicated `/contact/` page (with email + LinkedIn + GitHub + a "what I'm currently looking for" blurb) would help recruiters.

### 19. No RSS link in nav
`jekyll-feed` is enabled (good), but the feed isn't surfaced in the navigation.

### 20. Image asset folder is sparse
Only `profile.png` in `assets/images/`. The site is text-heavy. Adding 1-2 banner images (per-post header images, or a homepage hero) would warm it up.

### 21. The blog post 2025-12-11-how-data-cake-got-built.md uses different frontmatter style
Worth eyeballing for consistency — front-matter ordering, excerpt vs description, etc.

---

## 📋 RECOMMENDED ROADMAP

If you want to tier the remaining work:

**Week 1 (post-this-commit):**
- Decide Mort AI Nexus positioning (Option A/B/C above)
- Add `og_image` to the 4 patent posts (10 min each)
- Add favicon (Realfavicongenerator.net → drop in `/assets/`, override `_includes/head/custom.html`)

**Week 2:**
- Tags and categories index pages
- 404 page with personality
- Light intro copy on `/blog/`

**Week 3:**
- Enable share buttons on posts
- Set up analytics (GA4 free or Plausible $9/mo)
- Add `/contact/` page

**Whenever:**
- Per-post header images for older posts
- Twitter/X handle if you start posting there
