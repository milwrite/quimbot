# SG.md — Style Governance

**Version:** 2026-04-06  
**Maintainers:** Quimbot + Petrarch  
**Status:** Draft — pending milwrite approval

---

## Authority Chain

One source of truth. One load path. No exceptions.

**Canonical location:** `Quimbot/style/` (macro system)  
**Entry point:** `Quimbot/style/macros/INJECT.md`  
**Scope profiles:** `Quimbot/style/macros/scope/`  
**Individual rule cards:** `Quimbot/style/macros/rules/`  
**Router:** `Quimbot/style/README.md`

**Deprecated (do not edit, do not consult for new work):**
- `Quimbot/writing/STYLE_GUIDE.md` — old flat file, frozen 2026-03-21
- `Quimbot/writing/style/MASTER.md` — superseded by macro system; convert to pointer only
- `SOUL.md` writing rules — inline rules removed, replaced by pointer to SG.md
- `HEARTBEAT.md` copyedit protocol section — absorbed into `macros/scope/sentence-revision.md`

**Cross-machine:** Petrarch accesses the same files via `~/clawd/quimbot/style/` (same repo, different mount path). Both agents read from the same git-tracked source.

---

## Load Protocol

### Tier 1 — Always On (every session, every task)
Load at session start. No trigger required.

```
READ: Quimbot/style/macros/INJECT.md
```

Non-negotiables from INJECT.md fire on every output:
- SX-01: no interrupted subject
- SX-04: no nominalized subject
- PX-01: no unearned em dash
- CL-01: earned assertion gate
- CT-01: submarine rule
- DC-01: no AI slop
- DC-07: no contrastive pivots
- VB-01: verb audit
- PR-04: no trailing -ing tag-ons

### Tier 2 — Task-Scoped (load at task start, state in preamble)
Select the matching scope profile and load it before any writing output.

| Task | Profile file | Rule count |
|---|---|---|
| Cloze Reader paper | `macros/scope/cloze-paper.md` | 47 |
| Microblog / gallery write-up | `macros/scope/microblog.md` | TBD |
| Sentence revision pass | `macros/scope/sentence-revision.md` | TBD |
| Paragraph reorg | `macros/scope/paragraph-reorg.md` | TBD |
| Reddit / surveillance piece | `macros/scope/reddit-piece.md` | TBD |
| Phrase-level edit | `macros/scope/phrase-edit.md` | TBD |

### Tier 3 — Audit Mode (on explicit request)
When milwrite says "run audit", "check this", or "which macros fired?":
- List each sentence
- List macro IDs that apply
- State pass or violation
- Propose correction for each violation

---

## Preamble Format

Every writing response starts with:
```
[STYLE MACROS ACTIVE: <profile> — <count> rules loaded]
```

Example:
```
[STYLE MACROS ACTIVE: cloze-paper — 47 rules loaded]
```

No preamble = non-compliant output. Both agents enforce this.

---

## Fallback Methods (OpenClaw Config Layer)

When the macro system fails to load (session restart, context loss, bootstrap truncation), these fallbacks fire in order:

**Fallback 1 — Bootstrap injection**  
`SG.md` is listed in the workspace bootstrap chain. OpenClaw injects it into every session start automatically alongside AGENTS.md and SOUL.md. The non-negotiables from Tier 1 are always present because they live in the bootstrapped SG.md itself (see below).

**Fallback 2 — SOUL.md pointer**  
SOUL.md Writing Rules section is replaced with:
> "Load `Quimbot/style/macros/INJECT.md` + the relevant scope profile before any writing output. Non-negotiables: SX-01, SX-04, PX-01, CL-01, CT-01, DC-01, DC-07, VB-01, PR-04. See `Quimbot/SG.md` for full protocol."

SOUL.md no longer duplicates rules inline. It points here.

**Fallback 3 — Embedded non-negotiables (this file)**  
Even if macro files cannot be read, the nine non-negotiables below are embedded directly in SG.md (which is bootstrapped). They fire regardless.

### Embedded Non-Negotiables

These nine rules fire on every output, no file load required:

1. **SX-01 Interrupted subject** — banned: `Subject, [interruptive phrase], verb`. Move qualifier after verb or subordinate.
2. **SX-04 Nominalized subject** — banned: verb or adjective turned into noun phrase as subject. "The optimization of X" → "X optimizes."
3. **PX-01 Unearned em dash** — a lone em dash as pivot, connector, or sentence-closer is banned. Paired em dash for a genuine parenthetical aside only.
4. **CL-01 Earned assertion gate** — no non-trivial claim without traceable evidence in the same sentence or the preceding one.
5. **CT-01 Submarine rule** — do not pit studies that answer different questions as if they contradict. A submarine doesn't outperform Michael Phelps at swimming.
6. **DC-01 AI slop** — banned: delve, tapestry, vibrant, crucial, comprehensive, meticulous, embark, robust, seamless, groundbreaking, synergy, transformative, paramount, multifaceted, myriad, cornerstone, reimagine, empower, catalyst, invaluable, bustling, nestled, realm.
7. **DC-07 Contrastive pivots** — banned: "not X but Y", "not just X", "not only X but also Y", "less about X more about Y". State the point directly.
8. **VB-01 Verb audit** — for every sentence: is the verb the most precise and rhetorically effective option? Weak copulas ("is shaped by", "are X-mediated") usually have a stronger replacement.
9. **PR-04 Trailing -ing** — no participial phrase tacked onto the end of a sentence as a trailing add-on. Restructure or make it a separate sentence.

---

## Cross-Agent Alignment Protocol

**On cloze paper work specifically:**
- CT-03 is active: Quimbot cannot solo-approve its own style calls on the cloze paper. Flag for milwrite or Petrarch review.
- AK-05 is active: flag any suspected invented academic noun phrase before using it.
- NL-01 governs register: DHQ, peer-reviewed sources, structural continuity + functional asymmetry claim.

**Handoff rule:** when one agent passes a draft to the other, the receiving agent states which scope profile it loaded before making any edits.

**Rule update rule:** any new rule established during a revision session gets written to `Quimbot/style/` within the same session. No rule lives only in chat. No mental notes.

---

## File Maintenance

When a new rule is established:
1. Add it to the relevant scale file in `Quimbot/style/` with a date tag
2. If it's a banned construction, add it to `style/anti-patterns.md`
3. If it applies to cloze paper, add the macro ID to `macros/scope/cloze-paper.md`
4. Update `macros/TAXONOMY.md` if it's a new macro ID
5. Write the rule card to `macros/rules/<ID>.md`

Missing rule cards (stub status): SX-02, SX-03, SX-05, VB-02, PX-02, PX-03, PX-04, CL-02 through CL-05, PR-01 through PR-06, AK-01 through AK-05, NL-01, NL-04. Priority: write cloze-paper non-negotiables first.

---

## Ratification

This document is a draft until milwrite approves it. After approval:
- Quimbot updates SOUL.md writing rules section to point here (removing inline rules)
- Quimbot updates HEARTBEAT.md to remove the inline copyedit protocol (absorbed here)
- Petrarch updates equivalent config files on their machine
- Both agents confirm in this thread that their session load behavior matches this document

*Draft authored: Quimbot, 2026-04-06. Petrarch to review and co-sign.*
