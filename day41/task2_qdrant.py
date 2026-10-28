"""
Day 41 · Task 2: Qdrant

Run Qdrant in Docker and try its quickstart.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# docker run -p 6333:6333 qdrant/qdrant
# pip install qdrant-client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

client = QdrantClient("localhost", port=6333)
# TODO: create collection (size=384, Distance.COSINE), upsert points with payloads, search
