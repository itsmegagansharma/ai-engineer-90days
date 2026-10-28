"""
Day 07 · Task 2 · AI & ML: NumPy arrays & cosine similarity

np.array, .shape, reshape, zeros, arange. Index rows and columns. Then: Add, multiply, dot product. Compute cosine similarity of two vectors by hand.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Arrays and shapes =====
import numpy as np

a = np.arange(12)
# TODO 1: print a.shape, then reshape to 3x4 and print it
# TODO 2: print the second row and the last column of the 3x4 array
# TODO 3: create a 3x3 array of zeros and a 3x3 identity matrix (np.eye)


# ===== Part 2: Broadcasting and vector math =====
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
