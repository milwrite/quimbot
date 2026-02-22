# Quimbot

A workspace for the Orchestra project: staged LoRA fine-tuning for language-learning assistants, a creative coding gallery, and assorted side quests.

**Live gallery:** [milwrite.github.io/quimbot/gallery/](https://milwrite.github.io/quimbot/gallery/)

---

## Table of Contents

- [Fine-Tuning Pipeline](#fine-tuning-pipeline)
  - [Architecture](#architecture)
  - [Training Data](#training-data)
  - [Scripts & Tooling](#scripts--tooling)
  - [Evaluation Framework](#evaluation-framework)
- [Creative Coding Gallery](#creative-coding-gallery)
- [Reddit Scraper & Microlearning](#reddit-scraper--microlearning)
- [Openclaw Integration](#openclaw-integration)
- [Models](#models)
- [Side Quests](#side-quests)
- [Project Structure](#project-structure)
- [Data Policy](#data-policy)
- [Current Status](#current-status)

---

## Fine-Tuning Pipeline

Two-stage LoRA fine-tuning on Qwen-8B to build pedagogically-aware conversational models.

### Architecture

```
Qwen/Qwen3-8B-Base
       ↓
[Stage 1: Core Linguist Model]
       ↓
Qwen-8B-Linguist (generalized conversational + pedagogical behaviors)
       ↓
[Stage 2: Language-Specific Variants]
       ↓
├─ Qwen-8B-Spanish-Heritage
├─ Qwen-8B-Spanish-L2
├─ Qwen-8B-Mandarin-Heritage
└─ ... (scalable variants)
```

**Stage 1** establishes foundational capabilities: natural turn-taking, complexity adaptation, scaffolding strategies, and multilingual grounding.

**Stage 2** applies secondary fine-tuning for specific language/learner pairs (heritage speakers, L2 learners) with targeted corpora.

The pedagogical approach favors **scaffolding over correction**: recasting, questioning, hinting, and encouraging exploration rather than explicit error flagging.

### Training Data

Stage 1 mix: **43,175 records** (`fine-tuning/data/stage1_mix_v2_20260220.jsonl`)

| Source | Share | Records | Purpose |
|--------|-------|---------|---------|
| LMSYS Chat-1M | 40.8% | ~17,600 | Real conversational patterns (154 languages) |
| Magpie-300K | 25.5% | ~11,000 | Instruction-following quality |
| TOEFL Superset | 20.4% | ~8,800 | Learner error patterns + scaffolding |
| Prosocial Dialog | 10.2% | ~4,400 | Safety/ethics grounding |
| Pilot (custom) | 3.2% | ~1,370 | Synthetic pedagogical dialogues |

All sources are hard-deduped by message hash. Build script and manifest: `fine-tuning/build_stage1_mix.py`.

### Scripts & Tooling

| Script | Purpose |
|--------|---------|
| `fine-tuning/run_tinker_lora.py` | Main LoRA training loop |
| `fine-tuning/build_stage1_mix.py` | Stage 1 dataset mixing + dedup |
| `fine-tuning/prepare_stage1.py` | Dataset preprocessing |
| `fine-tuning/test_lora_model.py` | Base vs. fine-tuned comparison |
| `fine-tuning/generate_scaffolding_dialogues.py` | Synthetic pedagogical data generation |
| `fine-tuning/export_to_ollama.py` | Export merged model for local inference |

### Evaluation Framework

Location: [`evaluation/`](evaluation/)

15+ metrics (pedagogical quality, dialogue coherence, complexity adaptation), 4 built-in test suites, parallel execution with caching, JSON/Markdown reporters.

```bash
cd evaluation
pip3 install -r requirements-eval.txt
python3 qwen-eval-v2.py --models base-model fine-tuned-v1 --verbose
```

Docs: [evaluation/QWEN-EVAL-V2-README.md](evaluation/QWEN-EVAL-V2-README.md)

---

## Creative Coding Gallery

**Live:** [milwrite.github.io/quimbot/gallery/](https://milwrite.github.io/quimbot/gallery/)

An interactive collection of canvas-based visualizations spanning algorithmic art history, generative systems, and mathematical curiosities. Each piece is a standalone HTML file with mouse/touch interaction.

**22 artifacts** including:

- **Historical reconstructions:** Noll's Gaussian Quadratic (1965), Nake's Walk-Through Raster (1965), Molnár's (Dés)Ordres, Schotter (Georg Nees), 10 PRINT
- **Mathematical:** Harmonograph (1844), Lissajous curves, Lorenz attractor, Sierpinski triangle, L-systems
- **Simulations:** Boids flocking, Conway's Game of Life, reaction-diffusion, heat diffusion, Turing patterns
- **Other:** Chinoiserie garden, flow fields, constraint grids, starfield, Matrix rain

Source: [`docs/gallery/`](docs/gallery/)

---

## Reddit Scraper & Microlearning

Location: [`sidequests/microlearning/`](sidequests/microlearning/)

A proof-of-concept pipeline for automated microlearning content:

**Reddit ingest → topic ranking → human approval → content packet → publish**

- `scrape_reddit.py` scrapes trending posts from target subreddits
- `score_topics.py` ranks scraped topics by educational potential
- `generate_content_packets.py` produces structured learning packets from approved topics
- Schemas and examples define handoff contracts between pipeline stages

Docs: [`sidequests/microlearning/docs/`](sidequests/microlearning/docs/) covers architecture, quality gates, and a Reddit-to-Veo visual storytelling methodology.

---

## Openclaw Integration

**Clawdbot** is the orchestration layer powering agent collaboration in this project. Built on the [openclaw framework](https://github.com/clawdbot/clawdbot), it provides multi-agent coordination, Discord integration, and persistent memory.

### Key Capabilities

- **Discord Integration**  
  - Native messaging in dedicated channels (`#agent-log`, `#README.md`, etc.)
  - Real-time updates on training runs, eval results, and git pushes
  - Thread support for organized conversations
  
- **Agent-to-Agent (A2A) Tasks**  
  - Petrarch (main agent) spawns Quimbot for specialized fine-tuning work
  - Isolated sessions with dedicated context and memory
  - Background execution with result announcements
  
- **Persistent Memory**  
  - Daily memory files (`memory/YYYY-MM-DD.md`) track work history
  - `MEMORY.md` for long-term context and lessons learned
  - Heartbeat checks for proactive monitoring and maintenance
  
- **Skills & Tools**  
  - GitHub integration (`gh` CLI for commits, issues, PRs)
  - Reddit scraping and microlearning pipeline
  - Web search and research capabilities
  - Browser automation for dataset downloads

### Workflow Example

1. **Task Assignment:** Petrarch delegates "update eval framework" to Quimbot via `sessions_spawn`
2. **Execution:** Quimbot works in isolated session, commits changes, pushes to GitHub
3. **Reporting:** Quimbot posts completion + commit hash + file links to Discord
4. **Handoff:** Control returns to Petrarch with full context of changes

This architecture enables continuous development cycles without manual intervention—agents collaborate, iterate, and maintain the project autonomously.

**Documentation:** [docs.clawd.bot](https://docs.clawd.bot) | [GitHub](https://github.com/clawdbot/clawdbot)

---

## Models

Location: [`edudial/`](edudial/)

Configuration and tooling for model inference and training:

- `edudial/config/` — model and training configs
- `edudial/eval/` — evaluation harnesses
- `edudial/inference/` — inference scripts
- `edudial/xtuner/` — XTuner integration for fine-tuning

---

## Side Quests

Experimental projects in [`sidequests/`](sidequests/):

| Project | What it is |
|---------|-----------|
| **microlearning** | Reddit-to-content pipeline (see above) |
| **domain-expirations** | Dropcatch domain scraper + normalizer |
| **moltcomps** | Multi-agent site deployment experiment |
| **next/itp-lab** | ITP lab presentation deck ([live](https://milwrite.github.io/quimbot/itp-lab/)) |

---

## Project Structure

```
quimbot/
├── README.md
├── docs/
│   ├── gallery/            # Creative coding gallery (GitHub Pages)
│   │   ├── index.html      # Gallery index with iframe previews
│   │   ├── noll.html       # Noll Gaussian Quadratic (1965)
│   │   ├── nake.html       # Nake Walk-Through Raster (1965)
│   │   ├── boids.html      # Flocking simulation
│   │   └── ...             # 22 standalone artifacts
│   └── itp-lab/            # ITP lab presentation
├── fine-tuning/
│   ├── build_stage1_mix.py # Dataset mixing + dedup
│   ├── run_tinker_lora.py  # LoRA training
│   ├── data/               # Training data (gitignored)
│   └── ...
├── evaluation/             # Model evaluation framework
├── edudial/                # Model configs, inference, xtuner
├── research/               # Architecture specs, dataset research
├── sidequests/
│   ├── microlearning/      # Reddit scraper + content pipeline
│   ├── domain-expirations/ # Domain scraping
│   ├── moltcomps/          # Multi-agent deployment
│   └── next/itp-lab/       # Presentation deck
├── agents/                 # Agent coordination (KANBAN, STATUS, DEVLOG)
├── creative-coding/        # Early creative coding experiments
└── checkpoints/            # Local checkpoint cache (gitignored)
```

---

## Data Policy

Large files (datasets, checkpoints) are gitignored. Training data lives in `fine-tuning/data/`. Do not commit datasets to Git.

---

## Current Status

**Stage 1 (Core Linguist):** 🔄 Training mix finalized (43,175 records), awaiting full LoRA run  
**Stage 2 (Variants):** ⏸️ Pending Stage 1 completion  
**Gallery:** ✅ 22 artifacts live, ongoing expansion  
**Microlearning:** 🧪 POC stage, pipeline architecture defined  

**Last Updated:** 2026-02-21
