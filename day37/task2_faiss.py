"""
Day 37 · Task 2: FAISS

Build an index and search the same data. Compare speed.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install faiss-cpu
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
docs = [...]  # reuse your chunks

emb = model.encode(docs, normalize_embeddings=True).astype("float32")
index = faiss.IndexFlatIP(emb.shape[1])     # inner product = cosine (normalized)

# TODO: index.add(emb); search a query; print the top 3 docs
# TODO: time Chroma vs FAISS on the same 1,000 docs
