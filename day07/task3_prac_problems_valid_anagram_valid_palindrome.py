"""
Day 07 · Task 3 · Practice: Problems: Valid Anagram & Valid Palindrome

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Valid Anagram ----------------
def is_anagram(s: str, t: str) -> bool:
    """True if t uses exactly the same letters as s."""
    pass


# ---------------- Valid Palindrome ----------------
def is_palindrome(s: str) -> bool:
    """Ignore case and non-alphanumeric characters."""
    pass


if __name__ == "__main__":
    # Valid Anagram
    assert is_anagram("listen", "silent")
    assert not is_anagram("rat", "car")
    # Valid Palindrome
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("race a car")
    print("All tests passed!")
