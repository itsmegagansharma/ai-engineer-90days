"""
Day 03 · Task 2 · AI & ML: Tokens & context windows

Use tiktoken to count tokens in a paragraph. Learn what a context window limits.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# pip install tiktoken
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "Agents reason, plan, and use tools. नमस्ते!"

# TODO 1: tokens = enc.encode(text); print len(tokens) and the tokens
# TODO 2: print each token decoded on its own: [enc.decode([t]) for t in tokens]
# TODO 3: compare token counts for the same sentence in English vs Hindi. Why the difference?
