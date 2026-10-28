"""
Day 37 · Task 1: Chroma

Create a collection, add documents with metadata, query.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install chromadb
import chromadb

client = chromadb.PersistentClient(path="day37/chroma")
col = client.get_or_create_collection("notes")

# TODO: col.add(ids=[...], documents=[...], metadatas=[{"source": ..., "topic": ...}])
# TODO: res = col.query(query_texts=["..."], n_results=3); print documents and distances
