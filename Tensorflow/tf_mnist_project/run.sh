#!/usr/bin/env bash
# One-click setup + train + predict (macOS / Linux)
set -e
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python train.py
python predict.py
