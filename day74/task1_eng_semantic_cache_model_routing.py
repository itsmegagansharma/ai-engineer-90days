"""
Day 74 · Task 1 · Engineering: Semantic cache & model routing

Add a semantic cache for repeated questions. Then: Send easy questions to a small model, hard ones to a big one.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Caching =====
import numpy as np

CACHE: list[tuple[np.ndarray, str]] = []   # (question embedding, answer)
THRESHOLD = 0.92


def cached_answer(q_emb: np.ndarray) -> str | None:
    # TODO: return the cached answer if any stored embedding has cosine similarity >= THRESHOLD
    pass


def store(q_emb: np.ndarray, answer: str) -> None:
    CACHE.append((q_emb, answer))


# ===== Part 2: Routing =====
def pick_model(question: str) -> str:
    # TODO: short/simple questions -> small cheap model; long, multi-step or code -> big model
    #       start with rules (length, keywords); later try an LLM classifier
    pass
