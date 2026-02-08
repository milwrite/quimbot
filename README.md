# Quimbot

**Two-Stage Fine-Tuning Pipeline for Language Learning Assistants**

A workspace for the Orchestra fine-tuning project—building pedagogically-aware conversational models through staged LoRA fine-tuning on Qwen-8B.

---

## Architecture Overview

```
Qwen/Qwen3-8B-Base
       ↓
[Stage 1: Core Linguist Model]
       ↓
Qwen-8B-Linguist (generalized conversational + pedagogical behaviors)
       ↓
[Stage 2: Language-Specific Variants]
       ↓
├─ Qwen-8B-Spanish-Heritage
├─ Qwen-8B-Spanish-L2
├─ Qwen-8B-Mandarin-Heritage
└─ ... (scalable variants)
```

### Stage 1: Core Linguist
Establishes foundational capabilities:
- **Dialogic competence** — natural turn-taking, question-asking, conversational flow
- **Contextual adaptability** — adjusting complexity to learner signals
- **Pedagogical awareness** — scaffolding strategies, encouragement, cultural notes
- **Multilingual foundation** — cross-linguistic transfer from diverse corpora

### Stage 2: Language-Specific Variants
Secondary fine-tuning on language/learner-type specific data:
- Heritage speaker variants (code-switching, dialect awareness, identity-affirming)
- L2 learner variants (explicit grammar, structured progression, phoneme correction)

---

## Fine-Tuning Philosophy

### On-Policy Reward Learning

This project draws from research on **Reward Learning on Policy (RLP)** ([arXiv:2403.19279](https://arxiv.org/abs/2403.19279)):

> Standard RLHF can drift off-distribution as the policy updates. RLP keeps the reward model aligned by training on samples from the *current* policy, not just the original dataset.

**Why this matters for language learning:**
- Pedagogical goals (reward) must stay aligned with evolving student interactions (policy)
- As the model learns student patterns, the reward model remains calibrated
- Avoids reward hacking where the model games outdated reward signals

**Implementation path:**
1. Stage 1: Supervised fine-tuning (baseline Linguist model)
2. Collect human feedback (language teachers rate responses)
3. Train reward model on teacher preferences
4. Apply RLP to keep reward model on-distribution as policy adapts

### Scaffolding Over Correction

The pedagogical approach emphasizes **adaptive scaffolding** rather than explicit error correction:

- **Recasting:** Model correct form naturally ("Yes, she *went* to the store!")
- **Questioning:** Prompt reflection ("Does 'I go' fit with 'yesterday'?")
- **Hinting:** Offer clues ("When we talk about more than one, what changes?")
- **Encouraging exploration:** "Listen to both—which sounds better to you?"

We avoid explicit correction ("That's wrong") to support learner autonomy and discovery.

---

## Training Data

### Stage 1 Datasets (~4.5GB total)

| Dataset | Purpose | Size | Coverage |
|---------|---------|------|----------|
| **LMSYS Chat-1M** | Real conversational patterns | 2.4GB | 154 languages |
| **Magpie** | Instruction-following quality | 2.0GB | 300K examples |
| **Prosocial Dialog** | Safety/ethics grounding | 91MB | 120K dialogues |
| **TOEFL11** | Learner error patterns | ~6K | Scaffolding extraction |

**Proposed Mix:**
- 40% Real conversations (LMSYS) → Natural dialogue flow
- 20% Instruction-following (Magpie) → Task competence
- 15% Multilingual (reserved for Stage 2) → Cross-linguistic awareness
- 15% Pedagogical dialogues → Scaffolding behaviors
- 10% Safety/Ethics (Prosocial) → Appropriate classroom behavior

### Stage 2 Reserved

- **WAXAL** (1.3GB, 22 African languages) → `datasets/stage2-variants/`
- Language-specific corpora (to be collected per variant)

---

## Pipeline Components

### Training Infrastructure

- **Backend:** Tinker LoRA API
- **Base model:** `Qwen/Qwen3-8B-Base`
- **Method:** LoRA fine-tuning (rank 16-32)
- **Checkpoints:** Saved to Tinker storage (`tinker://...`)

### Key Scripts

| Script | Purpose |
|--------|---------|
| `fine-tuning/run_tinker_lora.py` | Main LoRA training loop |
| `fine-tuning/prepare_stage1.py` | Dataset mixing & preprocessing |
| `fine-tuning/test_lora_model.py` | Eval: compare base vs fine-tuned |
| `fine-tuning/generate_scaffolding_dialogues.py` | Synthetic pedagogical data |
| `fine-tuning/export_to_ollama.py` | Export merged model for local inference |

### Workflow Files

| File | Purpose |
|------|---------|
| `KANBAN.md` | Task board (updated 2x daily minimum) |
| `STATUS.md` | Current training/eval state |
| `DEVLOG.md` | Timestamped work notes |
| `RUNLOG.md` | Training run excerpts |
| `CUNY-LANGUAGE-ARCHITECTURE.md` | Full architectural specification |

---

## Evaluation Metrics

### Stage 1 (Core Linguist)
- Conversational coherence (multi-turn consistency)
- Question diversity (open-ended vs. closed)
- Complexity adaptation (can it simplify on cue?)
- Scaffolding quality (graceful error handling)

### Stage 2 (Variants)
- Linguistic accuracy (grammar, vocabulary)
- Cultural appropriateness (dialect, register)
- Learner-level fit (beginner vs. intermediate)
- Heritage/L2 distinction (code-switching vs. explicit instruction)

---

## Data Policy

**Do not commit datasets to Git.** Large files belong in local `datasets/` or off-repo storage. `.gitignore` excludes dataset directories.

---

## Project Structure

```
quimbot/
├── fine-tuning/          # Training scripts + workflows
├── datasets/             # Local data storage (gitignored)
│   ├── lmsys-chat-1m/
│   ├── magpie/
│   ├── prosocial/
│   ├── toefl11/
│   └── stage2-variants/  # WAXAL + future variant data
├── checkpoints/          # Local checkpoint cache
├── research/             # Dataset research + license verification
├── KANBAN.md             # Task board
├── STATUS.md             # Current state
├── DEVLOG.md             # Work log
└── CUNY-LANGUAGE-ARCHITECTURE.md  # Full architecture spec
```

---

## Quick Links

- [Fine-tuning README](fine-tuning/README.md)
- [Research README](research/README.md)
- [Architecture Spec](CUNY-LANGUAGE-ARCHITECTURE.md)
- [Collaboration Protocol](COLLABORATION.md)

---

## Current Status

**Stage 0 (Proof of Concept):** ✅ Complete  
- 63-step LoRA run on ultrachat subset
- Checkpoints saved to Tinker
- Eval confirms LoRA produces more concise outputs vs. base

**Stage 1 (Core Linguist):** 🔄 In Progress  
- Datasets downloaded (4.5GB)
- Mixing script ready
- Awaiting full training run with fixed checkpoint saving

**Stage 2 (Variants):** ⏸️ Pending Stage 1 completion

---

**Last Updated:** 2026-02-08
