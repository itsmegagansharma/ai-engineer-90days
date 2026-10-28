"""
Day 67 · Task 3 · Practice: Problems: JSON Schema Check & Deep Merge

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- JSON Schema Check ----------------
def check(data: dict, schema: dict) -> list[str]:
    """schema maps field -> type (str, int, float, list). Return a list of problems:
    missing fields and wrong types. Like a mini Pydantic for validating LLM output."""
    pass


# ---------------- Deep Merge ----------------
def deep_merge(a: dict, b: dict) -> dict:
    """Return a new dict: b's values win, but nested dicts are merged recursively.
    Agent frameworks merge state updates like this."""
    pass


if __name__ == "__main__":
    # JSON Schema Check
    schema = {"name": str, "age": int, "tags": list}
    assert check({"name": "a", "age": 3, "tags": []}, schema) == []
    assert sorted(check({"name": 1, "tags": []}, schema)) == ["age: missing", "name: expected str"]
    # Deep Merge
    assert deep_merge({"x": 1, "cfg": {"a": 1, "b": 2}}, {"cfg": {"b": 3}, "y": 2}) == {"x": 1, "cfg": {"a": 1, "b": 3}, "y": 2}
    print("All tests passed!")
