#!/bin/bash
# Complete the 1000-dialogue target using optimized v2 generator

set -e

cd "$(dirname "$0")"

echo "🚀 Scaffolding Generation - Completion Run"
echo "=========================================="
echo ""

# Check current status
CURRENT=$(wc -l < scaffolding_combined.jsonl 2>/dev/null || echo 0)
TARGET=1000
NEEDED=$((TARGET - CURRENT))

echo "📊 Current: $CURRENT dialogues"
echo "🎯 Target:  $TARGET dialogues"
echo "📝 Needed:  $NEEDED dialogues"
echo ""

if [ $NEEDED -le 0 ]; then
    echo "✅ Target already met!"
    exit 0
fi

# Run optimized generator
echo "🔧 Running optimized generator with:"
echo "   - Resume mode (skip existing patterns)"
echo "   - Quality filtering enabled"
echo "   - Multi-model fallback (Gemini → Haiku → Kimi)"
echo "   - Reduced token usage (200 vs 300)"
echo ""

python3 generate_scaffolding_v2.py \
    --output scaffolding_v2_completion.jsonl \
    --count $NEEDED \
    --resume \
    --filter-quality \
    --debug

echo ""
echo "✅ Generation complete!"
echo ""

# Merge with existing
echo "🔀 Merging with existing dialogues..."
cat scaffolding_combined.jsonl scaffolding_v2_completion.jsonl > scaffolding_1000_final.jsonl

FINAL=$(wc -l < scaffolding_1000_final.jsonl)
echo "📦 Final count: $FINAL dialogues"
echo "💾 Saved to: scaffolding_1000_final.jsonl"
echo ""

# Quality report
echo "📊 Quality breakdown:"
jq -r '.quality_check.reason' scaffolding_v2_completion.jsonl 2>/dev/null | sort | uniq -c || echo "  (quality data not available for old format)"

echo ""
echo "🎉 Done!"
