#!/usr/bin/env python3
"""
Analyze scaffolding dialogue quality and coverage.
"""

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

def analyze_file(filepath):
    """Analyze a scaffolding JSONL file."""
    
    path = Path(filepath)
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        return
    
    dialogues = []
    with path.open() as f:
        for line in f:
            try:
                dialogues.append(json.loads(line))
            except:
                continue
    
    if not dialogues:
        print(f"❌ No valid dialogues in {filepath}")
        return
    
    print(f"\n{'='*70}")
    print(f"📊 SCAFFOLDING ANALYSIS: {path.name}")
    print(f"{'='*70}\n")
    
    # Basic stats
    print(f"📈 Total dialogues: {len(dialogues)}")
    print(f"📁 File size: {path.stat().st_size / 1024:.1f} KB\n")
    
    # L1 distribution
    l1_counts = Counter(d.get("l1_background") for d in dialogues)
    print("🌍 L1 Background Distribution:")
    for l1, count in sorted(l1_counts.items(), key=lambda x: -x[1]):
        pct = count / len(dialogues) * 100
        bar = "█" * int(pct / 2)
        print(f"  {l1:12s} {count:4d} ({pct:5.1f}%) {bar}")
    print()
    
    # Proficiency levels
    level_counts = Counter(d.get("proficiency") for d in dialogues)
    print("📚 Proficiency Distribution:")
    for level, count in sorted(level_counts.items()):
        pct = count / len(dialogues) * 100
        print(f"  {level:12s} {count:4d} ({pct:5.1f}%)")
    print()
    
    # Error types
    error_counts = Counter(d.get("error_type") for d in dialogues)
    print("🎯 Error Type Distribution:")
    for etype, count in sorted(error_counts.items(), key=lambda x: -x[1])[:10]:
        pct = count / len(dialogues) * 100
        print(f"  {etype:25s} {count:4d} ({pct:5.1f}%)")
    if len(error_counts) > 10:
        print(f"  ... and {len(error_counts) - 10} more")
    print()
    
    # Message quality checks
    turn_counts = []
    teacher_questions = 0
    avg_teacher_len = []
    avg_student_len = []
    
    for d in dialogues:
        messages = d.get("messages", [])
        turn_counts.append(len(messages))
        
        for msg in messages:
            content = msg.get("content", "")
            if msg.get("role") == "assistant":
                avg_teacher_len.append(len(content))
                if "?" in content:
                    teacher_questions += 1
            elif msg.get("role") == "user":
                avg_student_len.append(len(content))
    
    print("💬 Dialogue Quality Metrics:")
    print(f"  Avg turns per dialogue:     {sum(turn_counts) / len(turn_counts):.1f}")
    print(f"  Avg teacher msg length:     {sum(avg_teacher_len) / len(avg_teacher_len):.0f} chars")
    print(f"  Avg student msg length:     {sum(avg_student_len) / len(avg_student_len):.0f} chars")
    print(f"  Teacher questions:          {teacher_questions} ({teacher_questions/len(dialogues):.1f} per dialogue)")
    print()
    
    # Coverage gaps
    print("🔍 Coverage Analysis:")
    l1_error_combos = set()
    for d in dialogues:
        l1 = d.get("l1_background")
        error = d.get("error_type")
        l1_error_combos.add((l1, error))
    
    total_l1s = len(l1_counts)
    total_errors = len(error_counts)
    max_combos = total_l1s * total_errors
    coverage_pct = len(l1_error_combos) / max_combos * 100 if max_combos > 0 else 0
    
    print(f"  Unique L1s:                 {total_l1s}")
    print(f"  Unique error types:         {total_errors}")
    print(f"  L1×Error combinations:      {len(l1_error_combos)} / {max_combos} ({coverage_pct:.1f}%)")
    print()
    
    # Recommendations
    print("💡 Recommendations:")
    
    # Check for imbalances
    min_l1 = min(l1_counts.values())
    max_l1 = max(l1_counts.values())
    if max_l1 / min_l1 > 1.5:
        print("  ⚠️  L1 distribution imbalanced (generate more for underrepresented)")
    else:
        print("  ✅ L1 distribution balanced")
    
    # Check turn depth
    avg_turns = sum(turn_counts) / len(turn_counts)
    if avg_turns < 4:
        print(f"  ⚠️  Low turn depth ({avg_turns:.1f}) - aim for 4-6 turns")
    else:
        print(f"  ✅ Good turn depth ({avg_turns:.1f})")
    
    # Check scaffolding questions
    questions_per = teacher_questions / len(dialogues)
    if questions_per < 1.5:
        print(f"  ⚠️  Low scaffolding questions ({questions_per:.1f}/dialogue) - aim for 2+")
    else:
        print(f"  ✅ Good scaffolding questions ({questions_per:.1f}/dialogue)")
    
    # Coverage
    if coverage_pct < 50:
        print(f"  ⚠️  Low coverage ({coverage_pct:.1f}%) - add more error type variety")
    else:
        print(f"  ✅ Good coverage ({coverage_pct:.1f}%)")
    
    print(f"\n{'='*70}\n")


def main():
    files = sys.argv[1:] if len(sys.argv) > 1 else [
        "scaffolding_combined.jsonl",
        "scaffolding_adaptive_500.jsonl",
        "scaffolding_1000.jsonl"
    ]
    
    for filepath in files:
        if Path(filepath).exists():
            analyze_file(filepath)


if __name__ == "__main__":
    main()
