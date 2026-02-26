# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Protocol

- Follow **COLLABORATION.md** protocol for multi-agent coordination
- Update **KANBAN.md**, **STATUS.md**, **DEVLOG.md**, **RUNLOG.md** after each significant action
- **Update `dataset_review.md` after every training or evaluation run** — document dataset composition changes, new/removed datasets, and data quality observations
- Always include commit hash **and** direct GitHub file link in Discord updates
- Never commit datasets or large artifacts to Git

## Agent Documentation

Agent coordination files are in the project root:

- **COLLABORATION.md** - Multi-agent workflow protocol
- **KANBAN.md** - Project board and stand-up notes
- **STATUS.md** - Real-time status updates
- **DEVLOG.md** - Timestamped work log
- **RUNLOG.md** - Training run history
- **NEXT-ACTIONS.md** - Prioritized action items

## Project Structure

```
molt/
├── README.md              # Project overview
├── CLAUDE.md              # This file (agent instructions)
├── dataset_review.md      # Dataset review notes (UPDATE AFTER EVERY RUN)
├── COLLABORATION.md       # Multi-agent workflow protocol
├── KANBAN.md              # Project board
├── STATUS.md              # Real-time status
├── DEVLOG.md              # Timestamped work log
├── RUNLOG.md              # Training run history
├── NEXT-ACTIONS.md        # Prioritized action items
├── LoRA-ROADMAP.md        # LoRA training roadmap
├── evaluation/            # Model evaluation framework
├── fine-tuning/           # Training scripts, workflows, and working JSONL data
├── datasets/              # Training data JSONL files (not committed)
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
python3.11 fine-tuning/run_tinker_lora.py --data datasets/stage1_mix_200k.jsonl --batch 64 --rank 16 --save-every 50
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
- **Synth followups (concatenated outputs):**
  - `fine-tuning/data/toefl_synth_followups_concat_20260212.jsonl` (5742 lines)
  - `fine-tuning/data/pilot_concat_20260212.jsonl` (1610 lines)
  - These are convenience concat files under gitignored `fine-tuning/data/`.
- **QA/Audit helpers (reproducible):**
  - `fine-tuning/qa_followups_jsonl.py` (fast schema/sanity scan)
  - `fine-tuning/consolidate_followups.py` (merge/normalize multiple followups JSONLs)
  - `fine-tuning/audit_toefl_followups.py` (deeper audit; issue + dupe counts)
- Required env vars for training: `TINKER_API_KEY`, `TINKER_API_BASE`, `HF_TOKEN`

## 2026-02-16 notes (recent decisions / state)
- Synth followups audit triage (see `agents/KANBAN.md`): TOEFL concat issues appear filterable:
  - 30 rows with empty assistant content
  - 2 role alternation violations
  - JSON parse errors = 0
- OpenRouter generation scaling currently blocked by HTTP 402; do not assume generation scripts will run until billing/key routing is fixed.
- Stage 1 mix decision pending: whether to hard-dedup synth followups or keep duplicates as implicit weighting.
- Repo hygiene: sidequest microlearning scripts exist under `sidequests/microlearning/`; do not commit `sidequests/microlearning/data/` artifacts (treat like datasets/output).

## 2026-02-24 notes (nightly review)
- Nightly stocktake completed and committed (`4efefe28`): added `fine-tuning/data/INVENTORY.md` with per-file row counts and dedup status.
- Dataset state re-confirmed at 33,834 rows across 7 tracked JSONL files in `fine-tuning/data/`.
- Evaluation scripts were syntax-validated (`evaluation/qwen-eval.py`, `evaluation/qwen-eval-v2.py`) and are execution-ready once weights land.
- New generation utility scaffold added: `fine-tuning/scripts/generation/generate_toefl_ollama_10k.py` for local Ollama batch synthesis.
- Hard blocker remains unchanged: Stage 1 Run 4 adapter weights are not on local disk (day 2 blocked).
- Secondary blocker remains: OpenRouter HTTP 402 prevents scale-out synthetic generation.

## 2026-02-25 notes (morning review)
- Overnight local generation added three fresh outputs with +156 rows total (`92 + 51 + 13`).
- Quick validation pass confirmed `toefl_ollama_batch_20260224_2130_clean.jsonl` at 21/21 valid rows.
- Working total reported in stand-up context is now 34,011 rows before dedup merge finalization.
- Immediate next data task: merge new outputs into a staging JSONL, dedup against current superset, then refresh `fine-tuning/data/INVENTORY.md`.
- Highest-priority execution path is unchanged: Run 4 checkpoint eval starts as soon as adapter weights (step 350 + final) are available locally.

## 2026-02-25 notes (evening review)
- No additional commits landed during daytime; progress concentrated on coordination, status hygiene, and handoff prep.
- Nightly trend artifact added at `reports/nightly/stocktake-2026-02-25.md` (branch, delta, dataset location snapshot).
- The execution queue for next cycle is explicit: merge + dedup + recount first, then immediate eval trigger once weights are provided.
- Blocking conditions are unchanged: missing local adapter weights for Run 4 eval and OpenRouter HTTP 402 for scale-out generation.
