# LinkedIn Brand Assets

Five-project case study series content. All assets are derivative of the blog post:
[Five Systems I Shipped: A Production Case Study Catalog](/2026/05/09/five-systems-case-studies.html)

## Files

| File | Purpose |
|---|---|
| `linkedin-projects.md` | Copy/paste content for the LinkedIn **Projects** section under your profile (Experience tab) |
| `linkedin-social-posts.md` | Five ready-to-publish LinkedIn social posts, one per project, with posting-tactics notes |
| `linkedin-featured-caption.md` | How to set up the LinkedIn **Featured** section (top of profile) — pin order, title, description text |
| `linkedin-banner.png` | LinkedIn profile banner (1584×396) — upload via Profile → Edit cover image |
| `robby.png`, `mort-ai-nexus.png`, `voice-bio.png`, `data-cake.png`, `connect-your-care.png` | 5 infographics (1080×1080) — one per project, attach to the matching social post |
| `html/*.html` | Source HTML for each infographic + the banner, editable and re-renderable |
| `build-infographics.py` | Python script that regenerates all infographics from project config |

## Re-rendering after edits

If you want to tweak a stat, color, or layout:

1. Edit the `PROJECTS` list at the top of `build-infographics.py` (or edit the `html/*.html` files directly for one-offs)
2. Run: `python3 build-infographics.py`
3. PNGs regenerate in this directory

Or for a single one-off:

```bash
google-chrome --headless --disable-gpu --hide-scrollbars \
  --window-size=1080,1080 --screenshot=robby.png \
  file:///path/to/html/robby.html
```

## The 5 Projects

| # | Slug | Project | Highlight |
|---|---|---|---|
| 1 | `robby` | Robby — Multi-Agent SDLC | 70 skills, 15 roles, MCP-integrated |
| 2 | `mort-ai-nexus` | Mort AI Nexus | Real-time multi-state nexus detection (patent pending) |
| 3 | `voice-bio` | JPMC Voice Biometric | ~10M accounts onboarded in 90 days, ~$830B fraud plateau |
| 4 | `data-cake` | Data Cake | NLP synthetic tax data, no PII (patent pending) |
| 5 | `connect-your-care` | HRCommand Decomposition | Strangler fig that drove the United Health acquisition |

## Posting plan

Drop one per week, Tuesday or Wednesday, 8–10am ET.
After all five are out: pin the blog post to your LinkedIn Featured section.

## Updating the banner

To re-render after editing `html/banner.html`:

```bash
google-chrome --headless --disable-gpu --hide-scrollbars \
  --window-size=1584,396 --screenshot=linkedin-banner.png \
  file:///path/to/html/banner.html
```

The banner reserves a 280px-wide zone on the bottom-left for the LinkedIn profile-picture overlay. Don't put text or critical visual elements there.
