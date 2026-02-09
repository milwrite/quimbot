"""
Qwen Model Evaluation Framework
Sophisticated evaluation toolkit for comparing LLM variants.
"""

__version__ = "0.2.0"
__author__ = "milwright"

from .core import ModelEvaluator, EvalConfig
from .metrics import MetricRegistry
from .reporters import MarkdownReporter, JSONReporter

__all__ = [
    "ModelEvaluator",
    "EvalConfig", 
    "MetricRegistry",
    "MarkdownReporter",
    "JSONReporter",
]
