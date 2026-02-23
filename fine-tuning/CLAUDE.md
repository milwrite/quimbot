# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

LoRA fine-tuning pipeline for Qwen3-8B using the Tinker SDK. Converts HuggingFace datasets to ChatML JSONL, trains LoRA adapters via Tinker's remote API, and evaluates results.

## Requirements

- **Python 3.11+** (Tinker SDK requires >=3.11)
- Env vars: `TINKER_API_KEY`, `TINKER_API_BASE`, `HF_TOKEN`

```bash
python3.11 -m pip install -r requirements.txt --user
```

## Commands

```bash
# Prepare data (HF datasets → ChatML JSONL)
python3.11 scripts/preparation/prepare_stage1.py
python3.11 scripts/preparation/prepare_data.py --output data/training_data.jsonl --max-examples 10000

# Train LoRA
python3.11 scripts/training/run_tinker_lora.py --data data/training_data.jsonl --batch 64 --rank 16 --save-every 50
python3.11 scripts/training/train_and_save_lora.py --data data/training_data.jsonl --batch 64 --max-steps 500 --rank 16

# Test / compare models
python3.11 scripts/testing/test_lora_model.py --lora-weights checkpoints/lora_*/final_lora_weights --compare-base
python3.11 scripts/testing/compare_models.py --lora-checkpoint checkpoints/lora_*/final_lora_weights

# Generate synthetic training data (requires OPENROUTER_API_KEY)
python3.11 scripts/generation/generate_scaffolding_v2.py --count 1000 --output data/scaffolding_v2.jsonl
```

## Directory Structure

```
fine-tuning/
├── scripts/
│   ├── preparation/    # Data conversion: HF → ChatML JSONL
│   ├── training/       # LoRA training via Tinker SDK
│   ├── generation/     # Synthetic data generation (OpenRouter API)
│   └── testing/        # Model comparison and analysis
├── data/               # Working JSONL files (small/test datasets)
├── checkpoints/        # LoRA checkpoint outputs (not committed)
└── *.md                # Workflow docs, taxonomy references
```

## Architecture

- **Training scripts** use `tinker.ServiceClient` to submit remote LoRA jobs. Data is converted from ChatML JSONL → token streams with loss masking on assistant turns only. Checkpoints save to `tinker://` URIs.
- **Preparation scripts** pull from HuggingFace datasets and write ChatML-format JSONL (`{"messages": [{"role": "...", "content": "..."}]}`). Large finalized datasets go to `../datasets/`, small working files go to `data/`.
- **Generation scripts** call OpenRouter API (Kimi K2.5, etc.) to produce synthetic scaffolding/mentor-student dialogues.
- **run_tinker_lora.py** is the primary training entry point; **train_and_save_lora.py** adds full local checkpointing on top.
