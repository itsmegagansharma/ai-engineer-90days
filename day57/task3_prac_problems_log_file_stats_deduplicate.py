"""
Day 57 · Task 3 · Practice: Problems: Log File Stats & Deduplicate Records

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Log File Stats ----------------
def log_stats(lines: list[str]) -> dict[str, int]:
    """Lines look like "2026-11-02 10:01 ERROR timeout". Count lines per level (INFO/WARN/ERROR)."""
    pass


# ---------------- Deduplicate Records ----------------
def dedupe(records: list[dict], key: str) -> list[dict]:
    """Keep the first record for each value of `key`, preserving order. Data pipelines need this."""
    pass


if __name__ == "__main__":
    # Log File Stats
    logs = ["2026-11-02 10:01 ERROR timeout", "2026-11-02 10:02 INFO ok", "2026-11-02 10:03 ERROR boom"]
    assert log_stats(logs) == {"ERROR": 2, "INFO": 1}
    # Deduplicate Records
    rows = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}, {"id": 1, "v": "c"}]
    assert dedupe(rows, "id") == [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}]
    print("All tests passed!")
