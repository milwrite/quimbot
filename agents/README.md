# Agent Coordination

This directory contains files for multi-agent collaboration and project management.

## Files

### Core Workflow
- **COLLABORATION.md** - Multi-agent coordination protocol
- **KANBAN.md** - Project board with daily stand-ups
- **STATUS.md** - Real-time status and current tasks
- **NEXT-ACTIONS.md** - Prioritized action items

### Logging
- **DEVLOG.md** - Timestamped work log (all significant actions)
- **RUNLOG.md** - Training run history and results

## Usage

### Daily Stand-ups
Agents update **KANBAN.md** twice daily (morning/evening) with:
- Recent deliverables
- Current blockers
- Next steps

### Status Updates
Keep **STATUS.md** current with:
- Active tasks
- Training status
- Immediate next steps

### Work Log
Log all significant work in **DEVLOG.md**:
- Timestamp (EST)
- Agent name
- Action taken
- Why (motivation)
- Result

### Example DEVLOG Entry
```markdown
- **2026-02-08 22:10 EST** — **[Petrarch]** Reorganized evaluation framework into evaluation/ subdirectory. **Why:** root folder too cluttered. **Result:** Success - moved all eval files, created evaluation/README.md. **Next:** Await instructions.
```

## See Also

- Project root: [../README.md](../README.md)
- Agent instructions: [../CLAUDE.md](../CLAUDE.md)
- Evaluation framework: [../evaluation/](../evaluation/)
- Fine-tuning workflows: [../fine-tuning/](../fine-tuning/)
