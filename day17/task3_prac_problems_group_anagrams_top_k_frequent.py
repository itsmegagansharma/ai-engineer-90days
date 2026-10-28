"""
Day 17 · Task 3 · Practice: Problems: Group Anagrams & Top K Frequent

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Group Anagrams ----------------
def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams. Key idea: sorted letters as a dict key."""
    pass


# ---------------- Top K Frequent ----------------
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """The k most common values. Try collections.Counter."""
    pass


if __name__ == "__main__":
    # Group Anagrams
    groups = sorted(sorted(g) for g in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    assert groups == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    # Top K Frequent
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("All tests passed!")
