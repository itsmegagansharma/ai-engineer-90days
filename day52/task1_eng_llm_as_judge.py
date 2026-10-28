"""
Day 52 · Task 1 · Engineering: LLM-as-judge

Use a model to grade answers against a rubric.

Complete every TODO, run the file, then tick this task on the tracker.
"""
JUDGE_PROMPT = """You grade an assistant's answer.
Question: {q}
Answer: {a}
Reference: {ref}
Score 1-5 for correctness and helpfulness. Reply as JSON: {{"score": n, "reason": "..."}}"""

# TODO: function judge(q, a, ref) -> dict using your LLM client; average scores over your test set
