"""
Day 08 · Task 2 · AI & ML: Vectorize a loop with NumPy

Replace a Python loop with a NumPy expression and time both.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import time
import numpy as np

nums = list(range(1_000_000))

start = time.perf_counter()
squares = [n * n for n in nums]
print("python:", time.perf_counter() - start)

# TODO: do the same with a numpy array (arr * arr) and time it
