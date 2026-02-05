# Petrarch ↔ Quimbot Collaboration Protocol

**Version:** 1.0  
**Effective:** 2026-02-04  
**Authors:** Petrarch (proposal) | Quimbot (synthesis) | zachary (approval)

---

## Core Principle

**Work in parallel, sync constantly, handoff explicitly.**

---

## 1. Real-Time Status Updates

### STATUS.md
**Location:** `/quimbot/STATUS.md`  
**Update frequency:** After every significant action (not just standups)

**Required fields:**
```markdown
**Last Update:** [timestamp] by [agent]
**Current Task:** [what you're doing right now]
**Active Work:** [detailed status]
**Completed Today:** [bullet list]
**Blockers:** [none or specific issues]
**Next Handoff:** [what the other agent should do next]
**Waiting On:** [dependencies]
```

**Rule:** Commit + push STATUS.md after:
- Starting a new task
- Completing a task
- Encountering a blocker
- Every 30 minutes during active work

---

## 2. Driver/Navigator Roles

### Driver (Active Executor)
**Responsibilities:**
- Execute current task
- Post progress updates every 10-15 minutes
- Log outputs/errors immediately
- Save work frequently (git commit)
- Ask Navigator for help when stuck

**Status indicators:**
- 🚗 Active work
- 🔄 Waiting for output (long-running process)
- ✅ Task complete, ready to handoff

### Navigator (Active Monitor)
**Responsibilities:**
- Monitor Driver's progress
- Watch for errors/blockers
- Prepare next task in parallel
- Review Driver's commits
- Ready to take over if Driver blocks

**Status indicators:**
- 👀 Monitoring
- 🔧 Preparing next task
- 🚨 Driver needs help

### Role Rotation
**Frequency:** Hourly or at natural handoff points  
**Trigger:** Task completion, blocker encountered, or time-based

**Handoff format:**
```
@other-agent: Taking Navigator role. You're up as Driver for [task].
See STATUS.md for context. Previous work in commit [hash].
```

---

## 3. Communication Channels

### Discord #orchestra
**Use for:**
- Explicit handoffs (tag @other-agent)
- Blocker alerts
- Status updates (every 15-30 min during active work)
- Success confirmations

**Template:**
```
@other-agent [emoji status]
Task: [brief description]
Status: [progress/complete/blocked]
Next: [what needs to happen]
```

### Git Commits
**Use for:**
- Code/doc changes
- Progress checkpoints
- Handoff markers

**Commit convention:**
```
[Agent] Category: Brief description

- Detailed bullet points
- What changed
- Why it changed
- What's next

@other-agent: [handoff instructions if applicable]
```

### STATUS.md
**Use for:**
- Current state snapshot
- Async coordination
- Historical record

---

## 4. Update Cadence

### During Active Work (both agents online)
| Interval | Action |
|----------|--------|
| Every action | Update STATUS.md locally |
| Every 15 min | Push STATUS.md + post Discord update |
| Every 30 min | Full KANBAN.md sync |
| Every hour | Role rotation check |

### During Async Work (one agent offline)
| Interval | Action |
|----------|--------|
| Before starting | Pull latest, read STATUS.md + KANBAN.md |
| After completing | Push all changes, update STATUS.md, post Discord summary |
| When blocked | Update STATUS.md with blocker, ping other agent |

---

## 5. File Ownership

### Petrarch Primary
- `/research/` — Dataset research & documentation
- `/LICENSE-VERIFICATION.md` — License analysis
- `DEVLOG.md` — Development log entries (shared)
- `KANBAN.md` — Backlog/Done sections
- `STATUS.md` — When Driver

### Quimbot Primary
- `/fine-tuning/` — Training scripts & experiments
- `DEVLOG.md` — Development log entries (shared)
- `KANBAN.md` — In Progress/Blocked sections
- `STATUS.md` — When Driver

### Shared (Both Agents)
- `README.md` — Project overview
- `DEVLOG.md` — Append-only log (both contribute)
- `KANBAN.md` — Update relevant sections
- `STATUS.md` — Active agent updates

**Merge conflict protocol:**
1. Pull before editing shared files
2. If conflict: keep both entries, mark with [Agent] prefix
3. Don't force-push

---

## 6. Handoff Checklist

### Before Handoff (Current Driver)
- [ ] Commit all work
- [ ] Update STATUS.md with current state
- [ ] Update DEVLOG.md with completed actions
- [ ] Update KANBAN.md (move tasks to appropriate column)
- [ ] Push to git
- [ ] Post Discord handoff message with:
  - What was completed
  - What's next
  - Any blockers
  - Commit hash for reference

### After Receiving Handoff (New Driver)
- [ ] Pull latest from git
- [ ] Read STATUS.md
- [ ] Read last 5 DEVLOG.md entries
- [ ] Check KANBAN.md for task context
- [ ] Confirm handoff in Discord ("Got it, starting [task]")
- [ ] Update STATUS.md with new current task
- [ ] Begin work

---

## 7. Daily Sync Protocol

### Morning Standup (10:00 EST)
**Both agents:**
1. Read overnight DEVLOG.md entries
2. Review KANBAN.md
3. Read STATUS.md
4. Post in Discord:
   - What you did overnight/yesterday
   - What you're doing today
   - Any blockers

**Assign:**
- Driver role (first active task)
- Navigator role
- Handoff points for the day

### Evening Standup (20:00 EST)
**Both agents:**
1. Update DEVLOG.md with day's work
2. Update KANBAN.md (move completed tasks to Done)
3. Update STATUS.md (what's pending for tomorrow)
4. Post in Discord:
   - What got done
   - What's blocked
   - Plan for tomorrow

---

## 8. Blocker Protocol

### When Blocked
1. **Immediate:** Update STATUS.md with blocker details
2. **Within 5 min:** Post in Discord:
   ```
   @other-agent 🚨 Blocked
   Task: [what you were doing]
   Blocker: [specific issue]
   Tried: [what you attempted]
   Need: [what would unblock you]
   ```
3. **Switch:** If other agent can unblock, offer to switch roles
4. **Escalate:** If both blocked, tag @zachary with details

### When Helping Unblock
1. Acknowledge quickly ("On it")
2. Investigate (5-10 min max)
3. Either:
   - Fix and post solution
   - Suggest workaround
   - Recommend different approach
4. Update STATUS.md when resolved

---

## 9. Success Criteria

### Good Coordination
✅ STATUS.md updated within 15 min of any state change  
✅ Discord updates every 15-30 min during active work  
✅ Handoffs completed within 5 min (ack → start)  
✅ No duplicate work (both agents working on same task)  
✅ Blockers resolved within 30 min  
✅ Git history shows clear progression (no long gaps)  

### Poor Coordination
❌ STATUS.md out of date >30 min  
❌ Silent work (no Discord updates >1 hour)  
❌ Handoffs take >15 min to acknowledge  
❌ Duplicate effort discovered  
❌ Blockers unresolved >1 hour  
❌ Git conflicts from simultaneous edits  

---

## 10. Enforcement

### Self-Monitoring
**Every 30 minutes, ask:**
- Is STATUS.md current?
- Have I posted a Discord update in the last 30 min?
- Does the other agent know what I'm doing?
- Am I blocked? If so, have I asked for help?

### zachary Monitoring
**Periodic checks:**
- STATUS.md freshness
- Discord activity
- Git commit frequency
- KANBAN.md accuracy

**Intervention triggers:**
- >1 hour without updates from either agent
- >2 hours without progress on active task
- Obvious coordination failures

---

## 11. Example Workflow

**Scenario:** Training a LoRA model

**10:00 - Morning Standup**
- Petrarch (Navigator): "I'll monitor and prep dataset downloads"
- Quimbot (Driver): "Starting 100-step training run"

**10:05 - Quimbot updates**
```markdown
STATUS.md:
**Current Task:** Training Qwen3-8B LoRA (100 steps)
**Active Work:** Initializing Tinker client...
```

**10:20 - Progress update**
```
@Petrarch 🔄
Training: Step 15/100 complete
Loss: 2.34
Next checkpoint: Step 25
```

**10:35 - Checkpoint save**
```
@Petrarch ✅
Checkpoint 25/100 saved
Loss: 1.98 (improving)
Logs in training_log.json
```

**11:00 - Training complete**
```
@Petrarch 🎉
Training complete! 100 steps done.
Final loss: 1.12
Weights saved to: checkpoints/lora_Qwen_*/final_lora_weights
Commit: abc1234

You're up as Driver: Test LoRA with test_lora_model.py
I'll switch to Navigator and prep next dataset.
```

**11:05 - Petrarch handoff ack**
```
@Quimbot 👀
Got it, pulling latest.
Starting inference testing now.
You: Download WAXAL dataset while I test?
```

**11:06 - Role swap confirmed**
```
@Petrarch ✅
Confirmed. Downloading WAXAL (19 African languages).
Will monitor your test results.
```

---

## 12. Amendments

**Process:**
1. Either agent proposes change in Discord
2. Both agents discuss
3. zachary approves
4. Update COLLABORATION.md
5. Commit with changelog

**Changelog:**
- 2026-02-04: Initial version

---

## Quick Reference Card

### Every Action
→ Update STATUS.md locally

### Every 15 Min
→ Push STATUS.md  
→ Post Discord update

### Every 30 Min
→ Sync KANBAN.md

### Every Hour
→ Check role rotation

### Every Handoff
→ Commit + Push + Discord tag

### Every Blocker
→ STATUS.md + Discord ping within 5 min

---

**Remember:** We're a team. Over-communicate. Ask for help. Celebrate wins. 🤝
