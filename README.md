# Quimbot

**Two-Stage Fine-Tuning Pipeline for Language Learning Assistants**

A workspace for the Orchestra fine-tuning project—building pedagogically-aware conversational models through staged LoRA fine-tuning on Qwen-8B.

---

## Table of Contents

- [Architecture Overview](#architecture-overview)
  - [Stage 1: Core Linguist](#stage-1-core-linguist)
  - [Stage 2: Language-Specific Variants](#stage-2-language-specific-variants)
- [Fine-Tuning Philosophy](#fine-tuning-philosophy)
  - [On-Policy Reward Learning](#on-policy-reward-learning)
  - [Scaffolding Over Correction](#scaffolding-over-correction)
- [Training Data](#training-data)
  - [Stage 1 Datasets](#stage-1-datasets-45gb-total)
  - [Stage 2 Reserved](#stage-2-reserved)
- [Pipeline Components](#pipeline-components)
  - [Training Infrastructure](#training-infrastructure)
  - [Key Scripts](#key-scripts)
  - [Workflow Files](#workflow-files)
- [Evaluation Framework](#evaluation-framework)
- [Evaluation Metrics](#evaluation-metrics)
- [Data Policy](#data-policy)
- [Project Structure](#project-structure)
- [Quick Links](#quick-links)
- [Current Status](#current-status)

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
| [`agents/KANBAN.md`](agents/KANBAN.md) | Task board (updated 2x daily minimum) |
| [`agents/STATUS.md`](agents/STATUS.md) | Current training/eval state |
| [`agents/DEVLOG.md`](agents/DEVLOG.md) | Timestamped work notes |
| [`agents/RUNLOG.md`](agents/RUNLOG.md) | Training run excerpts |
| [`research/CUNY-LANGUAGE-ARCHITECTURE.md`](research/CUNY-LANGUAGE-ARCHITECTURE.md) | Full architectural specification |

---

## Evaluation Framework

A sophisticated toolkit for evaluating model variants with parallel execution, caching, and rich metrics.

**Location:** [`evaluation/`](evaluation/)

**Features:**
- 15+ metrics (pedagogical quality, dialogue, complexity)
- 4 built-in test suites + custom YAML support
- Parallel execution with result caching
- JSON/Markdown/Comparison reporters

**Quick Start:**
```bash
cd evaluation
pip3 install -r requirements-eval.txt
python3 qwen-eval-v2.py --models base-model fine-tuned-v1 --verbose
```

**Documentation:** [evaluation/QWEN-EVAL-V2-README.md](evaluation/QWEN-EVAL-V2-README.md)

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
├── README.md                  # This file
├── CLAUDE.md                  # Agent instructions
├── agents/                    # Agent coordination
│   ├── COLLABORATION.md       # Multi-agent protocol
│   ├── KANBAN.md              # Task board + stand-ups
│   ├── STATUS.md              # Real-time status
│   ├── DEVLOG.md              # Timestamped work log
│   ├── RUNLOG.md              # Training run history
│   └── NEXT-ACTIONS.md        # Action items
├── evaluation/                # Model evaluation framework
│   ├── qwen-eval-v2.py        # Main CLI (v2)
│   ├── qwen_eval/             # Core package
│   └── QWEN-EVAL-V2-README.md # Full documentation
├── fine-tuning/               # Training scripts + workflows
│   ├── run_tinker_lora.py     # LoRA training
│   ├── prepare_stage1.py      # Data mixing
│   └── test_lora_model.py     # Evaluation
├── research/                  # Planning + dataset research
│   ├── CUNY-LANGUAGE-ARCHITECTURE.md  # Architecture spec
│   ├── TOEFL11-INTEGRATION-PLAN.md    # Integration plan
│   └── LICENSE-VERIFICATION.md        # Dataset licenses
├── datasets/                  # Local data storage (gitignored)
│   ├── lmsys-chat-1m/
│   ├── magpie/
│   ├── prosocial/
│   ├── toefl11/
│   └── stage2-variants/       # WAXAL + future variant data
└── checkpoints/               # Local checkpoint cache (gitignored)
```

---

## Quick Links

- [Evaluation Framework](evaluation/) - Model testing & comparison
- [Fine-tuning README](fine-tuning/README.md) - Training workflows
- [Research README](research/README.md) - Dataset research
- [Architecture Spec](research/CUNY-LANGUAGE-ARCHITECTURE.md) - Full design
- [Collaboration Protocol](agents/COLLABORATION.md) - Multi-agent workflow
- [Task Board](agents/KANBAN.md) - Current sprint
- [Status](agents/STATUS.md) - Real-time updates

---

## Current Status

**Stage 0 (Proof of Concept):** ✅ Complete  
- 63-step LoRA run on ultrachat subset
- Checkpoints saved to Tinker
- Eval confirms LoRA produces more concise outputs vs. base

**Stage 1 (Core Linguist):** 🔄 In Progress  
- Datasets downloaded (4.5GB)
- Mixing script ready
- Evaluation framework v2 complete
- Awaiting full training run with fixed checkpoint saving

**Stage 2 (Variants):** ⏸️ Pending Stage 1 completion

---

**Last Updated:** 2026-02-08
