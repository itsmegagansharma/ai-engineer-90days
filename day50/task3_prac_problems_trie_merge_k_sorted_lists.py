"""
Day 50 · Task 3 · Practice: Problems: Trie & Merge K Sorted Lists

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Trie ----------------
class Trie:
    """insert(word), search(word), starts_with(prefix). Each node is a dict of children + an end flag."""

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


# ---------------- Merge K Sorted Lists ----------------
import heapq


def merge_k(lists: list[list[int]]) -> list[int]:
    """Merge k sorted Python lists with a heap of (value, list_index, element_index)."""
    pass


if __name__ == "__main__":
    # Trie
    t = Trie(); t.insert("apple")
    assert t.search("apple") and not t.search("app") and t.starts_with("app")
    # Merge K Sorted Lists
    assert merge_k([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("All tests passed!")
