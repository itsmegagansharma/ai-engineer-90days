"""
Day 39 · Task 2: Augment

Build a prompt with the chunks and an instruction to cite sources.

Complete every TODO, run the file, and tick this task on the tracker.
"""
def build_prompt(question: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"[{i + 1}] (source: {c['source']}, page {c['page']})\n{c['text']}" for i, c in enumerate(chunks)
    )
    # TODO: return a prompt that says: answer only from the context, cite like [1], [2],
    #       and say "I don't know" if the answer isn't in the context
    pass
