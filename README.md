# Mission Control

A personal next-step advisor for Shubham Safaya. **Live:** https://shubham-safaya.github.io/mission-control/

Two modes in one self-contained `index.html` (no build, no backend, no Python):

1. **Roadmap** — every track that matters (top AI PM role, LinkedIn → 20K, *The Identity Layer* book, EB1A, build-in-public, content/reels, health, learning AI depth). Each shows the **one thing to do now** plus the next steps. Static and always available; edit the `TRACKS` data block to keep it current.

2. **Coach chat** — a real Claude advisor that already knows the goals, projects, and cadence (encoded in a system prompt). It runs **client-side with your own Anthropic API key**, stored only in your browser's `localStorage` and sent only to `api.anthropic.com` (uses the `anthropic-dangerous-direct-browser-access` header). Model selectable: Opus 4.8 / Sonnet 4.6 / Fable 5.

## Privacy / safety

- The committed system prompt contains **professional/public context only** — no financial or personal data.
- The API key never leaves your browser except in the direct call to Anthropic. Clear it with `localStorage.removeItem('mc_key')`.
- Get a key at [console.anthropic.com](https://console.anthropic.com/settings/keys).

Built by [Shubham Safaya](https://shubham-safaya.github.io).
