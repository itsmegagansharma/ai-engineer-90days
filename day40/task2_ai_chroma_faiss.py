"""
Day 40 · Task 2 · AI & ML: Chroma & FAISS

Create a collection, add documents with metadata, query. Then: Build an index and search the same data. Compare speed. Then: Filter results by source or date.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Chroma =====
# pip install chromadb
import chromadb

client = chromadb.PersistentClient(path="day40/chroma")
col = client.get_or_create_collection("notes")

# TODO: col.add(ids=[...], documents=[...], metadatas=[{"source": ..., "topic": ...}])
# TODO: res = col.query(query_texts=["..."], n_results=3); print documents and distances


# ===== Part 2: FAISS =====
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


# ===== Part 3: Metadata filters =====
# Using the Chroma collection from task1:
# TODO: query with where={"topic": "python"} and see only matching chunks come back
# TODO: try where={"$and": [{"topic": "python"}, {"source": "day07"}]}
