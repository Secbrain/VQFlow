"""
VQFlow Configuration Module
----------------------------
Contains constants and default paths for dataset capture.
"""

import os

# Root paths
ROOT_PATH = "./pcap-qos/"
DICT_PATH = "./dict.json"
TITLE_PATH = "./title.json"
ADBLOCK_EXTENSION = "./4.5.1_0.crx"

# Network capture configuration
TSHARK_PATH = "tshark"
INTERFACE = "eth0"
CAPTURE_FILTER = "tcp port 443"

# Browser options
CHROME_ARGS = [
    "--remote-debugging-pipe",
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]

# Number of repetitions per video (default)
REPEAT_PER_VIDEO = 10

# Create directories if missing
os.makedirs(ROOT_PATH, exist_ok=True)
