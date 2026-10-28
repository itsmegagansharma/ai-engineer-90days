"""
Day 38 · Task 3: Keep metadata

Store file name and page number with each chunk.

Complete every TODO, run the file, and tick this task on the tracker.
"""
"""ingest.py: load every PDF in a folder into Chroma with metadata.
Run: python day38/task3_ingest.py docs/"""
import sys
from pathlib import Path

import chromadb

# TODO: from task1_loaders import load_pdf; from task2_chunking import chunk_text
# TODO: for each page -> chunks -> col.add(ids=f"{file}-{page}-{i}", documents=chunk,
#        metadatas={"source": file, "page": page})
