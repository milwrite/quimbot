"""Evaluation metrics for response quality."""

import re
import logging
from typing import Callable, Dict, Any

logger = logging.getLogger(__name__)


MetricFunction = Callable[[str, str], Any]


class MetricRegistry:
    """Registry of evaluation metrics."""
    
    def __init__(self):
        self._metrics: Dict[str, MetricFunction] = {}
        self._register_default_metrics()
    
    def register(self, name: str, func: MetricFunction) -> None:
        """Register a custom metric."""
        self._metrics[name] = func
        logger.debug(f"Registered metric: {name}")
    
    def get(self, name: str) -> MetricFunction:
        """Get a metric function by name."""
        if name not in self._metrics:
            raise KeyError(f"Metric '{name}' not found. Available: {list(self._metrics.keys())}")
        return self._metrics[name]
    
    def list(self) -> list:
        """List all available metrics."""
        return list(self._metrics.keys())
    
    def _register_default_metrics(self) -> None:
        """Register built-in metrics."""
        
        # Basic metrics
        self.register("response_length", response_length)
        self.register("word_count", word_count)
        self.register("sentence_count", sentence_count)
        
        # Pedagogical metrics
        self.register("question_count", question_count)
        self.register("question_ratio", question_ratio)
        self.register("imperative_count", imperative_count)
        self.register("inquiry_markers", inquiry_markers)
        
        # Dialogue metrics
        self.register("collaborative_markers", collaborative_markers)
        self.register("personal_pronouns", personal_pronouns)
        self.register("hedging_phrases", hedging_phrases)
        
        # Complexity metrics
        self.register("avg_sentence_length", avg_sentence_length)
        self.register("unique_words", unique_words)
        self.register("lexical_diversity", lexical_diversity)


# ============================================================================
# Basic Metrics
# ============================================================================

def response_length(prompt: str, response: str) -> int:
    """Total character count."""
    return len(response)


def word_count(prompt: str, response: str) -> int:
    """Total word count."""
    return len(response.split())


def sentence_count(prompt: str, response: str) -> int:
    """Approximate sentence count."""
    sentences = re.split(r'[.!?]+', response)
    return len([s for s in sentences if s.strip()])


# ============================================================================
# Pedagogical Metrics
# ============================================================================

def question_count(prompt: str, response: str) -> int:
    """Count of question marks in response."""
    return response.count('?')


def question_ratio(prompt: str, response: str) -> float:
    """Ratio of questions to total sentences."""
    q_count = question_count(prompt, response)
    s_count = sentence_count(prompt, response)
    return q_count / s_count if s_count > 0 else 0.0


def imperative_count(prompt: str, response: str) -> int:
    """
    Count imperative sentences (commands).
    
    Rough heuristic: sentences starting with verbs like
    "Consider", "Try", "Think", "Let's", etc.
    """
    imperatives = [
        r'\bConsider\b', r'\bTry\b', r'\bThink\b', r'\bLet\'s\b',
        r'\bImagine\b', r'\bSuppose\b', r'\bStart\b', r'\bLook\b'
    ]
    
    count = 0
    for pattern in imperatives:
        count += len(re.findall(pattern, response, re.IGNORECASE))
    
    return count


def inquiry_markers(prompt: str, response: str) -> int:
    """
    Count inquiry-oriented phrases.
    
    Examples: "What do you think", "Can you tell me", "How would you"
    """
    markers = [
        r'\bWhat do you (think|know|remember)\b',
        r'\bCan you (tell|explain|describe)\b',
        r'\bHow (would|do|did) you\b',
        r'\bWhy (do|did|would) you\b',
        r'\bHave you (considered|thought|tried)\b'
    ]
    
    count = 0
    for pattern in markers:
        count += len(re.findall(pattern, response, re.IGNORECASE))
    
    return count


# ============================================================================
# Dialogue Metrics
# ============================================================================

def collaborative_markers(prompt: str, response: str) -> int:
    """
    Count collaborative language.
    
    Examples: "Let's", "We can", "Together"
    """
    markers = [
        r'\bLet\'s\b', r'\bWe can\b', r'\bWe might\b', r'\bWe could\b',
        r'\bTogether\b', r'\bYou and I\b'
    ]
    
    count = 0
    for pattern in markers:
        count += len(re.findall(pattern, response, re.IGNORECASE))
    
    return count


def personal_pronouns(prompt: str, response: str) -> Dict[str, int]:
    """Count first/second person pronouns."""
    
    first_person = len(re.findall(r'\b(I|me|my|mine|we|us|our|ours)\b', response, re.IGNORECASE))
    second_person = len(re.findall(r'\b(you|your|yours)\b', response, re.IGNORECASE))
    
    return {
        "first_person": first_person,
        "second_person": second_person,
        "total": first_person + second_person
    }


def hedging_phrases(prompt: str, response: str) -> int:
    """
    Count hedging language (indicates uncertainty, invites discussion).
    
    Examples: "might", "perhaps", "it seems", "possibly"
    """
    hedges = [
        r'\bmight\b', r'\bperhaps\b', r'\bpossibly\b', r'\bmaybe\b',
        r'\bit seems\b', r'\bappears to\b', r'\bcould be\b'
    ]
    
    count = 0
    for pattern in hedges:
        count += len(re.findall(pattern, response, re.IGNORECASE))
    
    return count


# ============================================================================
# Complexity Metrics
# ============================================================================

def avg_sentence_length(prompt: str, response: str) -> float:
    """Average words per sentence."""
    words = word_count(prompt, response)
    sentences = sentence_count(prompt, response)
    return words / sentences if sentences > 0 else 0.0


def unique_words(prompt: str, response: str) -> int:
    """Count of unique words (case-insensitive)."""
    words = re.findall(r'\b\w+\b', response.lower())
    return len(set(words))


def lexical_diversity(prompt: str, response: str) -> float:
    """
    Type-token ratio (unique words / total words).
    Indicator of vocabulary richness.
    """
    total = word_count(prompt, response)
    unique = unique_words(prompt, response)
    return unique / total if total > 0 else 0.0


# ============================================================================
# Utility Functions
# ============================================================================

def compute_all_metrics(prompt: str, response: str) -> Dict[str, Any]:
    """Compute all available metrics for a response."""
    
    registry = MetricRegistry()
    results = {}
    
    for metric_name in registry.list():
        try:
            metric_fn = registry.get(metric_name)
            results[metric_name] = metric_fn(prompt, response)
        except Exception as e:
            logger.warning(f"Metric {metric_name} failed: {e}")
            results[metric_name] = None
    
    return results
