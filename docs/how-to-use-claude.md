# How to get the most out of Claude (for Shubham)

You're treating Claude like a chat box. It's closer to a teammate that can read your files, run code, build apps, and ship to GitHub. Here's how to actually use it, and where each surface fits.

## The mental model: 3 surfaces, 3 jobs

| Surface | What it is | Use it for |
|---|---|---|
| **Claude Code** (terminal/IDE) | Claude with tools — reads your files, runs commands, edits code, pushes to git | **Building and changing systems.** This is what built your screener, dashboards, site, and these tools. Your default for anything that touches files or repos. |
| **Connectors** (Claude app) | Gmail, Drive, Notion, etc. plugged into a chat | **Giving a chat context.** "Summarize this Drive doc", "draft a reply to this email." Read/act on your data, not for scheduled jobs. |
| **Cowork / Projects** (Claude app) | Multi-step work in the app, with memory | One-off research, doc drafting, deck outlines. Good for non-code deliverables you want to iterate on. |
| **GitHub Actions** (not Claude) | Free cloud cron | **Recurring automation.** Your screener email, job brief, weekly essay, dashboard refresh all run here — no Claude needed once built. |

**Rule of thumb:** Claude Code *builds* the machine; GitHub Actions *runs* it on a schedule; connectors give a chat your context; cowork is for one-off thinking. You don't have Python locally and don't need it — everything recurring lives in Actions (the cloud).

## How to delegate well (this is the skill)

- **Give the goal and the constraints, not the steps.** "Make my screener email land before the bell and use my real holdings" beats "change line 14." Claude is better when it can see the whole problem.
- **Batch big asks.** One "QA all my projects, fix what's broken, and enhance each" session does more than ten small ones, because context compounds. You already do this — keep doing it.
- **Let it work, then review.** It can run for many minutes on a hard task. Ask for the outcome and the diff, not a play-by-play.
- **Point it at your stuff.** "Read my Downloads / my repo / this screenshot" — it reads PDFs, images, code, sheets. Grounding it in your real files is where the quality jumps.
- **Make it teach you.** "Explain what you changed and why" turns every task into learning. Use this for the AI-depth track.

## Highest-leverage things to ask Claude for (your context)

1. **Regenerate artifacts on demand:** resume variants per company, tailored cover letters, the EB1A dossier as criteria-mapped exhibits, recommender-letter drafts.
2. **Batch your content:** "Draft the next 8 chapters of The Identity Layer" or "10 LinkedIn hooks on identity, no em dashes." One session = a month of posts.
3. **Build more dashboards:** you now have a pattern (free public data → GitHub Pages → daily Action). Ask for the next one (e.g. "retail-media ad-spend tracker", "AI-job-market tracker") whenever you spot a data source.
4. **Interview prep:** "Run me through a Staff PM identity-platform case as the interviewer." It can play the loop.
5. **Keep it all green:** "QA my repos, fix any failing CI, enhance where weak" — a standing monthly ask.

## Maximize Fable 5 while you have it

Fable is the most capable model — best spent on **big, hard, one-shot builds**, not quick lookups. Front-load the ambitious stuff: regenerate your whole content backlog, design a new dashboard end-to-end, draft the EB1A exhibit set, write the next 8 book chapters. After it rolls off, Opus/Sonnet handle day-to-day fine.

## A standing weekly loop

- **Mon:** "What changed in my repos / pipelines last week, and what's the one thing to fix?"
- **Mid-week:** batch content (posts + next book chapter).
- **Fri:** "Prep me for one PM interview question in my domain."
- **Monthly:** "QA everything, enhance one flow, propose one new dashboard."

The Mission Control coach (this app) is wired with your context for exactly these — but Claude Code is where the building happens.
