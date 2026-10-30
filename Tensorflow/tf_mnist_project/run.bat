@echo off
REM One-click setup + train + predict (Windows)
if not exist .venv (
    python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python train.py
python predict.py
pause
