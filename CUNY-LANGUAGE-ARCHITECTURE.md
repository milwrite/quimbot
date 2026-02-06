# CUNY Foreign Language Learning Architecture
**Model:** Qwen-8B-Base → Fine-Tuned Language Learning Assistant  
**Target:** Heritage & Non-Native Students (Beginner to Intermediate)  
**Date:** 2026-02-05

---

## Overview

**Two-Stage Fine-Tuning Strategy:**

```
Qwen-8B-Base
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
├─ Qwen-8B-Arabic-L2
└─ ... (scalable to all CUNY language offerings)
```

---

## Stage 1: Core Linguist Model (PRIORITY)

**Goal:** Create a generalized language-learning assistant with:
1. **Dialogic competence** (question-asking, turn-taking, scaffolding)
2. **Contextual adaptability** (adjusting complexity to learner level)
3. **Pedagogical awareness** (error correction, encouragement, cultural notes)
4. **Multilingual foundation** (cross-linguistic transfer capabilities)

### Training Data Mix (Stage 1)

**Base Datasets (Already Downloaded):**

| Dataset | Purpose | Size | Language Coverage |
|---------|---------|------|-------------------|
| **LMSYS Chat-1M** | Real conversational patterns | 1M conversations | 154 languages |
| **Magpie-300K** | High-quality instruction-following | 300K examples | English (primary) |
| **WAXAL** | Multilingual speech/text data | 22 African languages | Diverse phonetics/syntax |
| **OpenHermes-2.5** | Instruction diversity | ~1M examples | English |

**Pedagogical Augmentation Needed:**
- Language learner dialogues (beginner/intermediate proficiency)
- Error correction examples (learner mistakes → teacher responses)
- Scaffolding patterns (simplification, paraphrasing, visual prompts)
- Cultural context explanations
- Grammar explanations in conversational format

**Proposed Mix:**
- 40% Real conversations (LMSYS) → Natural dialogue flow
- 20% Instruction-following (Magpie + OpenHermes) → Task competence
- 15% Multilingual data (WAXAL) → Cross-linguistic awareness
- 15% Pedagogical dialogues (to be sourced/created)
- 10% Safety/Ethics (Prosocial Dialog) → Appropriate classroom behavior

### Training Approach (Stage 1)

**Base Model:** Qwen/Qwen3-8B-Base  
**Method:** LoRA fine-tuning (rank 16-32)  
**Steps:** 500-1000 (full epoch on combined dataset)  
**Evaluation Metrics:**
- Conversational coherence
- Question diversity (open-ended vs. closed)
- Complexity adaptation (can it simplify language?)
- Error handling (does it correct gracefully?)

**Special Considerations:**
- **Avoid over-alignment:** Don't make it too formal/robotic
- **Maintain multilingual capacity:** Test cross-lingual transfer
- **Preserve cultural neutrality:** Stage 1 should be language-agnostic

---

## Stage 2: Language-Specific Variants

**Input:** Qwen-8B-Linguist (Stage 1 output)  
**Process:** Secondary fine-tuning on language-specific corpora

### Example: Spanish (Heritage vs. L2)

**Qwen-8B-Spanish-Heritage:**
- Focus: Code-switching (Spanish ↔ English)
- Dialect awareness (Caribbean, Mexican, South American variants)
- Cultural references (Latinx identity, family contexts)
- Error patterns: Heritage speakers (conjugation, spelling)

**Qwen-8B-Spanish-L2:**
- Focus: Explicit grammar instruction
- Vocabulary building (thematic units: food, travel, etc.)
- Pronunciation guidance (phoneme correction)
- Error patterns: Anglophone learners (false cognates, ser/estar)

### Data Requirements (Stage 2)

**Per Language:**
- Native speaker dialogues (10K+ examples)
- Learner corpora (errors + corrections)
- Textbook exercises (adapted to conversational format)
- Cultural texts (news, stories, social media)

**Heritage vs. L2 Distinction:**
- Heritage: Informal register, code-switching, identity-affirming
- L2: Structured progression, explicit rules, slower pacing

---

## Pedagogical Features (Cross-Stage)

### 1. **Adaptive Scaffolding**
Model should adjust output based on learner signals:
- "I don't understand" → Simplify + rephrase
- Slow response → Prompt with hints
- Error → Gentle correction + explanation

### 2. **Question-Asking Behavior**
Prioritize dialogic engagement:
- Open-ended: "¿Qué hiciste este fin de semana?"
- Comprehension checks: "¿Entiendes?"
- Reflective: "¿Por qué crees que...?"

### 3. **Cultural Contextualization**
Embed cultural notes naturally:
- "In Argentina, 'che' is used like 'dude' in English."
- "This phrase is more formal—use it with professors."

### 4. **Scaffolding Strategies (NOT Correction)**
Support discovery without giving answers:
- **Recasting:** Model correct form naturally ("Yes, she went to the store! What did she buy?")
- **Questioning:** Prompt reflection ("Does 'I go' or 'I went' fit with 'yesterday'?")
- **Hinting:** Offer clues ("When we talk about more than one, what changes?")
- **Encouraging exploration:** "Listen to both — which sounds better to you?"
- **AVOID explicit correction:** Never say "That's wrong" or "Remember the rule"

---

## RLHF Considerations (Reward Learning on Policy)

**Paper Reference:** [arXiv:2403.19279](https://arxiv.org/abs/2403.19279)

**Why RLP is Relevant:**
- Standard RLHF can drift off-distribution as the policy updates
- RLP keeps reward model aligned by using policy samples
- Critical for language learning: Pedagogical goals (reward) must stay aligned with student interactions (policy)

**Potential Application:**
- **Reward model:** Rate responses on pedagogical quality (clarity, encouragement, accuracy)
- **Policy:** Qwen-8B-Linguist generating responses to learner prompts
- **RLP advantage:** As model learns student patterns, reward model stays calibrated

**Implementation Path:**
1. Stage 1: Supervised fine-tuning (baseline Linguist model)
2. Collect human feedback (CUNY language teachers rate responses)
3. Train reward model on teacher preferences
4. Apply RLP to keep reward model on-distribution as policy adapts

**Outcome:** Model that aligns with teacher intuitions even as student interactions evolve

---

## Evaluation Framework

### Stage 1 (Core Linguist)
- **Dialogue quality:** Multi-turn coherence, question diversity
- **Adaptability:** Can it switch registers/complexity?
- **Multilingual transfer:** Test on unseen languages
- **Pedagogical tone:** Encouraging, patient, clear

### Stage 2 (Language-Specific)
- **Linguistic accuracy:** Grammar, vocabulary, pronunciation
- **Cultural appropriateness:** Dialect awareness, social context
- **Learner-level fit:** Beginner vs. intermediate differentiation
- **Heritage/L2 distinction:** Code-switching vs. explicit instruction

---

## Implementation Timeline

**Phase 1: Foundation (Current)**
- ✅ Download core datasets (LMSYS, Magpie, WAXAL, OpenHermes)
- ✅ Validate training pipeline (production run complete)
- ⏳ Source pedagogical dialogue data
- ⏳ Design preprocessing pipeline

**Phase 2: Stage 1 Training (Week 1-2)**
- Mix datasets per proposed ratio
- Run full training (500-1000 steps, batch 16)
- Evaluate on dialogue benchmarks
- Iterate on hyperparameters

**Phase 3: Stage 2 Pilot (Week 3-4)**
- Focus on Spanish (both heritage & L2)
- Collect CUNY-specific corpora
- Fine-tune two variants
- A/B test with students

**Phase 4: Scale (Month 2+)**
- Expand to Mandarin, Arabic, French, etc.
- Build CUNY language learning dataset repository
- Deploy in pilot classrooms

---

## Open Questions

1. **Pedagogical data sourcing:** Where to get learner dialogue corpora?
   - Partner with CUNY language depts for anonymized student transcripts?
   - Synthetic generation via GPT-4 (risky—may lack authenticity)?

2. **Heritage vs. L2 separation:** Should these be separate models or one model with mode switching?
   - Separate: Cleaner specialization
   - Unified: More efficient, relies on prompt engineering

3. **Evaluation with real students:** How to measure learning outcomes?
   - Pre/post assessments?
   - Student engagement metrics (time-on-task, questions asked)?

4. **RLHF scalability:** Can we collect enough teacher feedback across all languages?
   - Start with Spanish (largest CUNY enrollment)
   - Transfer reward model to other languages?

---

## Next Steps (Immediate)

1. **Commit progress to repo**
2. **Source pedagogical dialogue datasets** (search HuggingFace, academic repos)
3. **Design Stage 1 data mixing script**
4. **Test WAXAL multilingual transfer** (verify cross-lingual capabilities)
5. **Reach out to CUNY language faculty** for pilot partnership

---

**Status:** Architecture designed, awaiting implementation.  
**Last Updated:** 2026-02-05 21:56 EST by Petrarch 🜁
