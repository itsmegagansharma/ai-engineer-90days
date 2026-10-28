"""
Day 25 · Task 3 · Practice: Problems: Longest Substring Without Repeating & Container With Most Water

Solve both in the starter file, then run it: every assert must pass. Both use two pointers or a sliding window.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Longest Substring Without Repeating ----------------
def length_of_longest_substring(s: str) -> int:
    """Sliding window with a set or dict of last-seen positions."""
    pass


# ---------------- Container With Most Water ----------------
def max_area(heights: list[int]) -> int:
    """Two pointers from both ends; move the shorter side inward."""
    pass


if __name__ == "__main__":
    # Longest Substring Without Repeating
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    # Container With Most Water
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("All tests passed!")
