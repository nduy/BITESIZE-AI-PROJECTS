"""Load the trained model and predict a few random test digits."""
import os
import numpy as np
import tensorflow as tf

MODEL_PATH = os.path.join("model", "mnist.keras")


def main():
    if not os.path.exists(MODEL_PATH):
        raise SystemExit("No trained model found. Run train.py first.")

    model = tf.keras.models.load_model(MODEL_PATH)
    (_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_test = x_test.astype("float32") / 255.0

    idx = np.random.choice(len(x_test), 10, replace=False)
    probs = model.predict(x_test[idx], verbose=0)
    preds = probs.argmax(axis=1)

    print(f"{'Index':>6} {'Actual':>7} {'Predicted':>10} {'Confidence':>11}")
    for i, p, pr in zip(idx, preds, probs):
        mark = "" if p == y_test[i] else "  <-- wrong"
        print(f"{i:>6} {y_test[i]:>7} {p:>10} {pr[p]:>10.1%}{mark}")

    # Show one digit as ASCII art
    print("\nExample image:")
    img = x_test[idx[0]]
    for row in img:
        print("".join("#" if v > 0.5 else ("+" if v > 0.2 else " ") for v in row))
    print(f"Model predicts: {preds[0]}")


if __name__ == "__main__":
    main()
