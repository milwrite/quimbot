# TODO.md — Quimbot Workspace

## Next session (2026-02-16)
- [ ] Inspect `fine-tuning/data/_audit_20260215_1900/toefl_report.json` (or equivalent) and categorize the **30 issues** (auto-fixable vs filter vs regen).
- [ ] Decide dedup policy for synth followups:
  - [ ] message-level hash on full `messages` (hard dedup)
  - [ ] keep duplicates as implicit weighting
- [ ] Produce a training-ready Stage 1 mix (scripted + reproducible):
  - [ ] use `fine-tuning/prepare_stage1_mix_hf.py` + pinned dataset IDs
  - [ ] record exact ratios + seeds in a small config note
- [ ] Fix OpenRouter billing / key routing so 4–8 turn generations can resume without 402.
- [ ] Run a small Stage 1 LoRA pilot (e.g., 5k–20k examples) to validate loss + checkpoint saving.

## Backlog
- [ ] Add automated dataset quality metrics (length histograms, role sequence checks, empty content, tool-call anomalies).
- [ ] Add dedup module (exact + near-dup) for ChatML JSONL.
- [ ] Start TOEFL11 extraction for scaffolding patterns (if synth regen needed).
