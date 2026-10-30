# Simple TensorFlow Project: MNIST Digit Classifier

Trains a small neural network to recognise handwritten digits (0-9).

## Quick start

**Windows:** double-click `run.bat`
**macOS / Linux:** `./run.sh`

This creates a virtual environment, installs TensorFlow, trains the model
(~1 minute on CPU), saves it to `model/mnist.keras`, and runs sample predictions.

## Manual run

```
pip install -r requirements.txt
python train.py
python predict.py
```

## Files

| File               | Purpose                                      |
|--------------------|----------------------------------------------|
| `train.py`         | Loads MNIST, trains, evaluates, saves model  |
| `predict.py`       | Loads saved model, predicts 10 random digits |
| `requirements.txt` | Python dependencies                          |
| `run.bat / run.sh` | One-step setup and run scripts               |

## Notes

- Requires Python 3.9 - 3.12 (check TensorFlow's site for newer versions).
- The MNIST dataset downloads automatically on first run (internet needed once).
- Expected test accuracy: ~97-98%.
