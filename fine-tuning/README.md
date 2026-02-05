# Fine-tuning (Tinker SDK)

This folder contains a minimal pipeline to:
1) Pull a dialog dataset from Hugging Face
2) Convert it to JSONL chat format
3) Train using the official Tinker Python SDK

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch fine-tune with the Tinker SDK (defaults target qwen-8b-dialog)
python fine_tune_tinker.py
```

## Environment

Set these in `fine-tuning/.env` (already created):
- `TINKER_API_KEY`
- `HF_TOKEN`

Optional:
- `TINKER_API_BASE` (default: `https://tinker.thinkingmachines.dev/services/tinker-prod`)
  - Used by the Tinker SDK ServiceClient

## Defaults

- Dataset: `HuggingFaceH4/ultrachat_200k` (train_sft split)
- Output JSONL: `/home/milwrite/molt/ultrachat_200k_train_sft.jsonl`
- Base model: `Qwen/Qwen3-8B`
- Tinker model suffix: `qwen-8b-dialog`

If you want a different dataset or model name, pass flags:

```bash
python fine_tune_tinker.py \
  --data /home/milwrite/molt/ultrachat_200k_train_sft.jsonl \
  --base-model Qwen/Qwen3-8B \
  --suffix qwen-8b-dialog
```
