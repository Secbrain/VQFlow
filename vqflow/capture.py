"""
VQFlow Dataset Capture Module
-----------------------------
Implements the end-to-end pipeline for controlled video playback
and packet capture, as described in the VQFlow paper (Algorithm 1).
"""

import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from vqflow.utils import ensure_dir, timestamp
from vqflow import config


def capture_video(video_name: str, url: str, duration: int, run_id: int):
    """Capture a single video playback session."""
    ensure_dir(config.ROOT_PATH)
    video_dir = os.path.join(config.ROOT_PATH, video_name)
    ensure_dir(video_dir)

    filename = os.path.join(video_dir, f"{video_name}_{run_id}_{timestamp()}.pcap")

    # Start tshark
    tshark_call = [
        config.TSHARK_PATH, "-F", "pcap", "-f", config.CAPTURE_FILTER,
        "-i", config.INTERFACE, "-w", filename
    ]
    tshark_proc = subprocess.Popen(tshark_call)

    # Configure Chrome
    chrome_options = webdriver.ChromeOptions()
    for arg in config.CHROME_ARGS:
        chrome_options.add_argument(arg)
    if os.path.exists(config.ADBLOCK_EXTENSION):
        chrome_options.add_extension(config.ADBLOCK_EXTENSION)

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 30)

    try:
        driver.get(url.strip('"'))
        time.sleep(duration)
    finally:
        driver.quit()
        tshark_proc.kill()


def harvest_video(video_name: str, url: str, duration: int, n_runs: int):
    """Perform repeated captures for one video title."""
    for i in range(n_runs):
        print(f"[INFO] Capturing {video_name} | Run {i+1}/{n_runs}")
        capture_video(video_name, url, duration, i)
