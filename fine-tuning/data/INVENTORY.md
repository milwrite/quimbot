# Dataset Inventory
_Updated: 2026-03-27 17:00 ET_

## Active Superset (use this for training)

| File | Rows | Notes |
|------|------|-------|
| `toefl_superset12_merged_20260327.jsonl` | 76,419 | **Canonical superset as of 2026-03-27.** Superset11 + batch_20260327_merged (10,413 new unique records). 0 dupes, 0 parse errors. New error categories: CE (time/date prepositions), CF (make/do), CG (say/tell), CH (comparison errors), CI (demonstrative pronoun agreement), CJ (possessive adjective), CK (ago/before/earlier), CL (participle confusion bored/boring), CM (there-is/it-is), CN (come/go), BU (causative make/let/have to-V), BV (reported question word order), BW (neither-or/either-nor), BX (discourse connectors), BY (conditional tense mixing), BZ (quantifier SV agreement), CD (adjective-adverb confusion). Additional new domains: medical/healthcare, legal/courtroom, business/corporate, technology/IT, school-age education. |
| `toefl_superset11_merged_20260325.jsonl` | 66,006 | Superseded by superset12. Superset10 + batch_20260325, deduped. 0 parse errors. |
| `toefl_superset10_merged_20260324.jsonl` | 59,509 | Superseded by superset11. 0 parse errors. |
| `toefl_superset9_merged_20260321.jsonl` | 45,555 | Superseded by superset10. 0 parse errors. |
| `toefl_superset8_merged_20260320.jsonl` | 46,943 | Superseded by superset9. 0 parse errors. |
| `toefl_superset7_merged_20260317.jsonl` | 39,133 | Superseded by superset8. 0 parse errors. |
| `toefl_batch_20260327_merged.jsonl` | 10,413 | **New batch (2026-03-27).** Off-day generation. 7 generation scripts (v1-v7). 17 new error categories (BU-BZ, CD-CN). New domains: medical, legal, business, IT, school. 0 parse errors. Merged into superset12. |
| `toefl_batch_20260325.jsonl` | 10,000 | **Batch (2026-03-25).** Off-day generation. 12 new error categories: BI (modal perfect wrong participle), BJ (passive voice formation), BK (that-clause connector omission), BL (double negative expanded), BM (comparative/superlative form), BN (word form/false cognate), BO (quantifier + uncountable mismatch), BP (progressive with stative verbs), BQ (relative clause pronoun), BR (article with titles + pleonastic pronoun), BS (preposition after adjective expanded), BT (parallel structure). Deduped against superset10 (3,503 dupes removed from 13,503 raw). 0 parse errors. |
| `toefl_batch_20260321.jsonl` | 10,000 | **Batch (2026-03-21).** Off-day generation. 10 new error categories: stative verb progressive (AA), countable/uncountable (AB), verb complementation (AC), quantifier errors (AD), definite article overuse (AE), reflexive pronoun misuse (AF), negative inversion (AG), discourse connector errors (AH), causative verb errors (AI), possession construction (AJ). Plus expanded academic sub-patterns across SV agreement, tense, present perfect, articles, prepositions, word order, conditionals, reported speech, question formation, purpose infinitives, was/were, since+duration, gerund/inf. 0 parse errors. Deduped against superset8 (11,388 dupes removed from 56,943 raw). |
| `toefl_batch_20260319.jsonl` | 10,000 | Off-day generation 2026-03-19. 26 error categories. Merged into superset8. |

## Superset12 (completed 2026-03-27)

| Action | Status |
|--------|--------|
| Merge superset11 + toefl_batch_20260327_merged → `toefl_superset12_merged_20260327.jsonl` | **Done** |
| Rows (post-dedup) | 76,419 (0 dupes — all batch entries were already unique vs superset11) |
| Parse errors | 0 |

## Superset11 (completed 2026-03-25)

| Action | Status |
|--------|--------|
| Merge superset10 + toefl_batch_20260325 → `toefl_superset11_merged_20260325.jsonl` | **Done** |
| Rows (post-dedup) | 66,006 (3,503 dupes removed from 69,509 raw) |
| Parse errors | 0 |

## Superset9 (completed 2026-03-21)

| Action | Status |
|--------|--------|
| Merge superset8 + toefl_batch_20260321 → `toefl_superset9_merged_20260321.jsonl` | **Done** |
| Rows (post-dedup) | 45,555 (11,388 dupes removed from 56,943 raw) |
| Parse errors | 0 |

## Superset8 (completed 2026-03-20)

| Action | Status |
|--------|--------|
| Merge superset7 + toefl_batch_20260319 → `toefl_superset8_merged_20260320.jsonl` | **Done** |
| Rows (post-dedup) | 46,943 (2,190 dupes removed from 49,133 raw) |
| Parse errors | 0 |

## Source Files

| File | Raw Rows | JSON errors | Status |
|------|----------|-------------|--------|
| `combined_toefl_superset2_clean_dedup_20260219.jsonl` | 9,227 | 0 | Subsumed by superset3 |
| `toefl_superset2_merged_20260223.jsonl` | 14,566 | 0 | Subsumed by superset3 |
| `toefl_synth_10k_20260222_1120.jsonl` | 10,000 | 0 | Subsumed by superset3 |
| `toefl_ollama_10k.jsonl` | 120 | 0 | Subsumed by superset3 (+40 unique) |
| `toefl_ollama_batch_20260224_2130_clean.jsonl` | 21 | 0 | Subsumed by superset3 (+1 unique) |
| `toefl_ollama_gemma27b_10k.jsonl` | 1 | 0 | Subsumed by superset3 (+0 unique) |
| `toefl_ollama_batch_20260224_2130.jsonl` | 51 | 0 | Raw (unclean version of _clean above) |
| `toefl_superset4_merged_20260311.jsonl` | 17,549 | 0 | Subsumed by superset5 |
| `toefl_superset3_merged_20260227_0701.jsonl` | 5,560 | 0 | Subsumed by superset4 |
| `superset3_cleaned.jsonl` | 5,550 | 0 | Subsumed by superset4 (10 degenerate entries stripped) |
| `toefl_gptoss20b_10k.jsonl` | 11,999 | 0 | Subsumed by superset4 |
| `toefl_kimik2_10k.jsonl` | 1,503 | 0 | Subsumed by superset5 |
| `toefl_ollama_qwen8b_batch_20260313.jsonl` | 81 | 0 | Subsumed by superset5 |
| `toefl_batch_20260315.jsonl` | 10,000 | 0 | Merged into superset6 |
| `toefl_batch_20260317.jsonl` | 10,000 | 0 | New — pending merge into superset7 |

## In-Progress Generation

| File | Rows (live) | Model | Status |
|------|-------------|-------|--------|
| `toefl_batch_20260319.jsonl` | 10,000 | programmatic (Python) | **Complete — awaiting superset8 merge** |

## Prior In-Progress (now complete)

| File | Rows (live) | Model | Status |
|------|-------------|-------|--------|
| `toefl_batch_20260317.jsonl` | 10,000 | programmatic (Python) | **Complete — merged into superset7** |
| `toefl_batch_20260315.jsonl` | 10,000 | programmatic (Python) | **Complete — merged into superset6** |

## Misc / Scaffolding

| File | Rows | Notes |
|------|------|-------|
| `scaffolding_1000.jsonl` | 29 | Small scaffolding set |
| `proof_of_concept_10.jsonl` | 10 | Minimal POC |
| `test_scaffolding.jsonl` | 2 | Test set |
| `scaffolding_kimi_k2.5_50.jsonl` | 0 | Empty placeholder |

## QA Flags (2026-03-04)

| File | Lines | Notes |
|------|-------|-------|
| `superset3_flagged_short_lines.txt` | 10 line indices | Degenerate/short replies flagged for review |

## Dedup Summary (2026-02-27)

- **Raw lines across all source files:** ~34,941
- **Intra-baseline duplicates found:** 28,274
- **Unique entries in superset3:** 5,560
- **Dedup key:** MD5 of first user message (lowercased, stripped)
- **New Ollama entries added:** 41 (out of 142 candidate lines)

## Notes

- Superset3 is the canonical training-ready file. All new generation output (`toefl_gptoss20b_10k.jsonl`) should be folded in once generation completes via another merge+dedup pass.
- `toefl_ollama_batch_20260224_2130.jsonl` (raw) is superseded by the `_clean` version; both subsumed by superset3.
