"""
Day 41 · Task 2 · AI & ML: RAG: retrieve & augment

Embed the question and get the top 5 chunks. Then: Build a prompt with the chunks and an instruction to cite sources.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Retrieve =====
import chromadb

col = chromadb.PersistentClient(path="day40/chroma").get_or_create_collection("docs")


def retrieve(question: str, k: int = 5) -> list[dict]:
    # TODO: query Chroma; return [{"text": ..., "source": ..., "page": ...}, ...]
    pass


# ===== Part 2: Augment =====
def build_prompt(question: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"[{i + 1}] (source: {c['source']}, page {c['page']})\n{c['text']}" for i, c in enumerate(chunks)
    )
    # TODO: return a prompt that says: answer only from the context, cite like [1], [2],
    #       and say "I don't know" if the answer isn't in the context
    pass
