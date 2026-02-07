#!/usr/bin/env python3
"""
Generate scaffolding dialogues using Kimi K2.5 via OpenRouter.
Uses TOEFL11 error patterns to create pedagogical conversations.
"""

import argparse
import json
import os
import random
from pathlib import Path
from openai import OpenAI

# Error patterns by L1 (from TOEFL11 research)
ERROR_PATTERNS = {
    "Spanish": [
        {"error": "She is teacher", "correct": "She is a teacher", "type": "article_omission"},
        {"error": "I have three book", "correct": "I have three books", "type": "plural_omission"},
        {"error": "Yesterday I go to store", "correct": "Yesterday I went to the store", "type": "past_tense"},
        {"error": "He want to eat", "correct": "He wants to eat", "type": "verb_agreement"},
        {"error": "I am agree with you", "correct": "I agree with you", "type": "be_verb_overuse"},
    ],
    "Chinese": [
        {"error": "I have three book", "correct": "I have three books", "type": "plural_omission"},
        {"error": "Yesterday I go to school", "correct": "Yesterday I went to school", "type": "past_tense"},
        {"error": "She is very beautiful girl", "correct": "She is a very beautiful girl", "type": "article_omission"},
        {"error": "I very like this", "correct": "I really like this", "type": "adverb_placement"},
        {"error": "He go to work everyday", "correct": "He goes to work everyday", "type": "verb_agreement"},
    ],
    "Arabic": [
        {"error": "She is good teacher", "correct": "She is a good teacher", "type": "article_omission"},
        {"error": "I have many informations", "correct": "I have a lot of information", "type": "uncountable_plural"},
        {"error": "He is very tall man", "correct": "He is a very tall man", "type": "article_omission"},
        {"error": "I go to school yesterday", "correct": "I went to school yesterday", "type": "past_tense"},
        {"error": "They was happy", "correct": "They were happy", "type": "verb_agreement"},
    ],
}

# Simpler template that returns plain dialogue text
SCAFFOLDING_TEMPLATE = """Generate a natural 3-4 turn teacher-student dialogue where:
- Student (native {l1} speaker, {level} English) makes this error: "{error}"
- Teacher uses adaptive scaffolding: asks questions, recasts naturally, or expands (NO explicit correction)
- Student responds
- Teacher encourages

The teacher should model the correct form "{correct}" naturally without saying "that's wrong" or explaining rules.

Return ONLY the dialogue in this format:
Student: [student's message]
Teacher: [teacher's response]
Student: [student's next message]
Teacher: [teacher's final encouragement]"""


def generate_dialogue(pattern, l1, level, client, model="moonshotai/kimi-k2.5", debug=False):
    """Generate a single scaffolding dialogue using Kimi K2.5 via OpenRouter."""
    
    prompt = SCAFFOLDING_TEMPLATE.format(
        l1=l1,
        level=level,
        error=pattern['error'],
        correct=pattern['correct']
    )
    
    # Generate via OpenRouter
    # Note: Kimi K2.5 is a thinking model - needs high max_tokens for reasoning + response
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,  # High limit for thinking models
        temperature=0.7
    )
    
    generated_text = response.choices[0].message.content
    
    if debug:
        print(f"\n{'='*60}")
        print(f"RAW RESPONSE:\n{generated_text}")
        print(f"{'='*60}\n")
    
    # Parse dialogue format
    messages = []
    lines = generated_text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('Student:'):
            messages.append({"role": "user", "content": line.replace('Student:', '').strip()})
        elif line.startswith('Teacher:'):
            messages.append({"role": "assistant", "content": line.replace('Teacher:', '').strip()})
    
    # Fallback if parsing failed: store raw text
    if not messages:
        messages = [{"role": "assistant", "content": generated_text}]
    
    return {
        "l1_background": l1,
        "proficiency": level,
        "error_type": pattern['type'],
        "error_pattern": pattern['error'],
        "correct_form": pattern['correct'],
        "messages": messages,
        "raw_response": generated_text if debug else None
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="scaffolding_dialogues.jsonl", help="Output JSONL file")
    parser.add_argument("--count", type=int, default=100, help="Number of dialogues to generate")
    parser.add_argument("--model", default="moonshotai/kimi-k2.5", help="OpenRouter model to use")
    parser.add_argument("--debug", action="store_true", help="Print raw responses")
    args = parser.parse_args()
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("❌ Missing OPENROUTER_API_KEY")
    
    # Initialize OpenRouter client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    print(f"Generating {args.count} scaffolding dialogues using {args.model}...")
    print(f"Output: {args.output}\n")
    
    output_path = Path(args.output)
    generated = 0
    
    with output_path.open("w") as f:
        while generated < args.count:
            # Pick random L1 and error pattern
            l1 = random.choice(list(ERROR_PATTERNS.keys()))
            pattern = random.choice(ERROR_PATTERNS[l1])
            level = random.choice(["beginner", "intermediate"])
            
            try:
                dialogue = generate_dialogue(
                    pattern, l1, level, client, 
                    model=args.model, debug=args.debug
                )
                
                f.write(json.dumps(dialogue) + "\n")
                f.flush()  # Ensure writes happen immediately
                generated += 1
                
                print(f"[{generated}/{args.count}] Generated: {l1} ({level}) - {pattern['type']}")
                
            except Exception as e:
                print(f"❌ Error generating dialogue: {e}")
                import traceback
                traceback.print_exc()
                continue
    
    print(f"\n✅ Generated {generated} scaffolding dialogues!")
    print(f"Saved to: {args.output}")


if __name__ == "__main__":
    main()
