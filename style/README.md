# Style Guide — Master Router

*This directory is the shared writing system for Quimbot and Petrarch. Read the router first; then load only what you need.*

---

## Quick Routing

| Task | Read |
|---|---|
| Starting a new piece (any type) | `voice.md` → `structure.md` |
| Academic paper draft or revision | `academic.md` + `sentences.md` + `anti-patterns.md` |
| Microblog or gallery write-up | `voice.md` + `structure.md` (blog section) |
| Argument construction | `structure.md` + `paragraphs.md` |
| Word and vocabulary choices | `diction.md` |
| Sentence-level edit pass | `sentences.md` + `anti-patterns.md` |
| Full revision sweep | `checklist.md` (canonical checklist — Pre-Post Protocol + all categories) |
| Data embedding in prose | `paragraphs.md` (Data-in-Context section) |
| Making prose feel human | `paragraphs.md` (Humanizer section) |

---

## File Map

```
style/
  README.md          ← you are here
  checklist.md       ← canonical revision checklist (Pre-Post Protocol + all categories)
  voice.md           ← tone, register, what the writing should feel like
  structure.md       ← arc patterns, openings, endings, structural templates
  sentences.md       ← sentence-level rules (the dense ruleset)
  diction.md         ← vocabulary bans, verb choices, naming principles
  paragraphs.md      ← paragraph rhythm, data embedding, humanizer recs
  anti-patterns.md   ← consolidated banned constructions with solutions
  macros/            ← macro ID system for context-window injection
```

---

## Maintenance

Both Quimbot and Petrarch maintain this directory. When a new rule is established in practice, add it to the relevant file. The old flat file lives at `../writing/STYLE_GUIDE.md` for reference; this disaggregated version supersedes it.

When adding a rule, include:
- The specific pattern to ban or require
- At least one before/after example
- Date added (for tracking what's new vs. foundational)

---

## Macro System

For context-window injection, use `macros/`:

```
style/macros/
  TAXONOMY.md        ← full ID index (SX/VB/PX/CL/CT/DC/PR/AK/NL prefixes)
  INJECT.md          ← injection template + toggle commands
  scope/             ← per-task profiles (cloze-paper, sentence-revision, etc.)
  rules/             ← individual rule cards (e.g. CL-01.md, CT-02.md)
```

**To activate:** load `macros/INJECT.md` + the relevant scope file from `macros/scope/`.  
Toggle with: "style macros on/off" or "style macros: [profile]".

---

*Last updated: 2026-03-29. Quimbot.*
