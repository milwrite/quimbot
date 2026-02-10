#!/usr/bin/env python3
"""
Optimized scaffolding dialogue generation with:
- Resume capability (skip existing)
- Multi-model support (fallback chain)
- Better error handling + retry logic
- Reduced token usage
- Cost tracking
- Quality filtering
"""

import argparse
import json
import os
import random
import time
from pathlib import Path
from openai import OpenAI
from typing import Optional

# Expanded error patterns (original 5 → 12 per L1)
ERROR_PATTERNS = {
    "Spanish": [
        {"error": "She is teacher", "correct": "She is a teacher", "type": "article_omission"},
        {"error": "I have three book", "correct": "I have three books", "type": "plural_omission"},
        {"error": "Yesterday I go to store", "correct": "Yesterday I went to the store", "type": "past_tense"},
        {"error": "He want to eat", "correct": "He wants to eat", "type": "verb_agreement"},
        {"error": "I am agree with you", "correct": "I agree with you", "type": "be_verb_overuse"},
        {"error": "I no like this", "correct": "I don't like this", "type": "negation_error"},
        {"error": "Is very hot today", "correct": "It's very hot today", "type": "subject_omission"},
        {"error": "I am have a car", "correct": "I have a car", "type": "be_verb_overuse"},
        {"error": "She cooks very good", "correct": "She cooks very well", "type": "adverb_form"},
        {"error": "I go to the home", "correct": "I go home", "type": "article_overuse"},
        {"error": "More big than", "correct": "Bigger than", "type": "comparative_error"},
        {"error": "I studied for five years English", "correct": "I studied English for five years", "type": "word_order"},
    ],
    "Chinese": [
        {"error": "I have three book", "correct": "I have three books", "type": "plural_omission"},
        {"error": "Yesterday I go to school", "correct": "Yesterday I went to school", "type": "past_tense"},
        {"error": "She is very beautiful girl", "correct": "She is a very beautiful girl", "type": "article_omission"},
        {"error": "I very like this", "correct": "I really like this", "type": "adverb_placement"},
        {"error": "He go to work everyday", "correct": "He goes to work everyday", "type": "verb_agreement"},
        {"error": "I am boring", "correct": "I am bored", "type": "participle_confusion"},
        {"error": "She has a long hair", "correct": "She has long hair", "type": "article_overuse"},
        {"error": "I will go there in next week", "correct": "I will go there next week", "type": "preposition_error"},
        {"error": "Make me feel happy", "correct": "It makes me feel happy", "type": "subject_omission"},
        {"error": "My hometown has many traffic", "correct": "My hometown has a lot of traffic", "type": "uncountable_quantifier"},
        {"error": "More better", "correct": "Better", "type": "double_comparative"},
        {"error": "Although...but...", "correct": "Although...", "type": "conjunction_overuse"},
    ],
    "Arabic": [
        {"error": "She is good teacher", "correct": "She is a good teacher", "type": "article_omission"},
        {"error": "I have many informations", "correct": "I have a lot of information", "type": "uncountable_plural"},
        {"error": "He is very tall man", "correct": "He is a very tall man", "type": "article_omission"},
        {"error": "I go to school yesterday", "correct": "I went to school yesterday", "type": "past_tense"},
        {"error": "They was happy", "correct": "They were happy", "type": "verb_agreement"},
        {"error": "I am agree", "correct": "I agree", "type": "be_verb_overuse"},
        {"error": "The life", "correct": "Life", "type": "article_overuse"},
        {"error": "I study from long time", "correct": "I studied for a long time", "type": "preposition_tense"},
        {"error": "Big building", "correct": "A big building", "type": "article_omission"},
        {"error": "More good", "correct": "Better", "type": "comparative_error"},
        {"error": "I have 20 years", "correct": "I am 20 years old", "type": "verb_choice"},
        {"error": "My friend he is tall", "correct": "My friend is tall", "type": "pronoun_copy"},
    ],
    "Korean": [
        {"error": "I go to school yesterday", "correct": "I went to school yesterday", "type": "past_tense"},
        {"error": "She is pretty girl", "correct": "She is a pretty girl", "type": "article_omission"},
        {"error": "I have two cats and one dog", "correct": "I have two cats and a dog", "type": "article_omission"},
        {"error": "Yesterday I am happy", "correct": "Yesterday I was happy", "type": "past_tense"},
        {"error": "He don't like coffee", "correct": "He doesn't like coffee", "type": "verb_agreement"},
        {"error": "I very like pizza", "correct": "I really like pizza", "type": "adverb_placement"},
        {"error": "Teacher said me", "correct": "Teacher told me", "type": "verb_choice"},
        {"error": "I am boring now", "correct": "I am bored now", "type": "participle_confusion"},
        {"error": "More cheaper", "correct": "Cheaper", "type": "double_comparative"},
        {"error": "I can swimming", "correct": "I can swim", "type": "gerund_error"},
        {"error": "He is very tall person", "correct": "He is a very tall person", "type": "article_omission"},
        {"error": "I will go there next week in Monday", "correct": "I will go there on Monday next week", "type": "preposition_error"},
    ],
}

# Compact template (reduced from ~180 to ~120 tokens)
TEMPLATE = """Student (native {l1}, {level}): "{error}"
Teacher uses scaffolding—recast or question, NO explicit correction.
Model: "{correct}"

Format:
S: [error utterance]
T: [scaffolding response]
S: [reply]
T: [encouragement]"""

# Model fallback chain (cheapest first, with cost per 1M tokens)
MODELS = [
    {"name": "google/gemini-2.0-flash-001", "cost": 0.10},  # $0.10/1M
    {"name": "anthropic/claude-3.5-haiku", "cost": 1.00},   # $1/1M
    {"name": "moonshotai/kimi-k2.5", "cost": 0.50},         # $0.50/1M (estimate)
]


def load_existing(path: Path) -> set:
    """Load existing dialogues and return set of (l1, error, correct) tuples."""
    if not path.exists():
        return set()
    
    existing = set()
    with path.open() as f:
        for line in f:
            try:
                data = json.loads(line)
                key = (data.get("l1_background"), data.get("error_pattern"), data.get("correct_form"))
                existing.add(key)
            except:
                continue
    return existing


def count_tokens_estimate(text: str) -> int:
    """Rough token count (chars / 4)."""
    return len(text) // 4


def quality_check(dialogue: dict) -> tuple[bool, str]:
    """Basic quality filter. Returns (pass, reason)."""
    messages = dialogue.get("messages", [])
    
    if len(messages) < 3:
        return False, "too_short"
    
    # Check for explicit correction phrases (should use scaffolding instead)
    forbidden = ["wrong", "incorrect", "mistake", "error", "should be", "correct form"]
    text_lower = " ".join(m.get("content", "").lower() for m in messages)
    
    if any(word in text_lower for word in forbidden):
        return False, "explicit_correction"
    
    # Check for question-based scaffolding in teacher responses
    teacher_msgs = [m.get("content", "") for m in messages if m.get("role") == "assistant"]
    has_question = any("?" in msg for msg in teacher_msgs)
    
    if not has_question:
        return False, "no_scaffolding_question"
    
    return True, "ok"


def generate_with_retry(pattern, l1, level, client, models, max_retries=3, debug=False):
    """Try models in sequence with exponential backoff."""
    
    prompt = TEMPLATE.format(l1=l1, level=level, error=pattern['error'], correct=pattern['correct'])
    
    for model_info in models:
        model = model_info["name"]
        
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=200,  # Reduced from 300
                    temperature=0.7
                )
                
                generated = response.choices[0].message.content
                tokens_used = response.usage.total_tokens if hasattr(response, 'usage') else count_tokens_estimate(prompt + generated)
                
                # Parse
                messages = []
                for line in generated.strip().split('\n'):
                    line = line.strip()
                    if line.startswith('S:'):
                        messages.append({"role": "user", "content": line[2:].strip()})
                    elif line.startswith('T:'):
                        messages.append({"role": "assistant", "content": line[2:].strip()})
                    elif line.startswith('Student:'):
                        messages.append({"role": "user", "content": line.replace('Student:', '').strip()})
                    elif line.startswith('Teacher:'):
                        messages.append({"role": "assistant", "content": line.replace('Teacher:', '').strip()})
                
                if not messages:
                    messages = [{"role": "assistant", "content": generated}]
                
                dialogue = {
                    "l1_background": l1,
                    "proficiency": level,
                    "error_type": pattern['type'],
                    "error_pattern": pattern['error'],
                    "correct_form": pattern['correct'],
                    "messages": messages,
                    "model_used": model,
                    "tokens_used": tokens_used,
                    "cost_estimate_usd": (tokens_used / 1_000_000) * model_info["cost"]
                }
                
                # Quality check
                passed, reason = quality_check(dialogue)
                dialogue["quality_check"] = {"passed": passed, "reason": reason}
                
                if debug:
                    print(f"\n{'='*60}")
                    print(f"Model: {model} | Tokens: {tokens_used} | Quality: {reason}")
                    print(f"RAW:\n{generated}")
                    print(f"{'='*60}\n")
                
                return dialogue
                
            except Exception as e:
                wait = 2 ** attempt
                print(f"  ⚠️  {model} attempt {attempt+1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"     Retrying in {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"     Trying next model...")
                continue
    
    raise Exception(f"All models failed for {l1}/{pattern['type']}")


def main():
    parser = argparse.ArgumentParser(description="Generate scaffolding dialogues (optimized)")
    parser.add_argument("--output", default="scaffolding_v2.jsonl")
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--resume", action="store_true", help="Skip existing dialogues")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--filter-quality", action="store_true", help="Only save high-quality dialogues")
    args = parser.parse_args()
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("❌ OPENROUTER_API_KEY not set")
    
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    output_path = Path(args.output)
    
    # Load existing
    existing = load_existing(output_path) if args.resume else set()
    print(f"📂 Found {len(existing)} existing dialogues (will skip)")
    
    # Generate plan
    all_patterns = []
    for l1, patterns in ERROR_PATTERNS.items():
        for pattern in patterns:
            for level in ["beginner", "intermediate"]:
                all_patterns.append((l1, pattern, level))
    
    random.shuffle(all_patterns)
    
    print(f"\n🎯 Target: {args.count} dialogues")
    print(f"📋 Pool: {len(all_patterns)} unique (L1 × error × level)")
    print(f"💰 Models: {' → '.join(m['name'] for m in MODELS)}\n")
    
    generated = 0
    skipped = 0
    filtered = 0
    total_cost = 0.0
    
    mode = "a" if args.resume else "w"
    with output_path.open(mode) as f:
        for i in range(args.count):
            # Pick pattern
            l1, pattern, level = random.choice(all_patterns)
            key = (l1, pattern['error'], pattern['correct'])
            
            # Skip if exists
            if key in existing:
                skipped += 1
                continue
            
            try:
                dialogue = generate_with_retry(pattern, l1, level, client, MODELS, debug=args.debug)
                
                # Filter check
                if args.filter_quality and not dialogue["quality_check"]["passed"]:
                    filtered += 1
                    print(f"[{generated+skipped+filtered}/{args.count}] 🚫 Filtered: {dialogue['quality_check']['reason']}")
                    continue
                
                f.write(json.dumps(dialogue) + "\n")
                f.flush()
                
                total_cost += dialogue.get("cost_estimate_usd", 0)
                generated += 1
                existing.add(key)
                
                quality_icon = "✅" if dialogue["quality_check"]["passed"] else "⚠️ "
                print(f"[{generated}/{args.count}] {quality_icon} {l1} ({level}) - {pattern['type']} | ${total_cost:.4f}")
                
            except Exception as e:
                print(f"❌ Failed: {l1}/{pattern['type']} - {e}")
                continue
    
    print(f"\n{'='*60}")
    print(f"✅ Generated: {generated}")
    print(f"⏭️  Skipped (existing): {skipped}")
    print(f"🚫 Filtered (quality): {filtered}")
    print(f"💰 Estimated cost: ${total_cost:.4f}")
    print(f"📁 Output: {output_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
