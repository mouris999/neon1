from __future__ import annotations
import json
import math
import pickle
import re
from pathlib import Path
from typing import Any

import numpy as np

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "neon_data.json"
MEMORY_FILE = BASE_DIR / "data" / "neon_memory.pkl"

EMBEDDING_SIZE = 24
HIDDEN_SIZE = 48
LEARNING_RATE = 0.05
DEFAULT_MEMORY_SIZE = 1000
DEFAULT_MAX_SEQUENCE_LENGTH = 100
DEFAULT_EPOCHS = 150

SPECIAL_TOKENS = ["<bos>", "<eos>", "<pad>", "<unk>"]

def tokenize(text: str) -> list[str]:
    """
    Tokenizes the input text into a list of tokens.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list[str]: A list of tokens extracted from the input text.
    """
    # Use regex to split the text into words and punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    return tokens