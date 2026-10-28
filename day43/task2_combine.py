"""
Day 43 · Task 2: Combine

Merge BM25 and vector results with reciprocal rank fusion.

Complete every TODO, run the file, and tick this task on the tracker.
"""
def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[str]:
    """Each ranking is a list of doc ids, best first. Return the fused order."""
    scores: dict[str, float] = {}
    # TODO: for each ranking, for rank, doc_id: scores[doc_id] += 1 / (k + rank + 1)
    # TODO: return ids sorted by score, highest first
    pass


assert reciprocal_rank_fusion([["a", "b", "c"], ["b", "a", "d"]])[:2] in (["a", "b"], ["b", "a"])
