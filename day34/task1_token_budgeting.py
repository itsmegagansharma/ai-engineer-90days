"""
Day 34 · Task 1: Token budgeting

Count tokens before each call; keep under a limit.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
MAX_TOKENS = 1000


def count_tokens(messages: list[dict]) -> int:
    # TODO: sum len(enc.encode(m["content"])) + 4 per message
    pass


def trim(messages: list[dict]) -> list[dict]:
    # TODO: keep the system message, drop the oldest user/assistant messages until under MAX_TOKENS
    pass
