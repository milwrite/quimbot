# Claude / Agent Notes

## Core Protocol

- Follow **agents/COLLABORATION.md** protocol for multi-agent coordination
- Update **agents/KANBAN.md**, **agents/STATUS.md**, **agents/DEVLOG.md**, **agents/RUNLOG.md** after each significant action
- Always include commit hash **and** direct GitHub file link in Discord updates
- Never commit datasets or large artifacts to Git

## Agent Documentation

All agent coordination files are in the `agents/` subdirectory:

- **agents/COLLABORATION.md** - Multi-agent workflow protocol
- **agents/KANBAN.md** - Project board and stand-up notes
- **agents/STATUS.md** - Real-time status updates
- **agents/DEVLOG.md** - Timestamped work log
- **agents/RUNLOG.md** - Training run history
- **agents/NEXT-ACTIONS.md** - Prioritized action items

## Project Structure

```
quimbot/
├── README.md              # Project overview
├── CLAUDE.md              # This file (agent instructions)
├── agents/                # Agent coordination docs
├── evaluation/            # Model evaluation framework
├── fine-tuning/           # Training scripts and workflows
├── datasets/              # Training data (not committed)
├── checkpoints/           # Model checkpoints (not committed)
└── research/              # Research notes and plans
```
