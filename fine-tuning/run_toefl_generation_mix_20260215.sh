#!/usr/bin/env bash
set -euo pipefail

# Generates a turn-count mix of TOEFL synth followups using OpenRouter.
# Targets (per milwrite 2026-02-15):
#  - 4-message dialogues: 3x the 3-message dialogues
#  - 3-message dialogues: 4000
#  - Remaining balanced across 2, 5, 6 messages
#
# This script runs sequentially (safer for rate limits).

TS=${TS:-$(date +%Y%m%d_%H%M%S)}
OUTDIR=${OUTDIR:-fine-tuning/data}
BATCH=${BATCH:-80}
SLEEP=${SLEEP:-0.6}
MODEL=${MODEL:-${OPENROUTER_MODEL:-google/gemini-3-flash-preview}}

N3=${N3:-4000}
N4=${N4:-12000}     # 3x N3
N2=${N2:-2000}
N5=${N5:-2000}
N6=${N6:-2000}

mkdir -p "$OUTDIR"

run_one () {
  local turns=$1
  local n=$2
  local out="$OUTDIR/toefl_synth_followups_${n}_${turns}msg_openrouter_${TS}.jsonl"
  echo "[run] turns=$turns n=$n out=$out model=$MODEL"
  python3 fine-tuning/generate_toefl_followups_openrouter.py \
    --out "$out" --n "$n" --batch "$BATCH" --turns "$turns" --sleep "$SLEEP" --model "$MODEL"
}

run_one 4 "$N4"
run_one 3 "$N3"
run_one 2 "$N2"
run_one 5 "$N5"
run_one 6 "$N6"

echo "Done. Outputs in $OUTDIR with timestamp $TS"