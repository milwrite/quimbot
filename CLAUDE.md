# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Protocol

- Follow **agents/COLLABORATION.md** protocol for multi-agent coordination
- Update **agents/KANBAN.md**, **agents/STATUS.md**, **agents/DEVLOG.md**, **agents/RUNLOG.md** after each significant action
- Always include commit hash **and** direct GitHub file link in Discord updates
- Never commit datasets or large artifacts to Git

## Agent Documentation

All agent coordination files are in the `agents/` subdirectory:

- **agents/COLLABORATION.md** - Multi-agent workflow protocol
- **agents/KANBAN.md** - Project board and stand-up notes
- **agents/STATUS.md** - Real-time status updates
- **agents/DEVLOG.md** - Timestamped work log
- **agents/RUNLOG.md** - Training run history
- **agents/NEXT-ACTIONS.md** - Prioritized action items

## Project Structure

```
quimbot/
├── README.md              # Project overview
├── CLAUDE.md              # This file (agent instructions)
├── agents/                # Agent coordination docs
├── evaluation/            # Model evaluation framework
├── fine-tuning/           # Training scripts and workflows
├── datasets/              # Training data (not committed)
├── checkpoints/           # Model checkpoints (not committed)
└── research/              # Research notes and plans
```

## Commands

### Evaluation (recommended: v2)
```bash
pip3 install -r evaluation/requirements-eval.txt
python3 evaluation/qwen-eval-v2.py --models qwen2.5:8b --verbose
python3 evaluation/qwen-eval-v2.py --config evaluation/eval-config-example.yaml --workers 8 --cache
```

### Fine-tuning (requires Python 3.11+)
```bash
python3.11 -m pip install -r fine-tuning/requirements.txt --user
python3.11 fine-tuning/prepare_stage1.py
python3.11 fine-tuning/run_tinker_lora.py --data stage1_mix_200k.jsonl --batch 64 --rank 16 --save-every 50
python3.11 fine-tuning/test_lora_model.py --lora-weights checkpoints/lora_*/final_lora_weights --compare-base
```

### A2A Bridge (Node.js, zero dependencies)
```bash
node a2a-bridge.mjs                    # listens on 0.0.0.0:18800
A2A_PORT=9000 node a2a-bridge.mjs      # custom port
```

## Architecture

- **fine-tuning/run_tinker_lora.py** — primary training script; uses `tinker.ServiceClient`, converts JSONL ChatML → token streams with loss masking on assistant tokens only, saves checkpoints to `tinker://` URIs
- **evaluation/qwen_eval/** — evaluation package: `core.py` (engine + parallel workers + caching), `metrics.py` (15+ metrics), `test_suites.py` (4 built-in suites), `reporters.py` (JSON/Markdown/Comparison)
- **a2a-bridge.mjs** — standalone HTTP server exposing OpenClaw via Google A2A protocol (JSON-RPC: `tasks/send`, `tasks/get`, `tasks/cancel`), proxies to `http://127.0.0.1:18789/v1/chat/completions`

## Data & Environment

- Training data is JSONL in ChatML format (OpenAI-style messages). Datasets (*.jsonl, ~4.5GB) and model files (*.gguf) are gitignored.
- Required env vars for training: `TINKER_API_KEY`, `TINKER_API_BASE`, `HF_TOKEN`
