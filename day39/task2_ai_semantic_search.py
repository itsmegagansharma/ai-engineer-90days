"""
Day 39 · Task 2 · AI & ML: Semantic search

Embed 100 sentences, find the 5 closest to a query with cosine similarity.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
corpus = [line.strip() for line in open("day38/sentences.txt") if line.strip()]   # write 100 sentences
corpus_emb = model.encode(corpus, normalize_embeddings=True)


def search(query: str, k: int = 5) -> list[tuple[float, str]]:
    # TODO: encode the query (normalized), scores = corpus_emb @ q, return top k (score, sentence)
    pass


for score, text in search("how do I train a neural network"):
    print(f"{score:.3f}  {text}")
