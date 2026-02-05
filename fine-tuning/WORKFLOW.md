# LoRA Fine-Tuning Workflow

**Complete pipeline for training and evaluating LoRA models with Tinker SDK**

---

## Setup

### 1. Python Version
**Requirement:** Python 3.11 or higher (Tinker SDK doesn't support 3.9)

```bash
# Check version
python3.11 --version

# If not available, install:
brew install python@3.11  # macOS
```

### 2. Install Dependencies
```bash
cd fine-tuning
python3.11 -m pip install -r requirements.txt --user
```

### 3. Set Environment Variables
```bash
export TINKER_API_KEY="your-key-here"
export TINKER_API_BASE="https://tinker.thinkingmachines.dev/services/tinker-prod"
```

---

## Step 1: Prepare Training Data

Convert HuggingFace datasets to JSONL format:

```bash
python3.11 prepare_data.py \
  --dataset HuggingFaceH4/ultrachat_200k \
  --split train_sft \
  --output data/training_data.jsonl \
  --max-examples 10000
```

**Output:** JSONL file with OpenAI-style `{"messages": [...]}` format

---

## Step 2: Train LoRA Model

### Quick Test Run (2 steps)
```bash
python3.11 train_and_save_lora.py \
  --data data/training_data.jsonl \
  --batch 4 \
  --max-steps 2 \
  --output-dir checkpoints
```

### Full Training Run (100-500 steps)
```bash
python3.11 train_and_save_lora.py \
  --data data/training_data.jsonl \
  --batch 64 \
  --max-steps 500 \
  --rank 16 \
  --learning-rate 1e-4 \
  --save-every 50 \
  --output-dir checkpoints
```

**Parameters:**
- `--batch`: Batch size (64 recommended)
- `--max-steps`: Number of training steps (0 = full epoch)
- `--rank`: LoRA rank (16-32 typical)
- `--learning-rate`: Learning rate (1e-4 default)
- `--save-every`: Save checkpoint every N steps

**Output:**
```
checkpoints/lora_Qwen_Qwen3-8B_20260204_230000/
├── config.json                  # Training configuration
├── training_log.json            # Loss metrics per step
├── checkpoint_step_50/          # Intermediate checkpoint
├── checkpoint_step_100/
├── final_lora_weights/          # Final LoRA weights (use this for inference)
└── training_state/              # Full training state (for resumption)
```

---

## Step 3: Test LoRA Model

### Test LoRA Only
```bash
python3.11 test_lora_model.py \
  --base-model Qwen/Qwen3-8B \
  --lora-weights checkpoints/lora_Qwen_Qwen3-8B_*/final_lora_weights \
  --output lora_test_results.json
```

### Compare LoRA vs Base Model
```bash
python3.11 test_lora_model.py \
  --base-model Qwen/Qwen3-8B \
  --lora-weights checkpoints/lora_Qwen_Qwen3-8B_*/final_lora_weights \
  --compare-base \
  --output comparison_results.json
```

**Parameters:**
- `--compare-base`: Also test base model for side-by-side comparison
- `--test-prompts`: Path to custom prompts JSON (optional)
- `--max-tokens`: Max tokens per response (default: 150)
- `--temperature`: Sampling temperature (default: 0.7)

**Output:**
```json
{
  "base_model": "Qwen/Qwen3-8B",
  "lora_weights": "checkpoints/.../final_lora_weights",
  "results": [
    {
      "prompt": [{"role": "user", "content": "Hello!"}],
      "lora_response": "Hello! How can I help you today?",
      "base_response": "Hi there! What can I do for you?"
    }
  ]
}
```

---

## Complete Example

```bash
# 1. Prepare data (10K examples)
python3.11 prepare_data.py \
  --dataset HuggingFaceH4/ultrachat_200k \
  --split train_sft \
  --output data/ultrachat_10k.jsonl \
  --max-examples 10000

# 2. Train LoRA (100 steps, save every 25)
python3.11 train_and_save_lora.py \
  --data data/ultrachat_10k.jsonl \
  --batch 64 \
  --max-steps 100 \
  --save-every 25 \
  --rank 16

# 3. Test and compare
python3.11 test_lora_model.py \
  --lora-weights checkpoints/lora_Qwen_Qwen3-8B_*/final_lora_weights \
  --compare-base \
  --output results.json

# 4. Review results
cat results.json | python3 -m json.tool | less
```

---

## Troubleshooting

### Python Version Error
```
ERROR: Package 'tinker' requires a different Python: 3.9.6 not in '>=3.11'
```
**Fix:** Use `python3.11` instead of `python3`

### Missing TINKER_API_KEY
```
❌ Missing TINKER_API_KEY in environment
```
**Fix:**
```bash
export TINKER_API_KEY="your-key"
```

### Silent Failures
**Symptom:** Script hangs with no output
**Fix:** Add `print()` statements to debug or check network connectivity

---

## Next Steps After Testing

1. **Evaluate Quality:**
   - Compare LoRA vs base outputs
   - Check if LoRA shows improvement on dialogue tasks
   - Look for overfitting (LoRA too similar to training data)

2. **Iterate:**
   - Adjust `--rank` (higher = more capacity, slower)
   - Adjust `--learning-rate` (lower if unstable)
   - Increase `--max-steps` for better convergence

3. **Deploy:**
   - Use best checkpoint for inference
   - Document performance metrics
   - Share results with team

---

## File Reference

| Script | Purpose |
|--------|---------|
| `prepare_data.py` | Convert HuggingFace datasets → JSONL |
| `train_and_save_lora.py` | Train LoRA model with full checkpointing (local + Tinker) |
| `test_lora_model.py` | Generate responses and compare models |
| `run_tinker_lora.py` | Lightweight training with `--save-every` checkpoints to Tinker |
| `inspect_tinker_api.py` | Debug Tinker SDK methods |

### run_tinker_lora.py Options (Updated 2026-02-05)

```bash
python3.11 run_tinker_lora.py \
  --data data/training_data.jsonl \
  --batch 32 \
  --max-steps 100 \
  --save-every 25 \
  --rank 16
```

- `--save-every N`: Save checkpoint every N steps (0 = only final)
- Always saves `final` checkpoint at end
- Checkpoint names: `step_0025`, `step_0050`, `final` (alphanumeric only)
- Prints all `tinker://` paths at completion

---

**Last Updated:** 2026-02-05 10:25 EST
**Status:** Ready for production training runs (checkpoint saving fixed)
