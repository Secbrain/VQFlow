#!/usr/bin/env python3
"""
Run the VQFlow Capture Pipeline.
"""

import json
from vqflow.capture import harvest_video
from vqflow.utils import load_json
from vqflow import config

def main():
    zidian = load_json(config.DICT_PATH)
    titles = load_json(config.TITLE_PATH)

    for name in titles:
        url = zidian.get(f"{name}_url")
        duration = int(zidian.get(f"{name}_duration", 0))
        if not url or not duration:
            print(f"[WARN] Missing metadata for {name}, skipping.")
            continue
        harvest_video(name, url, duration, config.REPEAT_PER_VIDEO)

if __name__ == "__main__":
    main()
