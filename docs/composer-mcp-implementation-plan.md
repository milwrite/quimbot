# Composer-MCP Implementation Plan

## Purpose

`diss-mcp` already does real work. It audits citations, tracks prose state, renders documents, queries research corpora, and produces tracked-changes output. The current server also carries a hard boundary: it assumes a dissertation-shaped project, a registered chapter model, and a fixed project root. That boundary blocked the Cloze Reader smoke test as soon as the target file lived in a different repo.

This plan turns `diss-mcp` into a broader writing-workflow server without losing the dissertation tools that make it valuable. The right model is a layered generalization: build a portable writing substrate, preserve dissertation-specific features as a plugin, and disaggregate the style guide into scoped analytical domains that can run as profiles across many kinds of writing.

## Core Design Decision

Do not flatten `diss-mcp` into a generic rename.

Build a general writing MCP with a dissertation plugin.

That split preserves two things at once:

- the dissertation stack stays powerful
- the writing stack becomes reusable across papers, essays, microblogs, notes, and collaborative drafts

## System Architecture

The system should have four layers.

### Layer 1. Core writing substrate

This layer owns the mechanics of writing workflow independent of genre or project.

Responsibilities:

- resolve files and sections
- detect repo roots from target files
- find the correct git base for diffs and tracked changes
- store audit history
- generate structured reports
- manage profiles and rule activation
- run readiness gates
- render exports

This layer should know nothing about dissertations, corpora, Quarto chapters, or bibliography chains unless a plugin provides them.

### Layer 2. Style-analysis engine

This layer runs the writing rules themselves.

The current style guide should be decomposed into scoped domains instead of treated as one monolithic checklist. Each domain should be independently runnable, independently reportable, and profile-aware.

Primary domains:

1. diction
2. syntax
3. argumentation
4. coherence and cohesion
5. paragraph-level organization and construction
6. genre-specific rhetoric

This decomposition matters because different writing tasks fail in different ways. A microblog may need diction and paragraph checks but no citation logic. A dissertation chapter may need all domains plus bibliography and render gates. A memo may need syntax and coherence while ignoring scholarly citation rules.

### Layer 3. Profile system

Profiles activate subsets of rules, set severities, define gates, and establish exceptions.

Examples:

- `milwrite-dissertation`
- `cloze-paper`
- `general-academic`
- `microblog`
- `composer-default`

A profile should define:

- active rule domains
- active rules within each domain
- severity thresholds
- required clean-pass conditions
- allowed exception classes
- citation expectations
- export targets
- report verbosity

### Layer 4. Project-specific plugins

Plugins carry domain knowledge that only some projects need.

The dissertation plugin should preserve:

- chapter registry
- bibliography chain audit
- corpus SQL tools
- evidence lookup
- Quarto-aware render rules
- dissertation-specific readiness gates

This plugin model lets the writing substrate stay general while the dissertation stack remains deep.

## Rule Taxonomy

The current style-guide logic should be formalized into rule families. Each rule must become inspectable, configurable, and reportable.

Suggested taxonomy:

- `DX-*` diction
- `SX-*` syntax
- `AX-*` argumentation
- `CX-*` coherence/cohesion
- `PX-*` paragraph organization
- `GX-*` genre/profile constraints

Each rule record should include:

- `id`
- `name`
- `domain`
- `description`
- `rationale`
- `trigger`
- `heuristic_limitations`
- `severity`
- `autofixable`
- `dependencies`
- `examples_pass`
- `examples_fail`
- `allowed_exceptions`

## Disaggregated Style Domains

### 1. Diction

This domain handles lexical choice and register.

Checks should include:

- banned or disallowed terms
- vague intensifiers
- jargon inflation
- nominalized subject detection where feasible
- repeated weak verbs
- terminology drift across a section
- field-inappropriate phrasing
- abstract noun overload
- overuse of empty evaluative language

Representative rules:

- banned AI-slop vocabulary
- no vague transition fillers
- no unsupported abstract praise terms
- technical term consistency across a document

### 2. Syntax

This domain handles clause structure, punctuation logic, sentence shape, and grammatical sequencing.

Checks should include:

- sentence ceiling violations
- interrupted subject patterns
- dangling modifiers
- overloaded coordination
- clause-balance failures
- separator overuse
- single-separator rule
- em dash policy
- colon policy
- semicolon misuse
- apposition overload

Representative rules:

- no single em dash pivot
- no dangling participial opener
- sentence ceiling enforced by profile
- one separator family per clause cluster unless waived

### 3. Argumentation

This domain handles claim structure, reasoning pressure, evidence, and citation logic.

Checks should include:

- earned assertion gate
- same-question test
- unsupported causal leap detection
- claim without nearby evidence
- scholar-as-agent enforcement
- false contrast detection
- false dilemma in paired citation
- mismatched evidence/claim scope
- quotation without argumentative host clause
- theory-name as prop rather than active claim

Representative rules:

- no claim language without citation or evidentiary support in relevant genres
- no fabricated contradiction between studies answering different questions
- no framework-name substitution for actual argument

### 4. Coherence and cohesion

This domain handles sentence-to-sentence and paragraph-to-paragraph movement.

Checks should include:

- bare demonstratives
- weak backward pointers
- referent drift
- thin transition sentence detection
- local sequence discontinuity
- repeated topic re-entry without advancement
- paragraph bridge weakness
- pronoun ambiguity in dense argumentative prose

Representative rules:

- `this` requires a clarifying noun
- no thin hinge sentence that merely announces movement
- no unsupported return to a prior topic without explicit reconnection

### 5. Paragraph-level organization and construction

This domain handles the internal architecture of paragraphs and local paragraph runs.

Checks should include:

- stub paragraph detection
- paragraph bloat detection
- missing topic sentence or opening move
- multi-claim paragraph overload
- weak landing sentence
- paragraph split/merge suggestions
- adjacent paragraph redundancy
- paragraph sequence logic
- false emphasis through isolated short paragraph units

Representative rules:

- no paragraph whose only work is to restate the previous one
- no argument-bearing section built from consecutive underdeveloped stub paragraphs
- no final sentence that merely paraphrases earlier material without advancing the claim

### 6. Genre and rhetoric profile

This domain carries profile-bound rules.

Examples:

- dissertation chapter requires citation-aware argument checks
- microblog requires code snippet inclusion for technical pieces
- memo tolerates shorter paragraphs and lighter citation pressure
- talk script privileges cadence and rhetorical recurrence differently than article prose

## Tool Surface

The generalized MCP should expose a clearer writing-oriented tool layer.

### Core document tools

- `register_document`
- `resolve_document`
- `list_documents`
- `section_map`
- `detect_repo_root`
- `document_status`

### Audit tools

- `run_writing_audit`
- `run_domain_audit`
- `run_section_audit`
- `list_active_rules`
- `explain_rule`
- `readiness_check`
- `audit_status`
- `reset_audit`
- `waive_rule`

### Composition tools

- `diagnose_paragraph`
- `suggest_split`
- `suggest_merge`
- `trace_argument_flow`
- `find_transition_failures`
- `find_unearned_claims`
- `prepare_revision_brief`
- `compare_versions`

### Diff and revision tools

- `track_changes`
- `section_diff`
- `render_docx`
- `render_marked_copy`

### Dissertation plugin tools

- `verify_citations`
- `citation_chain_audit`
- `search_bibliography`
- `chapter_status`
- `render_gate`
- `query_corpus`
- `search_posts`
- `lookup_evidence`

## Report Format

The server should produce structured reports that make collaborative editing legible.

Each report should include:

- target file
- section boundaries
- profile name
- active domains
- findings grouped by domain
- severity counts
- clean or blocked status
- fixable versus judgment-call findings
- waiver list
- audit history summary

Example audit footer:

- `DX 3 found / 3 fixed`
- `SX 5 found / 4 fixed / 1 deferred`
- `AX 2 flagged / review required`
- `PX clean`

This report shape lets two agents divide work by domain or section without losing track of what has already been checked.

## Audit State Model

Audit history needs finer granularity than a chapter-wide pass log.

The new state model should track:

- document
- repo root
- section range
- profile
- domain
- pass timestamp
- agent/author
- violations found
- violations fixed
- unresolved issues
- waivers applied
- clean or blocked result
- rendered outputs produced

This model allows records like:

- document: `draft.md`
- section: `Cloze Reader :: critical artifact stretch`
- profile: `cloze-paper`
- diction: clean
- syntax: clean
- argumentation: one open question
- paragraph organization: revised and rechecked

## Exception and Waiver System

A style engine that cannot accommodate exceptions becomes a blunt instrument.

Every rule should support explicit waivers.

Waiver data should include:

- rule id
- file/section
- reason
- authorizing agent or human
- expiration or permanent flag

Examples of legitimate waivers:

- genuine contrast doing real argumentative work
- parenthetical em dash pair used correctly
- deliberately isolated short paragraph for landing effect
- quoted material preserved for evidentiary reasons
- field term of art that superficially resembles banned diction

## Project Root and Git Generalization

The smoke test exposed the immediate technical blocker.

`track_changes` failed because the target file lived in `Quimbot`, while the MCP server assumed the `diss` project root. The generalized system must resolve repo context from the target file itself.

Required behavior:

1. accept an explicit `file`
2. detect the nearest git root for that file
3. compute HEAD from that repo
4. diff against that repo’s tracked state
5. fail only if the file itself is untracked or outside a git repo

This change alone makes tracked changes portable across writing repos.

## Registration Model

The current chapter model should remain for dissertation projects, but arbitrary-file mode must be first-class.

Support two modes:

### Registered mode

Used for dissertation chapters, formal projects, and known bundles.

Fields:

- name
- file path
- profile
- section schema
- render settings
- bibliography settings

### Ad hoc mode

Used for one-off files and drafts.

Fields:

- file path
- optional profile
- optional section bounds

All core writing tools should work in either mode.

## Migration Plan

### Phase 1 — Stabilize current server

Goals:

- keep `diss-mcp` working
- fix repo-root assumptions
- allow arbitrary file audits

Tasks:

- make `track_changes` repo-local to target file
- allow `audit_status` on arbitrary files
- allow profile selection on core audit calls
- document current dissertation-only assumptions explicitly

### Phase 2 — Extract the writing substrate

Goals:

- separate portable writing functions from dissertation plugin logic

Tasks:

- create core file-resolution module
- create core audit-state module
- create core report generator
- create shared rule registry
- move dissertation-specific tools into plugin namespace internally

### Phase 3 — Implement rule domains

Goals:

- replace monolithic style logic with domain-organized passes

Tasks:

- define domain schema
- migrate existing style rules into domain records
- implement domain runner
- implement cross-domain report aggregation
- build waiver support

### Phase 4 — Add profile system

Goals:

- let different writing types activate different constraints

Tasks:

- create profile schema
- add default profiles
- build profile inheritance
- map rules to profiles
- store profile in audit history

### Phase 5 — Add composition tooling

Goals:

- move beyond pass/fail auditing into editorial guidance

Tasks:

- paragraph diagnosis
- transition diagnostics
- split/merge suggestion tools
- argument-flow tracing
- revision brief generation

### Phase 6 — Rebrand only after the boundary is real

Do not rename too early.

Once the writing substrate and plugin separation actually exist, then rename or alias:

- `diss-mcp` → `composer-mcp`
- retain `diss` as a plugin/profile bundle

## Minimum Viable Next Sprint

If only a small implementation window is available, do these first:

1. repo-local `track_changes`
2. arbitrary-file `audit_status`
3. `profile` argument on audit calls
4. `run_writing_audit(file, profile, section_start?, section_end?)`
5. first five domain buckets:
   - diction
   - syntax
   - argumentation
   - coherence/cohesion
   - paragraph organization

This sprint would turn the current server from a dissertation-bound tool into a usable general writing gate.

## Deliverables

Recommended immediate deliverables:

1. architecture note
2. rule taxonomy spec
3. profile schema spec
4. migration checklist
5. first sprint task list

## Proposed First Deliverable Breakdown

### A. Architecture note

Contents:

- system layers
- plugin boundary
- repo-root model
- audit-state model
- tool-surface principles

### B. Rule taxonomy spec

Contents:

- domain definitions
- rule ID conventions
- severity scale
- waiver model
- example rules per domain

### C. Profile schema spec

Contents:

- profile fields
- inheritance model
- activation semantics
- example profiles

### D. Migration checklist

Contents:

- current tool inventory
- portability blockers
- dissertation-only assumptions
- compatibility requirements
- rollout sequence

### E. Sprint task list

Contents:

- concrete coding tasks
- order of operations
- test cases
- sample target files across repos

## Testing Strategy

The generalized system should be tested on at least four writing types:

1. dissertation chapter in `diss`
2. paper draft in `Quimbot`
3. microblog entry in `creative-clawing`
4. one ad hoc markdown memo in a temporary repo

Tests should verify:

- file resolution
- repo-root detection
- tracked changes
- audit-state persistence
- profile activation
- domain reporting
- waiver recording
- rendering behavior

## Closing Principle

The writing MCP should become stricter by becoming more explicit.

A single undifferentiated style-guide gate produces confusion because the system cannot say whether a failure belongs to diction, syntax, evidence, sequence, or paragraph structure. A good writing workflow server should expose those layers clearly, run them selectively, and preserve a human-readable audit trail of why a piece of prose passed, failed, or was waived.

That change would let Quimbot and Petrarch use one required writing path across projects without forcing every task into dissertation-shaped assumptions.