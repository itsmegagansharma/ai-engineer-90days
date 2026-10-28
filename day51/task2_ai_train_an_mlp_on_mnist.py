"""
Day 51 · Task 2 · AI & ML: Train an MLP on MNIST

Train a small network on MNIST; plot loss per epoch.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

train = datasets.MNIST("day49/data", train=True, download=True, transform=transforms.ToTensor())
loader = DataLoader(train, batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(3):
    total = 0.0
    for images, labels in loader:
        # TODO: forward pass, loss, optimizer.zero_grad(), loss.backward(), optimizer.step()
        pass
    print(f"epoch {epoch}: loss {total / len(loader):.3f}")

# TODO: evaluate accuracy on the test set (train=False)
