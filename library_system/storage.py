"""
Storage Module (Module 2) - STARTER CODE (Contains Bug #2)
Responsible: Developer 2 / Branch: fix/storage

BUG DESCRIPTION:
1. `load_books` does not check if the parsed JSON data is actually a list!
   If a JSON object (dict) is loaded, it returns it directly instead of raising ValueError.
2. `open()` calls are missing `encoding="utf-8"`, causing failures on international characters.
"""

import json
import os
from typing import List, Dict, Any


def load_books(filepath: str) -> List[Dict[str, Any]]:
    """
    Load a list of book dictionaries from a JSON file.

    TODO (Dev 2):
    1. Ensure file is opened with encoding="utf-8".
    2. Check if parsed data is a list. If not, raise ValueError("Catalog data must be a list of book dictionaries").
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Database file not found: '{filepath}'")

    # BUG #2: Missing encoding="utf-8" AND missing type validation!
    with open(filepath, "r") as f:
        data = json.load(f)

    # Missing check: if not isinstance(data, list): raise ValueError(...)
    return data


def save_books(filepath: str, books: List[Dict[str, Any]], indent: int = 2) -> None:
    """
    Save a list of book dictionaries to a JSON file.

    TODO (Dev 2):
    Ensure file is opened with encoding="utf-8" and json.dump uses ensure_ascii=False.
    """
    if not isinstance(books, list):
        raise TypeError(f"Books data must be a list, got {type(books).__name__}")

    dir_path = os.path.dirname(filepath)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # BUG #2B: Missing encoding="utf-8"
    with open(filepath, "w") as f:
        json.dump(books, f, indent=indent)
