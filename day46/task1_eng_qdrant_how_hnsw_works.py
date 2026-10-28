"""
Day 46 · Task 1 · Engineering: Qdrant & how HNSW works

Run Qdrant in Docker and try its quickstart. Then: Read about HNSW indexes and why they make search fast.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Qdrant =====
# docker run -p 6333:6333 qdrant/qdrant
# pip install qdrant-client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

client = QdrantClient("localhost", port=6333)
# TODO: create collection (size=384, Distance.COSINE), upsert points with payloads, search


# ===== Part 2: Indexes =====
# ## HNSW in my own words
# - What problem does an index solve?
# - What is approximate nearest neighbour search?
# - Trade-off between speed and accuracy:
