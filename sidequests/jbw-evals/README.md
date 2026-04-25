# JBW Evals Sidequest

This directory tracks work to build a rigorous JBW parity evaluation system across InDesign, PDF, and visual rendering layers.

## Current status
This machine does not currently expose `~/Desktop/JBW/`, so this sidequest is scaffolded first and should connect to the real corpus on the machine where that path exists.

## Primary test case
The concrete article-level target is the published **JBW 44.1 Reifman article**.
This sidequest should judge progress against that article, not only against generic JBW assumptions.

## Source-of-truth order
1. native InDesign DOM
2. exported PDF
3. visual/browser review

## Completion model
Use a measurable progression:
- Level 0 — Scaffold
- Level 1 — Operational
- Level 2 — Structurally matched
- Level 3 — Geometrically matched
- Level 4 — Style matched
- Level 5 — Reifman parity pass

## Planned components
- corpus inventory
- style profile extraction
- PDF geometry/layout checks
- visual LLM evaluation prep
- browser/render inspection hooks
- InDesign MCP integration hooks
- recurring cron loop with logs and reports
- article-level Reifman parity scorecard
