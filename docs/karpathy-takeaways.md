# What's valuable in Andrej Karpathy's work — for an AI PM

Karpathy (ex-Tesla AI director, OpenAI founding team) builds the most-loved teaching artifacts in AI. His GitHub is a masterclass in one idea: **strip a complex system down to the smallest thing that still teaches the real lesson.** That instinct is exactly what separates a "PM who manages AI features" from a "PM who actually understands the machine." Here's what to take.

## The repos, ranked by value to you

1. **nn-zero-to-hero** (his lecture series + `micrograd`) — *start here.* `micrograd` is a neural network and backprop engine in ~100 lines of Python. If you build it once, you will understand gradients, training, and "why models do what they do" better than 95% of PMs. **This is your single highest-leverage learning move.** One lecture/week → one LinkedIn post each ("what a product manager learned building a neural net from scratch"). That content is rare and credible.
2. **nanoGPT** — the simplest real GPT training repo. Read it to understand what "training a model" actually involves: data, tokens, loss, compute, checkpoints. You don't need to train one; reading it demystifies the entire LLM supply chain you'll be PM-ing.
3. **nanochat** — "the best ChatGPT $100 can buy." A full ChatGPT-style stack (pretrain → finetune → serve) you can run end-to-end. Gold for understanding the *product* anatomy of an assistant: where personality, safety, and cost actually live.
4. **llm.c / llama2.c** — LLM training/inference in raw C. You won't write C, but the existence of these proves a point worth internalizing: the magic is mostly simple math at scale. Reduces "AI is mysterious" to "AI is engineering."

## The principles to steal (these are PM principles, not just code)

- **Radical simplification as a communication tool.** Karpathy's superpower isn't the code, it's removing everything non-essential until the core idea is obvious. Do this with specs, with LinkedIn posts, with exec updates. Your *The Identity Layer* series already does this — lean into it harder.
- **Build the smallest end-to-end version first.** Not a plan for the thing — the tiniest working thing. You already work this way (your screener, job pipeline, dashboards are all minimal-but-complete). Name it as your method in interviews: "I ship the smallest real version, then iterate."
- **Teach to prove you understand.** His reputation is built almost entirely on explaining clearly in public. That is *your* LinkedIn/Medium strategy. Karpathy is the proof that "build + explain in public" is a career, not a hobby.
- **Intuition over jargon.** He earns authority by making hard things feel simple, never by sounding smart. Copy the tone.

## Concrete moves this gives you

- **Learning track (in Mission Control):** watch one "Zero to Hero" lecture/week, build `micrograd` yourself, then write the "PM builds a neural net" post. Ties your identity/data credibility to genuine AI depth — exactly what Google/OpenAI/Anthropic screen for.
- **Interview story:** "I don't just write specs for models I don't understand — I built micrograd and nanoGPT to understand the gradient and the token, so I can have real conversations with research and eng." That sentence beats any cert.
- **Content angle nobody else has:** most PM influencers explain frameworks. Almost none can explain backprop in plain English *and* tie it to product. That intersection is your lane.

Bottom line: Karpathy is the template for "technical credibility earned in public." You're already building in public — add genuine model-level depth (his free lectures) and you become hard to ignore for the exact companies you're targeting.
