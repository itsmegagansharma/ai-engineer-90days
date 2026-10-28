"""
Day 44 · Task 1: Cross-encoder reranker

Retrieve 20, rerank with a cross-encoder, keep top 5.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(question: str, chunks: list[str], top_n: int = 5) -> list[str]:
    # TODO: scores = reranker.predict([(question, c) for c in chunks]); return top_n chunks by score
    pass

# TODO: retrieve 20 with hybrid search, rerank to 5, compare answers before/after
