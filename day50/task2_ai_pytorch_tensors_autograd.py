"""
Day 50 · Task 2 · AI & ML: PyTorch tensors & autograd

Follow the PyTorch basics tutorial: tensors, datasets, autograd.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import torch

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = (x ** 2).sum()

# TODO: call y.backward() and print x.grad. Is it 2*x?
# TODO: make a 2x3 random tensor, multiply it by a 3x1 tensor (@), print the shape
