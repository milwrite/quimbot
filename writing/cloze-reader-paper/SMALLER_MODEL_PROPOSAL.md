# Smaller Model Integration Proposal
*Petrarch + Quimbot — 2026-03-19*

## Context

milwrite asked us to review the `milwrite/cloze-reader` implementation and propose how a much smaller model could handle the three AI tasks without quality loss. Petrarch pulled the implementation from the public GitHub repo (`aiService.js`, game engine, `ChatService`). This document synthesizes both analyses.

---

## The Three Tasks

### 1. Word Selection (`selectSignificantWords` / `processBothPassages`)

The model receives a passage and returns a JSON array of 1–3 words to blank. Prompt ~200 tokens, response capped at 200 tokens, temperature 0.5. The JS validation layer (`_validateWords`) enforces the hard constraints: letter range, lowercase-only, not in first 10 words, actual presence in passage. The model's job is coarse semantic judgment ("is this word easy / medium / challenging?") plus basic POS filtering (nouns, verbs, adjectives over function words). The difficulty signal comes from prompt instruction, not from model internals.

**Proposal: skip the model call entirely.**

`wordfreq` + NLTK POS tags covers 90% of what the prompt asks the model to do. Pipeline:
1. POS-tag the passage with NLTK
2. Filter to NN/NNS/VB*/JJ tokens
3. Score by `wordfreq.word_frequency(word, 'en')` — invert for difficulty
4. Sample 1–3 words at the target difficulty percentile

Zero latency, no JSON compliance risk, no model dependency. The post-hoc JS validation already handles edge cases. This is the cleanest path for this task.

**Risk:** Low. wordfreq covers ~99% of English vocabulary. Obscure literary terms may score as "rare" regardless of actual pedagogical difficulty — acceptable given the existing difficulty tiers are approximate anyway.

### 2. Contextualization (`generateContextualization`)

One sentence of literary/historical context per passage. Max 150 tokens, temperature 0.7. Output is decorative — doesn't affect gameplay. Failure falls back gracefully to a boilerplate attribution string.

**Proposal: static lookup table first, model as fallback.**

A static author/period/genre → context string table covers the Gutenberg corpus well (finite author set, stable metadata). Zero inference cost, no hallucination risk on dates or attributions. For authors outside the table, fall back to SmolLM2-1.7B-Instruct or Phi-3.5-Mini. The existing boilerplate fallback stays as the final tier.

**Risk:** Low. The only failure mode is a gap in the lookup table, which the fallback already handles.

### 3. Hint Generation (`generateContextualHint` via `ChatService`)

Four hint types: part of speech, sentence role, word category, synonym. Each prompt ~100–150 tokens in, max 150 tokens out. The model is given the target word and told not to reveal it. The ask: produce a pedagogically useful paraphrase or synonym without naming the word. Fallback responses are static strings and are serviceable.

**Proposal: 7B instruct model.**

Qwen2.5-7B-Instruct or Mistral-7B-Instruct-v0.3. Both handle the soft instruction-following reliably. Do not go below 7B for this task without adversarial testing.

**Failure modes to test (ordered by severity):**

1. **Direct leak** — model outputs the target word in the hint. Catchable with a simple string match.
2. **Morphological leak** — model outputs a variant (e.g., "a form of *illuminate*" when target is "illumined"). Harder to catch; requires stemming or edit-distance check against the target in the hint validator.
3. **Near-synonym that collapses difficulty** — model gives a synonym so obvious it removes the challenge. Subjective; requires human eval pass.

The current `_validateWords` string match catches case 1 only. The fix for cases 1 and 2 belongs in the `/api/ai/chat` proxy as a server-side output filter — stemmed match check against the target word before the response reaches the client. This applies regardless of model size and should ship independently of the model swap.

Before committing to a smaller model for hints, run an adversarial pass on the synonym prompt with 50–100 literary word samples, checking for cases 1 and 2 specifically.

**Risk:** Medium. The failure mode isn't bad output — it's output that breaks the game mechanic. Morphological leak (case 2) is the highest-priority gap in the current validation logic regardless of model size.

---

## Summary Table

| Task | Current | Proposed | Risk |
|---|---|---|---|
| Word selection | LLM call (JSON array) | `wordfreq` + NLTK POS — no model | Low |
| Contextualization | LLM call (~25 words) | Static lookup table; SmolLM2-1.7B as fallback | Low (fallback covers failure) |
| Hint generation | LLM call (4 hint types) | Qwen2.5-7B-Instruct | Medium (needs adversarial pass) |

---

## Implementation Order

1. **Word selection** — replace model call with wordfreq + NLTK. No new dependencies beyond `nltk` and `wordfreq` (both pip-installable). Ship this first; lowest risk, largest latency win.
2. **Contextualization** — swap to SmolLM2 or Phi-3.5-Mini via local inference (Ollama or llama.cpp). Validate on 20 passages from the corpus.
3. **Hint generation** — swap to Qwen2.5-7B. Run adversarial synonym test first. Add morphological leak check to hint validator (stemmer comparison against target word before returning hint to client).

---

## Open Questions for milwrite

- Is local inference (Ollama) acceptable, or does this need to stay API-compatible?
- What's the latency budget per game round? (Affects whether 7B local is viable or if we need to keep hints on a fast API endpoint.)
- Should the morphological leak fix go in regardless of model swap? (Yes, per Quimbot — it's a gap in current validation independent of this proposal.)
