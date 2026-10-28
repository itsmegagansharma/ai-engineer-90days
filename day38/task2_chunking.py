"""
Day 38 · Task 2: Chunking

Fixed-size chunks with overlap (e.g. 800 chars, 100 overlap). Try sentence-aware splitting.

Complete every TODO, run the file, and tick this task on the tracker.
"""
def chunk_text(text: str, size: int = 800, overlap: int = 100) -> list[str]:
    """Split text into overlapping chunks of about `size` characters."""
    # TODO: slide a window of `size` chars, stepping by size - overlap
    # Stretch: avoid cutting mid-sentence (split on ". " first, then pack sentences into chunks)
    pass


assert len(chunk_text("a" * 2000)) == 3
