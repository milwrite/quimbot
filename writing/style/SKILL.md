# Style Skill

**Location:** `writing/style/`  
**Trigger:** Any task involving writing, revising, critiquing, or producing prose artifacts

---

## What This Skill Does

Loads the appropriate style sub-files based on the task's scale and context.  
Enforces milwrite's prose protocol as an experimental writing standard across all artifact work.

---

## When to Load

| Trigger phrase | Action |
|---|---|
| "revise this," "edit this," "clean this up" | Load checklist.md + sentences.md |
| "write a draft," "write an intro," "write a section" | Load voice.md + structure.md + checklist.md |
| "fix the diction," "too many nominalizations," "verb audit" | Load diction.md + sentences.md |
| "does this structure work?" | Load structure.md + paragraphs.md |
| "full document revision" | Load all files |
| "DHQ / cloze paper / academic piece" | Load voice.md (project notes) + all files |
| "Reddit / surveillance / CUNY piece" | Load voice.md (project notes) + all files |

---

## Protocol

1. **Identify the task scale** (word/phrase, sentence, paragraph, full piece)
2. **Load the relevant sub-file(s)** from the router in MASTER.md
3. **Check checklist.md** before returning any revised prose
4. **When generating new prose:** load voice.md to calibrate register before writing; load examples.md to anchor to milwrite's actual patterns

---

## Files

- `MASTER.md` — router and governing principles
- `diction.md` — word-level rules
- `sentences.md` — sentence-level rules and banned constructions
- `paragraphs.md` — paragraph organization, evidence integration, citations
- `structure.md` — piece-level architecture, signature moves, project-specific arcs
- `voice.md` — tone, register, project contexts, humanizing rules
- `examples.md` — positive and negative examples from milwrite's work
- `checklist.md` — full revision checklist

---

## Maintenance

When a new rule is established during a revision session:
1. Add it to the relevant scale file with a date tag
2. If it's a new banned construction, add it to checklist.md
3. If it emerged from a specific project, note it in voice.md under Project Notes
4. **Do not edit STYLE_GUIDE.md** — that file is the old flat structure, preserved for history

---

## Source Reference

Based on:
- milwrite's existing `writing/STYLE_GUIDE.md` (rules accumulated 2026-02-01 through 2026-03-21)
- Every.to AI style guide (Katie Parrott / Claude, 2025) — structural framing and example organization
- milwrite's published work (Journalism Studies 2025; CUNY Academic Works)
