"""
Day 15 · Task 2: Broadcasting and vector math

Add, multiply, dot product. Compute cosine similarity of two vectors by hand.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    # TODO: dot(a, b) / (norm(a) * norm(b))
    pass


cat = np.array([0.9, 0.1, 0.3])
kitten = np.array([0.85, 0.15, 0.35])
car = np.array([0.1, 0.9, 0.2])

print(cosine_similarity(cat, kitten))  # close to 1
print(cosine_similarity(cat, car))     # much lower
# This is exactly how semantic search compares embeddings later in the plan.
