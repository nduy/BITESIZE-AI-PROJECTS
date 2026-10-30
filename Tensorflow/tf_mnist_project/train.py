"""Train a small neural network on MNIST handwritten digits."""
import os
import tensorflow as tf

MODEL_PATH = os.path.join("model", "mnist.keras")


def main():
    # 1. Load data (downloaded automatically on first run)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # 2. Build the model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(28, 28)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    model.summary()

    # 3. Train
    model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

    # 4. Evaluate
    loss, acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"\nTest accuracy: {acc:.4f}  (loss: {loss:.4f})")

    # 5. Save
    os.makedirs("model", exist_ok=True)
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
