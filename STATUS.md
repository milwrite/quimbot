# Real-Time Status

**Last Update:** 2026-02-08 03:05 EST by Quimbot

## Current Task
- **[Petrarch]** Stage 1 training rerun with checkpoint saving fixed
- **[Quimbot]** Evaluation + reporting (LoRA vs base)

## Training Status
**Stage 0 (production proof run):**
- ✅ Qwen/Qwen3-8B LoRA, 63 steps
- ✅ Checkpoints saved to Tinker (`step_0010` … `final`)
- ✅ Final URI: `tinker://1d70c787-fc09-5de9-9922-4fcf062f7c80:train:0/sampler_weights/final`

**Stage 1 (mixed dataset run):**
- ⚠️ 500-step run completed but **weights not saved** (invalid checkpoint name format)
- ✅ Script patched to use simple labels (`step_XXXX`, `final`)
- 🔁 **Needs rerun** to persist weights

## Active Work
- ✅ Eval script fixed (`test_lora_model.py` sampling API)
- ✅ Eval run completed; outputs in `lora_test_results.json` (LoRA more concise vs base)

## Next Steps
1. Rerun Stage 1 training with fixed checkpoint labels
2. Capture and share tinker:// checkpoint URIs
3. Run eval on Stage 1 final checkpoint and post diffs

---

**Note:** Do not commit datasets to Git; datasets live in local `datasets/` only.
