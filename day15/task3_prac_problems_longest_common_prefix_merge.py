"""
Day 15 · Task 3 · Practice: Problems: Longest Common Prefix & Merge Sorted Lists

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Longest Common Prefix ----------------
def longest_common_prefix(words: list[str]) -> str:
    pass


# ---------------- Merge Sorted Lists ----------------
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list without calling sorted(). Two pointers."""
    pass


if __name__ == "__main__":
    # Longest Common Prefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "car"]) == ""
    # Merge Sorted Lists
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1]) == [1]
    print("All tests passed!")
