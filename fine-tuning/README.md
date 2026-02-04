# Fine-tuning (Tinker API)

This folder contains a minimal pipeline to:
1) Pull a dialog dataset from Hugging Face
2) Convert it to JSONL chat format
3) Upload + launch a Tinker fine-tune

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Build dataset + launch fine-tune (defaults target qwen-8b-dialog)
python fine_tune_tinker.py
```

## Environment

Set these in `fine-tuning/.env` (already created):
- `TINKER_API_KEY`
- `HF_TOKEN`

Optional:
- `TINKER_API_BASE` (default: `https://api.tinker.ai/v1`)

## Defaults

- Dataset: `HuggingFaceH4/ultrachat_200k` (train_sft split)
- Output JSONL: `data/ultrachat_200k_train_sft.jsonl`
- Tinker model name (suffix): `qwen-8b-dialog`

If you want a different dataset or model name, pass flags:

```bash
python fine_tune_tinker.py \
  --dataset HuggingFaceH4/ultrachat_200k \
  --split train_sft \
  --model qwen-8b-dialog
```
