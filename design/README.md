# Design — UI direction mockups

Reference mockups for a future redesign of ethos71.github.io. These are
**not part of the published site** — the `design/` folder is in the Jekyll
`exclude:` list (`_config.yml`), so nothing here builds or ships to
GitHub Pages. It's a design archive we can point back to.

## Decision

**Chosen direction: `1-editorial-minimal` ✅**

Picked 2026-05-30. Magazine / print-editorial aesthetic — type and
whitespace carry it, the blog *is* the product. Fits a writing-heavy
site with 15+ long-form posts better than a portfolio-first layout.

- **Fonts:** Fraunces (serif display) + Newsreader (body)
- **Palette:** warm paper `#faf8f5`, near-black ink `#1a1a1a`, single
  oxblood accent `#9b3d2e`
- **Layout:** big-drama hero → two-column reading grid (date-gutter
  article list + editorial sidebar: about / topics / pull quote)

The other seven are kept for reference / cross-pollination (e.g. the
Swiss-grid `#6` work-row treatment, or the docs-sidebar `#8` archive
index, could be grafted in later).

## What's here

Open `mockups/index.html` for the side-by-side contact sheet. Each
direction has a `.png` (full-page screenshot at 1280px) and a `.html`
(live, interactive — real fonts + hover states).

| # | Direction | Notes |
|---|-----------|-------|
| 1 | **Editorial Minimal** ✅ | Chosen. Fraunces + oxblood, writing-first. |
| 2 | Dark Terminal | Near-black, electric-lime, bento metrics, `whoami` hero. |
| 3 | Polished Portfolio + Motion | Name-as-art hero, aurora glow, work tiles front. |
| 4 | Light Editorial-Corporate | Airy light bands, deep-green, high-trust. |
| 5 | Neo-Brutalist | Thick borders, hard shadows, chunky Archivo. |
| 6 | Swiss Grid | Strict 12-col, numbered sections, tabular metadata. |
| 7 | Moody Editorial Dark | Premium magazine at night — charcoal + gold serif, grain. |
| 8 | Docs / Dev-clean Sidebar | Fixed sidebar + post index. Best for a large archive. |

## Provenance

- Built 2026-05-30 with real site content (real post titles, metrics,
  work). Mockups are **homepages only** — the article reading page is
  still to be designed before any build.
- Rendered to PNG with headless Chrome at 1280px wide.

## Verification captures

`verification/` holds screenshots of what actually shipped, kept as a
record of the redesign landing:

- `BUILT-home.png`, `BUILT-article.png` — built output (home + article
  reading page) from the Editorial Minimal build.
- `LIVE-deployed.png`, `LIVE-final-home.png`, `LIVE-about-voice.png`,
  `LIVE-blog-list.png` — post-deploy captures of the live site.

## Next steps (not yet done)

1. Mock the **article / post reading page** in the Editorial Minimal
   direction (the real test for a content site).
2. Prototype the winner on a branch — homepage + article page — and
   preview before anything touches `main`'s look-and-feel.
