"""
Day 52 · Task 2: Execute

Run each step with tools, store results.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from task1_plan import make_plan


def execute(goal: str) -> list[dict]:
    plan = make_plan(goal)
    results = []
    for i, step in enumerate(plan.steps):
        # TODO: run each step with your day 50 agent; store {"step": ..., "result": ...}
        pass
    return results
