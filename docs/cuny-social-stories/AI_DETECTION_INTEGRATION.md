# AI-Detection Vignettes Integration Plan

Last updated: 2026-05-12

## Working Decision

Build the Javabot / AI-detection vignettes as a **thematic track** inside the social stories project, not as replacement material for the existing 2023-2025 yearly pages.

The current social-stories arc already uses 2023, 2024, and 2025 to show student-made scaffolding around digital breakage, advising damage, alumni care work, registration tools, federal-aid panic, and textbook costs. AI detection belongs inside that same dissertation argument, but it has a distinct rhythm: it starts in 2023, intensifies during finals and policy uncertainty, and turns writing process into an audit trail by 2024-2026. Treating it as a separate track keeps the main arc readable while letting AI detection develop at the density it needs.

No local file or text string named `javabot` was found in this workspace. The current integration sources are the AI-detection narrative files under `dissertation/narratives/`.

## Source Materials

- `dissertation/narratives/cuny-ai-detection-2023-2026.md`
- `dissertation/narratives/cuny-ai-detection-2024-supplement.md`
- `dissertation/narratives/cuny-false-positives-frustrations-2023-2026.md`
- `dissertation/narratives/writing-under-surveillance-vp-draft-v5.md`

These files already use the right evidentiary discipline for social stories: CUNY-only subreddit scope, paraphrase rather than quotation, evidence IDs for traceability, and a scene-to-system movement.

## Proposed Site Structure

Keep existing public URLs stable:

```text
cuny-social-stories/
├── index.html
├── all.html
├── 2023.html
├── 2024.html
├── 2025.html
└── ...
```

Add a parallel thematic route:

```text
cuny-social-stories/
├── _src/
│   ├── 2023.md
│   ├── ...
│   └── ai-detection/
│       ├── 2023.md
│       ├── 2024.md
│       ├── 2025.md
│       └── 2026.md
└── ai-detection/
    ├── index.html
    ├── all.html
    ├── 2023.html
    ├── 2024.html
    ├── 2025.html
    └── 2026.html
```

The main `index.html` should add a small “Thematic Tracks” section that links to `ai-detection/index.html`, while the yearly 2023-2025 pages can add a short related-track link rather than absorbing the full AI-detection material.

## Track Motif

Use a distinct motif from the main arc:

> **writing process as audit trail**

That motif is sharper than a generic AI-panic label. It names the actual student labor appearing across the source files: students save Google Docs history, Word versions, Draftback playback, screenshots, notes, old essays, detector results, and the ability to orally explain prose choices because writing is increasingly treated as something to verify after suspicion.

## Content Map

| Year | Working title | Function in the track |
| --- | --- | --- |
| 2023 | Detector Scores Become Finals Anxiety | AI detection enters through Blackboard/SafeAssign/Turnitin/Brightspace uncertainty, then becomes finals-season fear and academic-integrity defense work. |
| 2024 | Grammar, Multilingual Prose, and the Proof Burden | The issue shifts from abstract detection to style policing, Grammarly suspicion, SafeAssign template panic, WU/F risk, and department/dean escalation. |
| 2025 | Defensive Writing Becomes Routine | Students pre-check drafts, preserve edit histories, make prose less polished, and ask peers how to survive detector/instructor suspicion before formal accusation. |
| 2026 | AI Suspicion Becomes Course Metadata | Detection risk circulates before enrollment through course reviews, instructor reputations, homework enforcement warnings, and department-specific caution. |

## How It Should Relate to the Existing 2023-2025 Pages

The existing pages should stay broad:

- 2023 remains about digital breakage and career translation.
- 2024 remains about advising damage, alumni care work, and salary transparency.
- 2025 remains about registration tools, federal-aid panic, and textbook-cost workarounds.

Add one sentence or callout to each of those pages:

- 2023: AI detection begins as another vendor-layer uncertainty alongside ransomware and platform trust.
- 2024: AI detection sharpens the advising-damage page's broader claim about official misclassification and student proof burdens.
- 2025: AI detection extends the tool-building/proof-building arc from registration into writing itself.

The full AI-detection scenes should live in the thematic track, where they can accumulate without flattening the annual social-story pages.

## Builder Changes Needed

The current `build.py` assumes one main series loaded from `_src/YYYY.md`. To support the AI-detection track cleanly:

1. Add a small series configuration object for `main` and `ai-detection`.
2. Move vignette loading into a reusable function that accepts a source directory and output directory.
3. Keep current root-level outputs unchanged for the main series.
4. Render the AI-detection track into `ai-detection/`.
5. Add `series`, `motif`, and optional `source_note` frontmatter fields, while preserving compatibility with the current files.
6. Optionally generate an AI-detection `all.md` from the same source so the consolidated artifact is no longer manual.

This is a small refactor rather than a new application. The existing parser, markdown conversion, page chrome, yearly pages, index page, and single-page timeline can mostly be reused.

## Source File Shape

Use the same yearly source format, with a few additional fields:

```markdown
---
year: 2024
series: ai-detection
title: "Grammar, Multilingual Prose, and the Proof Burden"
date: 2024-01-01
motif: "writing process as audit trail"
subreddits: [CUNY, QueensCollege, Baruch, CCNY, HunterCollege]
evidence_ids:
  - submission_1dx458s
  - comment_lbzj9ov
  - submission_1h64qax
  - submission_1hpta1h
---
Opening paragraph that names the year's movement in the AI-detection arc.

Two to four anchor moments, paraphrased and tied to the proof burden.

Closing paragraph naming the broken infrastructure and linking to the adjacent year.

**Evidence**: ...
```

## Drafting Rules

- Keep the existing disguise protocol: paraphrase, do not quote Reddit prose.
- Preserve evidence IDs in every yearly source file.
- Keep "broken infrastructure" language in the drafting notes or closing paragraph; it is one of the strongest features of the AI-detection narratives.
- Do not make the track only about detector unreliability. The richer dissertation claim is about assessment, literacy crisis discourse, multilingual writing, instructor trust, and students turning writing process into evidence.
- Use the LaGuardia / Grammarly / spoken-written English case as the public-facing emblem, because `writing-under-surveillance-vp-draft-v5.md` already makes it work as a typifying vignette.

## Chapter-Level Use

This track can feed three dissertation locations:

- Chapter 1: literacy-crisis discourse, digital surveillance, and the movement from student deficiency narratives into AI suspicion.
- Chapter 2 or methods: platform affordances and evidence limits, since students are discussing detection systems through Reddit while also producing defensive records outside Reddit.
- Later findings chapter: student-made scaffolding under AI detection, where peer advice becomes a defense kit rather than only navigational help.

The key bridge sentence for chapter prose:

> Beginning in 2023, CUNY Reddit's student-made scaffolding turns toward AI detection: students do not only exchange advice about portals, holds, and registration; they learn to preserve drafts, timestamps, version histories, and explanations of style because writing itself has become an object of institutional audit.
