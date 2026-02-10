# Scaffolding Generation Optimization

## Current Status (2026-02-10)

**✅ What We Have:**
- 491 high-quality dialogues in `scaffolding_combined.jsonl`
- Balanced L1 distribution (36% Spanish, 35% Arabic, 29% Chinese)
- Good scaffolding quality (1.6 questions/dialogue, 4.2 turns avg)
- 66.7% coverage of L1×error combinations

**❌ Original Blocker:**
- Target: 1,000 dialogues
- Stopped at 491 due to OpenRouter credit exhaustion (402 error)
- Empty files: `scaffolding_gpt120b_500.jsonl`, `scaffolding_qwen72b_500.jsonl`

---

## Optimization Strategy

### 1. **Cost Reduction (10x cheaper)**

**Old approach:**
- Model: `moonshotai/kimi-k2.5` (~$0.50/1M tokens)
- Max tokens: 300
- No fallback models

**New approach:**
- Primary: `google/gemini-2.0-flash-001` ($0.10/1M) ← **5x cheaper**
- Fallback: `anthropic/claude-3.5-haiku` ($1.00/1M)
- Final fallback: `moonshotai/kimi-k2.5` ($0.50/1M)
- Max tokens: 200 (reduced by 33%)
- Compact prompt template (120 vs 180 tokens)

**Estimated cost to complete:**
- Remaining: 509 dialogues
- Tokens per dialogue: ~350 (prompt + response)
- Total tokens: ~178K
- **Cost: $0.018 (~2 cents)**

### 2. **Robustness Improvements**

**Resume capability:**
```bash
python3 generate_scaffolding_v2.py --resume --output scaffolding_v2.jsonl
```
- Skips existing (l1, error, correct) combinations
- Safe to interrupt and restart
- No duplicate work

**Retry logic:**
- Exponential backoff (2^n seconds)
- Automatic model fallback on failure
- Per-dialogue error handling (continues on failure)

**Quality filtering:**
```bash
python3 generate_scaffolding_v2.py --filter-quality
```
- Rejects explicit corrections ("wrong", "incorrect", "should be")
- Requires scaffolding questions
- Enforces minimum turn count

### 3. **Expanded Coverage**

**Old:** 5 error patterns per L1 (15 total)
**New:** 12 error patterns per L1 + Korean added (48 total)

**New error types:**
- `negation_error` (Spanish: "I no like")
- `subject_omission` (Spanish: "Is very hot")
- `participle_confusion` (Chinese: "I am boring")
- `conjunction_overuse` (Chinese: "Although...but")
- `pronoun_copy` (Arabic: "My friend he is tall")
- `gerund_error` (Korean: "I can swimming")
- ...and 6 more

**New L1:**
- Korean (12 patterns) — high-value for ESL tutoring

---

## Analysis Tools

### Quality Analysis
```bash
python3 analyze_scaffolding.py scaffolding_combined.jsonl
```

**Metrics tracked:**
- L1 distribution balance
- Proficiency level split
- Error type coverage
- Turn depth (avg 4.2 ✅)
- Scaffolding questions per dialogue (1.6 ✅)
- L1×Error combination coverage (66.7% ✅)

### Cost Tracking
```bash
python3 generate_scaffolding_v2.py --count 100
```

**Real-time tracking:**
- Tokens used per dialogue
- Cost per dialogue
- Running total cost
- Model used (for debugging expensive fallbacks)

---

## Completion Plan

### Option A: Complete to 1,000 (Recommended)
```bash
chmod +x complete_scaffolding.sh
./complete_scaffolding.sh
```

**What it does:**
1. Calculate remaining dialogues needed
2. Run optimized generator with resume + quality filtering
3. Merge with existing into `scaffolding_1000_final.jsonl`
4. Generate quality report

**Estimated time:** 10-15 minutes
**Estimated cost:** $0.02

### Option B: Train Now with 491
Use existing `scaffolding_combined.jsonl` (491 dialogues) for Stage 1.

**Mix strategy:**
- Scaffolding: 491 × ~600 bytes = 295 KB
- Anchor data: LMSYS + Magpie + Prosocial ≈ 200 MB
- Mix ratio: ~0.15% scaffolding (very low, but LoRA-ROADMAP says 20-30% on-policy)

**Verdict:** Too low. Should complete to 1,000 or generate more via on-policy loop.

---

## Scripts Created

| Script | Purpose | Status |
|--------|---------|--------|
| `generate_scaffolding_v2.py` | Optimized generation with resume + quality + multi-model | ✅ Ready |
| `analyze_scaffolding.py` | Quality analysis + recommendations | ✅ Ready |
| `complete_scaffolding.sh` | One-command completion to 1,000 | ✅ Ready |

---

## Next Steps

### Immediate (Today)
1. ✅ Analysis complete — quality confirmed
2. ✅ Optimized generator ready
3. **→ Run completion script** (`./complete_scaffolding.sh`)
4. Verify final quality (re-run analysis)
5. Update KANBAN with deliverable

### Short-term (This Week)
Per `LoRA-ROADMAP.md`, build on-policy loop:
1. `onpolicy_sample.py` — generate from current LoRA checkpoint
2. `onpolicy_score.py` — rule-based quality scoring
3. `onpolicy_train.py` — mixed training wrapper

### Long-term (Stage 1 Retraining)
1. Combine scaffolding (1,000) + anchor (LMSYS + Magpie + Prosocial)
2. Mix ratio: 70-80% anchor, 20-30% scaffolding
3. Train for 500-1000 steps
4. Evaluate + iterate via on-policy loop

---

## Key Improvements Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Cost/1M tokens** | $0.50 | $0.10 | **5x cheaper** |
| **Tokens/dialogue** | ~450 | ~350 | **22% reduction** |
| **Error patterns** | 15 | 48 | **3.2x coverage** |
| **L1 languages** | 3 | 4 | +Korean |
| **Resume support** | ❌ | ✅ | Crash-safe |
| **Quality filter** | ❌ | ✅ | Auto-reject bad outputs |
| **Model fallback** | ❌ | ✅ | 3-tier chain |
| **Cost tracking** | ❌ | ✅ | Real-time monitoring |

---

## Cost Comparison

**Completing to 1,000 dialogues:**

| Approach | Cost | Notes |
|----------|------|-------|
| **Original (Kimi K2.5)** | $0.09 | 509 × 350 tokens × $0.50/1M |
| **Optimized (Gemini Flash)** | $0.018 | 509 × 350 tokens × $0.10/1M |
| **Savings** | **$0.072** | 80% cost reduction |

**For context:**
- A coffee costs ~$5.00
- This optimization saves enough to generate **50,000+ dialogues** for the price of one coffee

---

## Quality Assurance

**Automated checks (v2 generator):**
- ✅ No explicit correction phrases
- ✅ Minimum 3 turns
- ✅ At least 1 scaffolding question
- ✅ Valid ChatML format

**Manual verification recommended:**
- Sample 10-20 dialogues from final output
- Check for natural scaffolding flow
- Verify error patterns are realistic
- Confirm L1 distribution remains balanced

---

**Status:** Ready to execute. New OPENROUTER_API_KEY configured. Run `./complete_scaffolding.sh` when ready.

🜁
