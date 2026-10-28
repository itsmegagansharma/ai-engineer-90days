"""
Day 70 · Task 2 · AI & ML: Deterministic rules + LLM judgment

Put fixed business rules in plain code and let the LLM handle only judgment steps.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# Deterministic rules in plain code, LLM only for judgment.
REFUND_LIMIT = 5000


def decide_refund(order: dict, customer_message: str) -> dict:
    # Rule 1 (code): orders older than 30 days -> reject, no LLM call
    # Rule 2 (code): amount > REFUND_LIMIT -> needs human approval
    # Judgment (LLM): is the complaint about a product defect? -> classify
    # TODO: implement and return {"decision": ..., "reason": ..., "needs_human": bool}
    pass
