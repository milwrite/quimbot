# Consolidated datasets (Legion / this workspace)

This note consolidates the main corpora used/available for Stage 1 tuning with Tinker (PEFT/LoRA), and clarifies what lives locally vs what is downloaded from HuggingFace.

## Local (already present on disk)

All of these live under `fine-tuning/data/` (gitignored; do not commit to repo).

### UltraChat
- `fine-tuning/data/ultrachat_200k_train_sft.jsonl` (~500M)
- `fine-tuning/data/ultrachat_200k_train_sft_cuny_es.jsonl` (~1.3G)

### Stage 1 mixed dataset (current)
- `fine-tuning/data/stage1_train.jsonl` (~445M)

### TOEFL-style synthetic follow-ups
- 2-turn, OpenRouter/Gemini-3-Flash: `fine-tuning/data/toefl_synth_followups_5k_2turn_gemini3flash_openrouter_20260212_1922.jsonl` (5,000 lines)
- Earlier small parts: `fine-tuning/data/toefl_synth_followups_10_part*_*.jsonl` (many small files)
- Earlier small pilot: `fine-tuning/data/toefl_synth_followups_100part1_20260211_2301.jsonl` (54 lines)

### TOEFL scaffolding
- `fine-tuning/scaffolding_1000.jsonl` (~18K)
- `fine-tuning/test_scaffolding.jsonl` (~1.1K)

## HuggingFace datasets to download for the Stage 1 mix

These are NOT currently stored in `fine-tuning/data/` as JSONL by default; we should download/convert them into the unified Stage 1 mix file.

- Prosocial Dialog: `allenai/prosocial-dialog`
- LMSYS Chat 1M: `lmsys/lmsys-chat-1m`
- Magpie: `Magpie-Align/magpie-llama-3.1-pro-300k-filtered`
  - Note: **the correct dataset id is `...300k-filtered` (no underscore)**. The underscore variant fails.

## Unifying / preparing a single Stage 1 training mix

Script:
- `fine-tuning/prepare_stage1_mix_hf.py`

Purpose:
- Reads local UltraChat JSONLs + local TOEFL followups
- Downloads LMSYS + Magpie + Prosocial via `datasets.load_dataset`
- Converts each source into OpenAI-style chat: `{ "messages": [ {"role":...,"content":...}, ... ] }`
- Shuffles and writes a single mixed JSONL.

Recommended workflow:
1. Run a **small** mix first (sanity check schema + spot-check samples)
2. Scale up sample caps/ratios
3. Train LoRA via `train_and_save_lora.py --data <mix.jsonl>`

## Notes / gotchas

- `fine-tuning/data/` is gitignored; only commit scripts + docs.
- Some older generation outputs are 0-byte placeholders; ignore them in the mix.
- Our Tinker training script saves sampler weights (`tinker://.../sampler_weights/...`). The `save_state` call currently fails because it passes a filesystem path; it needs a Tinker-safe label.
