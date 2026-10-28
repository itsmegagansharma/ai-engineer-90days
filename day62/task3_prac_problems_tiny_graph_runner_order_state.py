"""
Day 62 · Task 3 · Practice: Problems: Tiny Graph Runner & Order State Machine

Solve both in the starter file, then run it: every assert must pass. Build the core of LangGraph yourself.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Tiny Graph Runner ----------------
def run_graph(nodes: dict, edges: dict, start: str, state: dict, max_steps: int = 20) -> dict:
    """nodes: name -> function(state) -> dict of updates.
    edges: name -> next name, or a function(state) -> next name, or "END".
    Run from start, merging updates into state, until END. This is LangGraph in 15 lines."""
    pass


# ---------------- Order State Machine ----------------
ALLOWED = {"draft": {"submitted"}, "submitted": {"approved", "rejected"}, "approved": {"shipped"}}


class Order:
    """Track status and reject illegal transitions (raise ValueError). Keep a history list.
    Agent workflows with approvals are state machines like this."""

    def __init__(self):
        pass

    def move(self, new_status: str) -> None:
        pass


if __name__ == "__main__":
    # Tiny Graph Runner
    nodes = {"inc": lambda s: {"n": s["n"] + 1}, "double": lambda s: {"n": s["n"] * 2}}
    edges = {"inc": lambda s: "double" if s["n"] < 5 else "END", "double": "inc"}
    assert run_graph(nodes, edges, "inc", {"n": 0})["n"] == 7
    # Order State Machine
    o = Order(); o.move("submitted"); o.move("approved")
    try:
        o.move("draft"); raise AssertionError("should fail")
    except ValueError:
        pass
    print("All tests passed!")
