"""
Day 43 · Task 1: BM25

pip install rank_bm25 and run keyword search over your chunks.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install rank_bm25
from rank_bm25 import BM25Okapi

docs = [...]  # your chunks
tokenized = [d.lower().split() for d in docs]
bm25 = BM25Okapi(tokenized)

# TODO: scores = bm25.get_scores(query.lower().split()); print top 5
