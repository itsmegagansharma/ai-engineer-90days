"""
Day 45 · Task 2: Parent-document retrieval

Search small chunks, return their larger parent section.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Parent-document retrieval:
#   - split each section into small chunks (~200 chars) for precise search
#   - store parent_id in metadata
#   - after search, return the full parent section (~1500 chars) to the LLM

parents: dict[str, str] = {}    # parent_id -> full section text

# TODO: build parents + small chunks; search small; dedupe by parent_id; return parent texts
