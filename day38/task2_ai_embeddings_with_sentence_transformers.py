"""
Day 38 · Task 2 · AI & ML: Embeddings with sentence-transformers

An embedding is a list of numbers; similar meaning → close vectors. Then: Use sentence-transformers (all-MiniLM-L6-v2) or an API embedding model.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Concept =====
# ## Explain embeddings to a friend (5 lines max)
#
# ## Why do "dog" and "puppy" end up close together?


# ===== Part 2: Generate embeddings =====
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = ["The cat sits on the mat", "A kitten is resting on a rug", "Stock prices fell today"]

# TODO: embeddings = model.encode(sentences); print the shape
# TODO: print the first 5 numbers of the first embedding
