"""
Day 10 · Task 1: Type hints

Annotate all functions: def add(a: float, b: float) -> float. Try list[str], dict[str, int], str | None.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Add type hints to every function. Then run: pip install mypy && mypy day10/task1_type_hints.py

def average(nums):
    return sum(nums) / len(nums)

def find_user(users, name):
    for u in users:
        if u["name"] == name:
            return u
    return None          # hint: return type is dict | None

def tag_counts(tags):
    counts = {}
    for t in tags:
        counts[t] = counts.get(t, 0) + 1
    return counts
