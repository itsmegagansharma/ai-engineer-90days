"""
Day 76 · Task 1: Caching

Add a semantic cache for repeated questions.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import numpy as np

CACHE: list[tuple[np.ndarray, str]] = []   # (question embedding, answer)
THRESHOLD = 0.92


def cached_answer(q_emb: np.ndarray) -> str | None:
    # TODO: return the cached answer if any stored embedding has cosine similarity >= THRESHOLD
    pass


def store(q_emb: np.ndarray, answer: str) -> None:
    CACHE.append((q_emb, answer))
