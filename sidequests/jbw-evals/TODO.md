# JBW Eval Sidequest TODO

## Goal
Build a highly rigorous eval suite for parity with established JBW style across InDesign source, exported PDF, and visual renderings, favoring more recent issues when there is unevenness across issues.

## Primary target
Use the published **JBW 44.1 Reifman article** as the concrete article-level test case.
Treat article-level parity as distinct from full-issue parity.

### Article-level target reminders
- target article: **Reifman (P2)**
- article-level geometry target discussed in coordination:
  - **32 pages**
  - **432 × 648 pt**
- do **not** confuse this with full-issue trim parity

## Scope
- Exact page dimensions and exact placement/alignment checks
- Figure and table structures, conventional placement, and consistency with existing templates
- Typography parity:
  - font family
  - font size
  - italics and bold styling parallelism
  - line spacing
  - paragraph spacing
  - margins / columns / gutters
  - running heads / folios / section markers
- Visual parity across rendered pages and spreads
- InDesign-aware checks, with future MCP-assisted inspection where available
- Browser and vision testing of current layout outputs

## Inputs / context to inspect
- `~/Desktop/JBW/` for:
  - existing issues
  - output examples
  - InDesign resources
  - templates
- Existing Petrarch eval assets mentioned in Discord:
  - `~/Desktop/JBW/evals/jbw_parity_suite.py`
  - `~/Desktop/JBW/evals/jbw_visual_eval.py`
  - supporting README / metadata templates / scripts

## Immediate tasks
- [ ] Mirror or inventory `~/Desktop/JBW/` structure from the current machine that has it
- [ ] Create a local research inventory of JBW issues, templates, and output examples
- [ ] Compare candidate PDFs directly against the currently published Reifman article on the JBW site
- [ ] Avoid redundant re-sourcing of InDesign automation resources already covered by the current MCP / UXP path
- [ ] Define parity dimensions at three layers:
  - [ ] InDesign structural metadata
  - [ ] PDF extracted geometry/text/layout heuristics
  - [ ] vision-based rendered parity
- [ ] Add explicit checks for:
  - [ ] exact page size / trim size
  - [ ] page element positions by region and tolerance bands
  - [ ] figure/table caption placement and spacing conventions
  - [ ] paragraph spacing / leading / style continuity
  - [ ] bold / italic usage continuity against prior issues
  - [ ] font-size ladder and style-map consistency
- [ ] Prefer recent issues as canonical when older issues disagree
- [ ] Write result logs for each eval run
- [ ] Add short-view loop: candidate-level fast checks
- [ ] Add long-view loop: issue-over-issue trend analysis and drift detection
- [ ] Add placeholders for InDesign MCP integration points
- [ ] Add placeholders for browser/vision inspection of rendered layouts

## Programmatic eval roadmap
- [ ] `inventory_jbw_assets.py` — crawl issues/templates/examples and build corpus manifest
- [ ] `extract_pdf_layout_features.py` — page geometry, text blocks, spacing, style heuristics
- [ ] `compare_issue_style_profiles.py` — derive recent-issue canonical profile and compare candidates
- [ ] `run_jbw_eval_loop.sh` — repeatable runner with logs
- [ ] `logs/` — timestamped result outputs and summaries
- [ ] `reports/` — rolling parity summaries and recommendations

## Reifman parity scorecard
### 1. Geometry match
- [ ] page count matches target article
- [ ] page size / trim matches target article
- [ ] margins match within tolerance
- [ ] text-block width / height match within tolerance
- [ ] opener vs body-page geometry is distinct and correct
- [ ] running head / folio coordinates match within tolerance
- [ ] frame / object coordinates match within tolerance bands

### 2. Style-system match
- [ ] paragraph style inventory parity
- [ ] character style inventory parity
- [ ] object style inventory parity
- [ ] font-size ladder parity
- [ ] leading / line-spacing parity
- [ ] paragraph spacing before/after parity
- [ ] bold / italic behavior parity
- [ ] caps / small-caps behavior parity where applicable

### 3. Structural match
- [ ] opener page structure matches target
- [ ] title / author / abstract / keywords treatment matches target
- [ ] introduction treatment matches target
- [ ] body-page structure matches target
- [ ] figure treatment matches target
- [ ] table treatment matches target
- [ ] blockquote treatment matches target
- [ ] references treatment matches target
- [ ] about-the-author treatment matches target

### 4. Flow / composition match
- [ ] no overset text
- [ ] no collapsed spacing
- [ ] no broken paragraph joins
- [ ] line endings / reflow broadly stable
- [ ] figure / table anchoring behaves conventionally

### 5. Visual match
- [ ] opener page visually matches target strongly
- [ ] representative body pages visually match target strongly
- [ ] figure/table pages visually match target strongly
- [ ] references page visually matches target strongly

### 6. Native-source confidence
- [ ] native InDesign DOM extraction available
- [ ] plugin connected
- [ ] extraction successful against live doc
- [ ] style / geometry facts logged from actual document

## Completion levels
- [ ] Level 0 — Scaffold: target named, spec exists, files exist
- [ ] Level 1 — Operational: loop runs, logs and review packets generate
- [ ] Level 2 — Structurally matched: all article forms present in correct places
- [ ] Level 3 — Geometrically matched: page/text-block/frame geometry within tolerance
- [ ] Level 4 — Style matched: typography/spacing/style behavior materially parallel
- [ ] Level 5 — Reifman parity pass: geometry + structure + style + visual checks all pass strongly

## Cron / automation plan
- [ ] Schedule recurring cron runner to continue:
  - corpus inventory refresh
  - eval reruns
  - result logging
  - iterative TODO refinement
- [ ] Keep runs safe when `~/Desktop/JBW/` is unavailable on this machine

## Notes
- If there is unevenness across issues, weight more recent JBW issues more heavily.
- Treat this as both a regression harness and a style-spec extraction system.
