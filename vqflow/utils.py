"""
Utility functions for VQFlow Dataset Collection.
"""

import json
from datetime import datetime
from pathlib import Path

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def timestamp() -> str:
    """Return timestamp suitable for filenames."""
    return datetime.now().strftime("%H_%M_%S")

def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
