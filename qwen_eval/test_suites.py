"""Test suite definitions and loaders."""

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

logger = logging.getLogger(__name__)


@dataclass
class TestSuite:
    """A collection of evaluation tests."""
    
    name: str
    tests: List[Dict[str, str]]
    description: str = ""
    
    def __len__(self) -> int:
        return len(self.tests)


# Built-in test suites
PEDAGOGICAL = TestSuite(
    name="pedagogical",
    description="Tests for inquiry-led, scaffolding dialogue",
    tests=[
        {
            "name": "scaffolding_inquiry",
            "prompt": "I'm struggling to understand why photosynthesis requires light. Can you help?",
            "criteria": "Should ask questions, scaffold thinking, avoid direct answers",
            "tags": ["inquiry", "scaffolding"]
        },
        {
            "name": "adaptive_depth",
            "prompt": "What's a derivative in calculus?",
            "criteria": "Should probe understanding level before explaining",
            "tags": ["adaptive", "probing"]
        },
        {
            "name": "socratic_method",
            "prompt": "Tell me how to solve 2x + 5 = 13",
            "criteria": "Should guide through questions rather than showing steps",
            "tags": ["socratic", "math"]
        },
        {
            "name": "metacognitive",
            "prompt": "I don't know how to start writing this essay about climate change.",
            "criteria": "Should help identify what they DO know, guide process",
            "tags": ["metacognition", "writing"]
        },
        {
            "name": "conceptual_confusion",
            "prompt": "I keep mixing up mitosis and meiosis. They seem the same to me.",
            "criteria": "Should explore the confusion, ask diagnostic questions",
            "tags": ["confusion", "diagnostics"]
        }
    ]
)

DIALOGUE = TestSuite(
    name="dialogue",
    description="Multi-turn conversational patterns",
    tests=[
        {
            "name": "multi_turn_context",
            "prompt": "I want to learn Python but I've never programmed before.",
            "criteria": "Should establish context through questions",
            "tags": ["context", "programming"]
        },
        {
            "name": "collaborative",
            "prompt": "Can you explain how neural networks work?",
            "criteria": "Should invite co-investigation, not lecture",
            "tags": ["collaboration", "ai"]
        },
        {
            "name": "open_ended",
            "prompt": "I'm interested in learning about philosophy. Where should I start?",
            "criteria": "Should explore interests, guide discovery",
            "tags": ["open-ended", "guidance"]
        }
    ]
)

BASELINE = TestSuite(
    name="baseline",
    description="Sanity checks for basic functionality",
    tests=[
        {
            "name": "factual_recall",
            "prompt": "What is the capital of France?",
            "criteria": "Simple factual answer",
            "tags": ["factual", "simple"]
        },
        {
            "name": "basic_instruction",
            "prompt": "How do I make a list in Python?",
            "criteria": "Clear technical explanation",
            "tags": ["instruction", "programming"]
        },
        {
            "name": "math_problem",
            "prompt": "What is 15% of 240?",
            "criteria": "Correct numerical answer",
            "tags": ["math", "computation"]
        }
    ]
)

STRESS_TEST = TestSuite(
    name="stress",
    description="Edge cases and challenging scenarios",
    tests=[
        {
            "name": "ambiguous_question",
            "prompt": "Why is the sky?",
            "criteria": "Should handle ambiguity, clarify intent",
            "tags": ["ambiguous", "clarification"]
        },
        {
            "name": "multiple_concepts",
            "prompt": "Explain quantum entanglement, superposition, and how they relate to quantum computing.",
            "criteria": "Should manage complexity, possibly break down",
            "tags": ["complex", "physics"]
        },
        {
            "name": "misconception",
            "prompt": "I learned that heavier objects fall faster. Is that true?",
            "criteria": "Should gently correct, explore understanding",
            "tags": ["misconception", "physics"]
        }
    ]
)


# Registry of all built-in suites
BUILT_IN_SUITES = {
    "pedagogical": PEDAGOGICAL,
    "dialogue": DIALOGUE,
    "baseline": BASELINE,
    "stress": STRESS_TEST
}


def load_test_suite(name_or_path: str) -> TestSuite:
    """
    Load a test suite by name or from a YAML file.
    
    Args:
        name_or_path: Built-in suite name or path to YAML file
        
    Returns:
        TestSuite instance
        
    Raises:
        ValueError: If suite not found
    """
    # Check built-in suites first
    if name_or_path in BUILT_IN_SUITES:
        logger.info(f"Loading built-in suite: {name_or_path}")
        return BUILT_IN_SUITES[name_or_path]
    
    # Try loading from file
    path = Path(name_or_path)
    if path.exists():
        logger.info(f"Loading custom suite from: {path}")
        return load_test_suite_from_yaml(path)
    
    raise ValueError(
        f"Test suite '{name_or_path}' not found. "
        f"Available: {', '.join(BUILT_IN_SUITES.keys())}"
    )


def load_test_suite_from_yaml(path: Path) -> TestSuite:
    """Load a custom test suite from YAML."""
    if not HAS_YAML:
        raise ImportError("pyyaml required for custom test suites. Install with: pip3 install pyyaml")
    
    with open(path) as f:
        data = yaml.safe_load(f)
    
    return TestSuite(
        name=data.get("name", path.stem),
        description=data.get("description", ""),
        tests=data.get("tests", [])
    )


def list_test_suites() -> Dict[str, TestSuite]:
    """Get all available built-in test suites."""
    return BUILT_IN_SUITES


def export_test_suite_template(path: Path) -> None:
    """Export a YAML template for custom test suites."""
    if not HAS_YAML:
        raise ImportError("pyyaml required to export templates. Install with: pip3 install pyyaml")
    
    template = {
        "name": "custom_suite",
        "description": "Your custom test suite",
        "tests": [
            {
                "name": "test_1",
                "prompt": "Your test prompt here",
                "criteria": "What you're evaluating for",
                "tags": ["tag1", "tag2"]
            }
        ]
    }
    
    with open(path, 'w') as f:
        yaml.dump(template, f, default_flow_style=False, sort_keys=False)
    
    logger.info(f"Template exported to: {path}")
