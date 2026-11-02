# PyTorch MNIST Demo

A tiny project that trains a convolutional neural network to recognize handwritten digits.

## Setup (Python 3.9+)

```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# macOS/Linux:  source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python train.py     # downloads MNIST, trains ~3 epochs (about a minute on CPU), saves mnist_cnn.pt
python predict.py   # loads the saved model and predicts 10 test digits
```

Expect roughly 98-99% test accuracy.

## Files

- `model.py`   – the CNN definition
- `train.py`   – training and evaluation loop
- `predict.py` – inference on sample images

Tweak `EPOCHS`, `BATCH_SIZE`, or `LEARNING_RATE` at the top of `train.py`.
