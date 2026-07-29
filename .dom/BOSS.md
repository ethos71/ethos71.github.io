# Chain of Command

**Boss:** `@dom` — the AI cost-cutting toolkit.
**Source of truth:** https://github.com/ethos71/dom
**This bot:** `ethos71.github.io`
**Tracked branch:** `main`

Any agent, human, or CI job that lands in this repo and needs to know
*who decides* reads this file first. It is deliberately short and
deliberately stable — the details live where they belong (below), and
this file only says who is in charge and how work flows.

---

## The rule that matters most

**`@dom` does not implement in this repo.**

`@dom` writes `TODO.md` and memory. The owning bot implements. That
boundary runs in both directions and neither side may cross it
unilaterally:

**This repo is the exception.** Across the other bots, `@dom` delegates
and never implements — it writes `TODO.md` and the owning bot does the
work. Here there is no separate owning bot: **`@dom` operates this site
directly** and implements its own tasks.

So the boundary that constrains `@dom` here is not *who writes the
code*, it is *how it ships*:

| `@dom` may | `@dom` may NOT |
|---|---|
| Write and commit content and layout | Push straight to the deploy branch |
| Open a branch and a PR | Merge before CI build-check is green |
| Merge once CI is green and verified | Publish unreviewed outward-facing copy |
| Delegate case studies to `@job` | Publish anything scrubbed from the public résumé |

This is a public, outward-facing site tied to a job search. An unverified
push is visible to anyone reading it, immediately.

> This is not a style preference. On 2026-07-12 an `@dom` session
> dumped the toolkit uncommitted into a bot's working tree and created
> branches and worktrees there. The bot had to revert it, clean 31
> stale worktrees, and re-install the toolkit itself. **The toolkit was
> wanted — the delivery was the violation.**

## How work reaches this repo

```
@dom  ──dom delegate──▶  TODO.md  ──▶  this bot implements  ──▶  ship gate  ──▶  merge
```

1. `@dom` appends a task to `TODO.md` with an ID (`DOM-<date>-<n>`), a
   priority, and a verification command.
2. This bot picks it up, implements it, and runs the verification.
3. A branch + PR gates the ship — this site is public and outward-facing,
   so changes are verified by the PR's CI build-check and an artifact
   screenshot **before** merge, never pushed straight to the deploy
   branch.
4. This bot reports back by updating the task's status in `TODO.md`.

## Command surface

Every bot command is `@<bot> --<command>` — never a bare
`/<command>` (that collides with Claude Code and Copilot built-ins).

| Command | Does |
|---|---|
| `@ethos71.github.io --update` | Pull the latest toolkit from `@dom` |
| `@ethos71.github.io --status` | Readiness check |
| `@ethos71.github.io --usage` | Tokens / cost / latency + local-model audit |
| `@ethos71.github.io --task <file> 'change' 'test'` | Delegate one atomic code task |

## Where to read next

| Question | File |
|---|---|
| What am I supposed to be doing? | `TODO.md` |
| What is `@dom` and how does it route? | `.github/agents/dom.md` |
| What does this repo's own agent own? | `.github/agents/` |

## No toolkit here

This repo deliberately ships **no dom toolkit** — it is public, and
`.github/dom-bots.json` would publish the private roster (Decision A,
2026-07-12). There is no `.dom/VERSION`, no `--update`, and no eval
suite. This file is maintained by hand from @dom's copy.

---

## A note on what is *not* in this file

No roster. No sibling bot names. No local filesystem paths. No
infrastructure detail.

This file is tracked in git, and some repos that carry it are
**public**. Chain of command is safe to publish; the roster
(`.github/dom-bots.json`) is not, and must never be summarized,
quoted, or reconstructed here. In the toolkit repos an eval enforces
that automatically; here there is no eval, so it is on you to re-read
this file before every commit that touches it.

<!-- Managed by dom install.sh. Regenerated on every `--update`.
     Local edits are overwritten — change the generator in dom, not this file. -->
