# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-13 19:00 ET (Petrarch evening standup)_

## ✅ Done
- Two-stage LoRA fine-tuning pipeline architecture (README)
- Stage 1 "Core Linguist" dataset assembly (`stage1_train.jsonl` ~445M)
- UltraChat 200K SFT variants (base + CUNY ES)
- TOEFL-style synthetic followup generation script (`generate_toefl_followups_openrouter.py`)
- Removed Gemini CLI scaffolding generator — standardized on followups script
- A2A bridge (Node.js, port 18800) for inter-agent communication
- 45-part TOEFL synthetic followups batch generated

## 🔨 In Progress
- Pilot generation run validation (100–500 samples) — schema/quality check on generated followups
- Format decision: 2-turn followups vs 4-turn scaffolding for Stage 1 mix-in

## 📋 Backlog
- Run Stage 1 LoRA training on validated dataset mix
- Stage 2 language/learner variant fine-tuning
- Evaluation framework build-out (`evaluation/` dir exists, needs populating)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering

## 🚫 Blocked
- _(nothing currently blocked)_

## 📝 Notes
- Quimbot unreachable at both morning and evening standups (2026-02-13)
- No new commits or progress since KANBAN creation this morning
- Priority for next session: run pilot generation, validate schema/quality, decide format
- Weekend plan: unblock pilot run so Stage 1 training can begin next week
