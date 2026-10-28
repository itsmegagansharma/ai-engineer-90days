"""
Day 43 · Task 2 · AI & ML: Hybrid search: BM25 + rank fusion

pip install rank_bm25 and run keyword search over your chunks. Then: Merge BM25 and vector results with reciprocal rank fusion.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: BM25 =====
# pip install rank_bm25
from rank_bm25 import BM25Okapi

docs = [...]  # your chunks
tokenized = [d.lower().split() for d in docs]
bm25 = BM25Okapi(tokenized)

# TODO: scores = bm25.get_scores(query.lower().split()); print top 5


# ===== Part 2: Combine =====
def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[str]:
    """Each ranking is a list of doc ids, best first. Return the fused order."""
    scores: dict[str, float] = {}
    # TODO: for each ranking, for rank, doc_id: scores[doc_id] += 1 / (k + rank + 1)
    # TODO: return ids sorted by score, highest first
    pass


assert reciprocal_rank_fusion([["a", "b", "c"], ["b", "a", "d"]])[:2] in (["a", "b"], ["b", "a"])
