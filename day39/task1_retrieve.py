"""
Day 39 · Task 1: Retrieve

Embed the question and get the top 5 chunks.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import chromadb

col = chromadb.PersistentClient(path="day37/chroma").get_or_create_collection("docs")


def retrieve(question: str, k: int = 5) -> list[dict]:
    # TODO: query Chroma; return [{"text": ..., "source": ..., "page": ...}, ...]
    pass
