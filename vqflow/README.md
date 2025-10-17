# VQFlow Dataset Capture

This repository provides the automated capture pipeline used in **VQFlow**.

It automates YouTube playback under controlled QoS conditions while recording encrypted network traces using `tshark`.

## Features
- Automated capture via Selenium and headless Chrome
- Ad-blocker support to skip ads
- Concurrent traffic capture with `tshark`
- Modular, reproducible design

## Usage
```bash
pip install -r requirements.txt
python run_capture.py
