"""
Day 51 · Task 3: Revise

Loop until the score passes or 3 rounds.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from task1_generate import generate
from task2_critique import critique


def reflect(task: str, target: int = 8, max_rounds: int = 3) -> str:
    draft = generate(task)
    for r in range(max_rounds):
        review = critique(task, draft)
        print(f"round {r}: score {review['score']}")
        # TODO: stop if score >= target; else revise using the feedback
    return draft
