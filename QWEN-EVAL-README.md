# Qwen Model Evaluation Workflow

Systematic evaluation framework for comparing Qwen base models against pedagogical fine-tuned variants.

## Quick Start

```bash
# List available test suites
python3 qwen-eval.py --list-suites

# Run basic evaluation (base model vs dialog-v1)
python3 qwen-eval.py --verbose

# Evaluate specific models
python3 qwen-eval.py --models qwen2.5:8b qwen-8b-dialog-v1 custom-lora-v2

# Different test suite
python3 qwen-eval.py --test-suite dialogue --verbose

# Save results
python3 qwen-eval.py --output results.json --report eval-report.md
```

## Test Suites

### 1. **Pedagogical** (default)
Tests for inquiry-led, scaffolding dialogue:
- **scaffolding_inquiry**: Should ask questions, avoid direct answers
- **adaptive_depth**: Should probe understanding before explaining
- **socratic_method**: Guide through questions vs showing steps
- **metacognitive**: Help identify existing knowledge, guide process

**Criteria:** Question-asking, co-investigation, adaptive scaffolding

### 2. **Dialogue**
Multi-turn conversational patterns:
- **multi_turn_context**: Establish context through questions
- **collaborative**: Invite co-investigation, not lecture

**Criteria:** Conversational flow, contextual awareness

### 3. **Baseline**
Sanity checks for basic functionality:
- **factual_recall**: Simple factual answers
- **basic_instruction**: Clear technical explanations

**Criteria:** Correctness, clarity

## Evaluation Process

### Stage 1: Base Model vs First-Order Variant

Compare `Qwen/Qwen3-8B` (base) against `qwen-8b-dialog-v1` (LoRA-tuned):

```bash
python3 qwen-eval.py \
  --models qwen2.5:8b qwen-8b-dialog-v1 \
  --test-suite pedagogical \
  --output stage1-results.json \
  --report stage1-report.md \
  --verbose
```

**What to look for:**
- Does dialog-v1 ask more questions?
- Does it avoid direct instruction?
- Is scaffolding evident?
- Trade-offs in speed/quality?

### Stage 2: LoRA Variant Comparison

As you develop new LoRA variants, compare against the current best:

```bash
python3 qwen-eval.py \
  --models qwen-8b-dialog-v1 qwen-8b-dialog-v2 qwen-8b-socratic-v1 \
  --test-suite pedagogical \
  --output stage2-results.json \
  --report stage2-comparison.md
```

**Iteration workflow:**
1. Train new LoRA variant
2. Convert to GGUF, import to Ollama
3. Run eval against previous best
4. Compare reports side-by-side
5. Document what changed (data mix, hyperparams, etc.)

### Stage 3: Regression Testing

Before promoting a variant to production:

```bash
# Run all test suites
for suite in pedagogical dialogue baseline; do
  python3 qwen-eval.py \
    --models qwen-8b-dialog-v1 qwen-8b-NEW-VARIANT \
    --test-suite $suite \
    --output "regression-${suite}.json" \
    --report "regression-${suite}.md"
done
```

Ensure new variant:
- ✅ Maintains pedagogical quality (pedagogical suite)
- ✅ Preserves conversational flow (dialogue suite)
- ✅ Doesn't break basic functionality (baseline suite)

## Adding Custom Tests

Edit `qwen-eval.py` and add to `TEST_SUITES`:

```python
TEST_SUITES["custom"] = [
    {
        "name": "your_test_name",
        "prompt": "Your test prompt here",
        "criteria": "What you're looking for in the response"
    }
]
```

Then run:
```bash
python3 qwen-eval.py --test-suite custom --verbose
```

## Metrics

The script captures:
- **Response text**: Full model output
- **Total time**: End-to-end inference time
- **Tokens/sec**: Rough throughput estimate
- **Timestamp**: When evaluation ran

### Performance Baselines
- Base Qwen2.5:8b: ~30-50 tok/s (M1/M2 Mac)
- Dialog-v1 (LoRA): Similar speed (LoRA adds minimal overhead)

## Output Formats

### JSON Results (`--output`)
```json
[
  {
    "model": "qwen-8b-dialog-v1",
    "prompt": "I'm struggling to understand...",
    "response": "What specifically about...",
    "tokens_per_sec": 42.3,
    "total_time": 3.2,
    "timestamp": "2026-02-08T21:15:00"
  }
]
```

### Markdown Report (`--report`)
- Performance summary table
- Side-by-side response comparisons
- Easy to commit to git, review in PRs

## Integration with Fine-Tuning Pipeline

1. **Pre-training**: Establish baseline with base model
2. **Post-LoRA**: Evaluate immediately after training
3. **Iteration**: Compare each variant against previous best
4. **Regression**: Full suite before production deployment

## Workflow Tips

### Quick Iteration
```bash
# Fast feedback loop during development
python3 qwen-eval.py \
  --models NEW-VARIANT \
  --test-suite pedagogical \
  --verbose | tee quick-check.log
```

### Automated Comparison
```bash
# Save timestamped reports for history
DATE=$(date +%Y%m%d-%H%M)
python3 qwen-eval.py \
  --models qwen-8b-dialog-v1 qwen-8b-dialog-v2 \
  --output "evals/results-${DATE}.json" \
  --report "evals/report-${DATE}.md"
```

### Git Workflow
```bash
# Commit eval results alongside model checkpoints
git add qwen-eval.py evals/
git commit -m "eval: dialog-v2 vs dialog-v1 (pedagogical suite)"
```

## Next Steps

- [ ] Add automated scoring (GPT-4 as judge?)
- [ ] Expand test suites (ESL, exam prep, etc.)
- [ ] Multi-turn conversation evaluation
- [ ] Compare against other pedagogical models
- [ ] A/B testing framework for real users

## References

- Base model: [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)
- Dialog-v1: [milwright/qwen-8b-dialog-v1](https://huggingface.co/milwright/qwen-8b-dialog-v1)
- Magpie dataset: [Magpie-Align/Magpie-Pro-300K-Filtered](https://huggingface.co/datasets/Magpie-Align/Magpie-Pro-300K-Filtered)
