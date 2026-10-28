"""
Day 11 · Task 3 · Practice: Problems: Majority Element & Missing Number

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Majority Element ----------------
def majority_element(nums: list[int]) -> int:
    """The value that appears more than n/2 times."""
    pass


# ---------------- Missing Number ----------------
def missing_number(nums: list[int]) -> int:
    """nums has n distinct numbers from 0..n. Return the missing one."""
    pass


if __name__ == "__main__":
    # Majority Element
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    # Missing Number
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    print("All tests passed!")
