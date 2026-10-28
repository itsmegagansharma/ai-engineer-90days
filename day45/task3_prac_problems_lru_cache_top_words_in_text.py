"""
Day 45 · Task 3 · Practice: Problems: LRU Cache & Top Words in Text

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- LRU Cache ----------------
from collections import OrderedDict


class LRUCache:
    """get/put in O(1). Evict the least recently used key when over capacity."""

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# ---------------- Top Words in Text ----------------
import re
from collections import Counter


def top_words(text: str, k: int = 3) -> list[tuple[str, int]]:
    """Lowercase, split into words with re.findall(r"[a-z']+", ...), return the k most common."""
    pass


if __name__ == "__main__":
    # LRU Cache
    c = LRUCache(2); c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    # Top Words in Text
    assert top_words("the cat and the hat and the bat", 2) == [("the", 3), ("and", 2)]
    print("All tests passed!")
