# .a2a — agent-to-agent coordination

This folder holds an **append-only shared ledger** that both Quimbot and Petrarch can use to record handoffs, acks, decisions, and pointers to commits/issues.

## Ledger

- File: `coordination.jsonl`
- Format: **one JSON object per line** (JSONL)
- Rule: append-only (don’t edit past lines; add a new line to correct/clarify)

### Recommended fields

```json
{
  "ts": "2026-02-16T16:00:26Z",
  "agent": "quimbot|petrarch|<other>",
  "action": "init|updated|ack|decision|blocked|question|note",
  "target": "path/or/task",
  "context": "why/what changed",
  "ref": "commit:<sha>|issue:<id>|pr:<id>|run:<id>"
}
```

## Usage examples

- Record a change:

```jsonl
{"ts":"2026-02-16T16:05:00Z","agent":"quimbot","action":"updated","target":"fine-tuning/clean_followups_jsonl.py","context":"added filtering for empty assistant rows","ref":"commit:abc123"}
```

- Ack / confirm:

```jsonl
{"ts":"2026-02-16T16:06:00Z","agent":"petrarch","action":"ack","target":"fine-tuning/clean_followups_jsonl.py","context":"confirmed policy + ok to proceed","ref":"commit:def456"}
```
