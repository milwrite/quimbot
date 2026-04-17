# JBW Eval Sidequest TODO

## Goal
Build a highly rigorous eval suite for parity with established JBW style across InDesign source, exported PDF, and visual renderings, favoring more recent issues when there is unevenness across issues.

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
