# OpenClaw Config and Memory RAG Health Runbook

## Purpose

Use this runbook when OpenClaw is running but memory RAG embeddings are down, or when session UI metadata shows a mismatched provider/model pair.

This was validated on 2026-03-01 in the Studio environment.

## Typical Symptoms

- `openclaw memory status --deep` shows:
  - `Provider: none (requested: auto)`
  - `Embeddings: unavailable`
  - `No API key found for provider "openai"`
- TUI/session line shows invalid pair like `anthropic/gpt-5.3-codex`
- `openclaw health --json` fails with gateway close `1006`

## Preconditions

- OpenClaw CLI is installed and on PATH (`openclaw --version`)
- You have access to the OpenClaw config at `~/.openclaw/openclaw.json`
- You have a valid OpenAI API key available (or another supported embedding provider key)

## 1) Baseline Health Snapshot

Run these first:

```bash
openclaw doctor --non-interactive
openclaw gateway status
openclaw health --json
openclaw memory status --deep
```

Expected healthy baseline:

- `gateway status` shows `RPC probe: ok`
- `health --json` has `"ok": true`
- `memory status --deep` shows:
  - `Provider: openai`
  - `Embeddings: ready`
  - `Vector: ready`

## 2) Fix Embeddings Unavailable (No API Key)

### 2.1 Confirm key presence in active config (without printing secret)

```bash
jq '{
  hasOpenAIKey:(.env.vars.OPENAI_API_KEY|type=="string" and (.|length>0)),
  modelPrimary:.agents.defaults.model.primary
}' ~/.openclaw/openclaw.json
```

If `hasOpenAIKey` is `false`, set it.

### 2.2 Set OPENAI_API_KEY in OpenClaw config

If key exists in `~/.clawdbot/clawdbot.json`, copy it:

```bash
KEY=$(jq -r '.env.vars.OPENAI_API_KEY // empty' ~/.clawdbot/clawdbot.json)
if [ -z "$KEY" ]; then
  echo "OPENAI_API_KEY missing in ~/.clawdbot/clawdbot.json" >&2
  exit 1
fi
openclaw config set --strict-json env.vars.OPENAI_API_KEY "\"$KEY\""
```

Or set directly from shell env:

```bash
openclaw config set --strict-json env.vars.OPENAI_API_KEY "\"$OPENAI_API_KEY\""
```

### 2.3 Restart gateway so env var takes effect

```bash
openclaw gateway restart
openclaw gateway status
```

If restart gets interrupted:

```bash
openclaw gateway start
openclaw gateway status
```

### 2.4 Re-check memory and run semantic probe

```bash
openclaw memory status --deep
openclaw memory search --query "nightly comm test" --json
```

Healthy output should include:

- `Provider: openai (requested: auto)`
- `Model: text-embedding-3-small`
- `Embeddings: ready`
- A result from `memory/...` in `memory search`

## 3) Fix Wrong Provider/Model Pair in Session UI

This is usually stale/missing transcript metadata in session store.

### 3.1 Preview cleanup impact

```bash
openclaw sessions cleanup \
  --dry-run \
  --fix-missing \
  --json \
  --store ~/.openclaw/agents/main/sessions/sessions.json
```

### 3.2 Apply cleanup

```bash
openclaw sessions cleanup \
  --enforce \
  --fix-missing \
  --json \
  --store ~/.openclaw/agents/main/sessions/sessions.json
```

### 3.3 Verify main session metadata is consistent

```bash
openclaw sessions --json | jq '
  .sessions[] |
  select(.key=="agent:main:main") |
  {key,model,modelProvider,totalTokens,contextTokens}
'
```

Expected:

- `model: gpt-5.3-codex`
- `modelProvider: openai-codex`

## 4) End-State Validation Checklist

Run:

```bash
openclaw gateway status
openclaw health --json
openclaw memory status --deep
openclaw memory search --query "agent-to-agent communication test" --json
openclaw doctor --non-interactive
```

Declare success when all are true:

- Gateway runtime is running and `RPC probe: ok`
- Health JSON has `"ok": true`
- Memory status shows `Embeddings: ready`
- Semantic memory query returns relevant file hits
- No blocking doctor errors for memory/gateway

## 5) Known Pitfalls

- `openclaw config set ... OPENAI_API_KEY` updates config, but embeddings still fail until gateway restart completes.
- Multiple gateway instances on the same port can cause restart loops and false negative probes.
- If CLI can not write `~/.openclaw` (lockfile or EPERM), run commands in a shell with proper permissions.
- Do not trust TUI model/provider labels if session store has missing transcripts. Run cleanup first.

## 6) Security Notes

- Never commit raw API keys to git.
- Never paste keys in Discord or shared channels.
- Validate key presence with boolean checks, not by printing values.
