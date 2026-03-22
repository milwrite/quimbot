# Model Substitution Proposal — Cloze Reader
**Authors:** Petrarch + Quimbot  
**Date:** 2026-03-19  
**Status:** Draft — awaiting milwrite review

---

## Context

The current implementation routes all three AI tasks through a single model (`google/gemma-3-27b-it` via OpenRouter). This document proposes a task-differentiated substitution strategy that preserves output quality while reducing model size and inference cost.

Source reviewed: `src/aiService.js`, `src/clozeGameEngine.js`, `src/conversationManager.js`, `app.py`

---

## The Three Tasks

### Task 1 — Word Selection (`selectSignificantWords` / `processBothPassages`)

**What the model actually does:**  
Receives a passage (~150–300 words), returns a JSON array of 1–3 words classified by approximate frequency/difficulty tier (easy / medium / challenging). Hard constraints (letter range 4–12/14, lowercase only, not first 10 words, present in passage) are enforced *post-hoc* in `_validateWords` in JS. The model is doing coarse POS filtering + rough frequency judgment, not semantic reasoning.

**Token budget:** ~200 in / 200 out  
**Temperature:** 0.5  
**Failure mode:** JSON non-compliance (caught and parsed with regex fallbacks); wrong difficulty tier (not caught, affects gameplay balance but not game function)

**Proposal: Replace with `wordfreq` + NLTK POS tags (local, zero-cost)**  
Quimbot's argument here is correct. The post-hoc JS validation already enforces the hard constraints. What the model adds is (a) POS classification and (b) rough difficulty scoring. Both are solvable locally:

- `wordfreq` (Python, 2.5MB model) gives word frequency per Zipfian tier — frequency rank maps reliably to easy/medium/challenging
- `nltk.pos_tag` gives POS labels (NN, VB, JJ) to filter for nouns/verbs/adjectives
- No JSON compliance risk, zero latency, no API call

**Alternatively**, if a model call is retained for this task: `Phi-3.5-Mini-128k-instruct` (3.8B) or `Qwen2.5-7B-Instruct` handles this prompt reliably. Both produce valid JSON arrays from short-passage prompts at temperature 0.5. The instruction is explicit enough that model capacity is not the binding constraint.

**Risk: Low.** The JS validation layer catches bad output. Difficulty calibration may require tuning the frequency-tier thresholds, but that's a config change, not a structural one.

---

### Task 2 — Contextualization (`generateContextualization`)

**What the model actually does:**  
Given title, author, and passage, produces one sentence (max 25 words) of literary or historical context. Output is decorative — it does not affect game logic. Failure already falls back to a hardcoded attribution string (`A passage from ${author}'s "${title}"`).

**Token budget:** ~200 in / 150 out  
**Temperature:** 0.7  
**Failure mode:** Generic or inaccurate context (fallback deployed and acceptable)

**Proposal: `Phi-3.5-Mini-128k-instruct` or `Gemma-3-4B-IT`**  
Both handle well-represented Gutenberg-era authors (Austen, Melville, Dickens, Poe) at this output length. Degradation risk exists for obscure texts in the HuggingFace `manu/project_gutenberg` dataset — smaller models have weaker coverage of minor 19th-century authors. But the fallback is already deployed, so degradation is graceful.

**Alternative: Drop the API call entirely.** A curated static lookup table keyed on author / period / genre would cover 80–90% of the Gutenberg corpus at zero cost and higher accuracy than a small model hallucinating context. This is worth evaluating before committing to a model call at all.

**Risk: Low.** Worst case is fallback to attribution string, which is acceptable per current behavior.

---

### Task 3 — Hint Generation (`generateContextualHint` via `ChatService`)

**What the model actually does:**  
Given a passage with the target word blanked, plus the target word (privately), generates one of four hint types: part of speech, sentence role, word category, synonym. The model must hold the target word in context, produce a pedagogically useful paraphrase, and not name the word or a close variant.

**Token budget:** ~150 in / 150 out  
**Temperature:** 0.7  
**Failure mode (Quimbot's addition):** Two distinct failure modes:
1. Direct leak — model outputs the target word (caught by simple string match)
2. Morphological leak — model outputs a variant (e.g., "a form of *illuminate*" when target is "illumined") — **not caught by `_validateWords`**, which validates input words against the passage, not hint output against the target word

**Proposal: `Qwen2.5-7B-Instruct`**  
This is the most sensitive task. The synonym prompt in particular requires instruction-following precision: the model must suppress the target word *and* its morphological family under a soft instruction ("never say this word directly"). Qwen2.5-7B handles this well in informal testing; Phi-3.5-Mini shows higher leak rates on synonym tasks.

**Before any model substitution here: adversarial pass required.** Specifically:

- Test synonym prompt against 50–100 common Gutenberg content words
- Check output for: exact match, stemmed match (Porter/Snowball), and edit-distance ≤ 2 from target
- If leak rate > 5%, model is disqualified for this task regardless of size

**If adversarial pass clears:** `Qwen2.5-7B-Instruct` via OpenRouter or local (if self-hosted path is open).  
**If not:** retain 27B for hint generation only; substitute on Tasks 1 and 2.

A separate mitigation (independent of model choice): add a server-side output filter in `app.py`'s `/api/ai/chat` proxy that strips any hint containing the target word or a stemmed match before returning to client. This is a one-time engineering fix that makes the hint task model-agnostic on the leak dimension.

**Risk: Medium** without output filter; **Low** with output filter in place.

---

## Full Proposal Table

| Task | Current model | Proposed replacement | Approach | Cost delta (approx) | Risk |
|------|--------------|---------------------|----------|---------------------|------|
| Word selection | Gemma-3-27B-IT | `wordfreq` + NLTK (local) | No API call | ~100% reduction | Low |
| Word selection (alt) | Gemma-3-27B-IT | Qwen2.5-7B or Phi-3.5-Mini | Smaller model | ~6–8x reduction | Low |
| Contextualization | Gemma-3-27B-IT | Static lookup or Gemma-3-4B-IT | Table or smaller model | ~80–100% reduction | Low |
| Hint generation | Gemma-3-27B-IT | Qwen2.5-7B-Instruct | Smaller model + output filter | ~6–8x reduction | Medium → Low with filter |

---

## Implementation Dependencies

For the local word selection path:
- Python: `wordfreq`, `nltk` (already available in `requirements.txt` environment)
- New endpoint in `app.py`: `/api/words/select` — takes passage + count + level, returns JSON array
- Remove model call from `aiService.js` `selectSignificantWords`; replace with fetch to local endpoint
- Preserve JS `_validateWords` as-is (still catches edge cases)

For the output filter:
- In `app.py` `/api/ai/chat`: inspect request for hint task (identify by system prompt content or add explicit `task_type` field to `AIChatRequest`)
- If `task_type == "hint"` and a `target_word` is passed: strip response if it contains target or stemmed match before returning
- Requires minor schema addition to `AIChatRequest` — no client-breaking change

---

## Paper relevance

This substitution analysis is directly useful for Sessions 4–5 (artifact close reading). The fact that word selection — the task most central to the paper's argument about model-mediated cloze construction — is replaceable by a frequency table and POS tagger raises a pointed question: what is the 27B model actually contributing to the "semantic inbetweenness" heuristic? The implementation answer is: POS classification and a difficulty tier, both of which are achievable without instruction-following capability. That's material for the "code as argument" section — the gap between what the prompt claims the model is doing and what the model is actually being asked to do.

---

## Next steps

1. **milwrite decides:** local word selection path vs. smaller model vs. status quo
2. If local path: Quimbot implements `/api/words/select` endpoint + JS refactor
3. Adversarial pass on synonym prompt (either path — this is a hygiene fix regardless of model size)
4. Output filter in proxy (recommended regardless of model size)
5. Petrarch documents model substitution matrix for paper artifact section
