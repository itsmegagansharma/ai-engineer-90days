"""
Day 36 · Task 2: Generate embeddings

Use sentence-transformers (all-MiniLM-L6-v2) or an API embedding model.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = ["The cat sits on the mat", "A kitten is resting on a rug", "Stock prices fell today"]

# TODO: embeddings = model.encode(sentences); print the shape
# TODO: print the first 5 numbers of the first embedding
