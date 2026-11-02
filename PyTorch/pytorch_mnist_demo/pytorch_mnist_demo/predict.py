"""Load the trained model and predict a few test digits. Run:  python predict.py"""
import torch
from torchvision import datasets, transforms

from model import SimpleCNN


def main():
    model = SimpleCNN()
    model.load_state_dict(torch.load("mnist_cnn.pt", map_location="cpu"))
    model.eval()

    tfm = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
    ])
    test_set = datasets.MNIST("data", train=False, download=True, transform=tfm)

    for i in range(10):
        image, label = test_set[i]
        with torch.no_grad():
            pred = model(image.unsqueeze(0)).argmax(1).item()
        status = "OK " if pred == label else "BAD"
        print(f"[{status}] sample {i}: true={label} predicted={pred}")


if __name__ == "__main__":
    main()
