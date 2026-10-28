"""
Day 58 · Task 1 · Engineering: Permissions & audit logging

Filter chunks by user role metadata; log every answer with its sources.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import json
from datetime import datetime

ROLE_ACCESS = {"employee": ["public"], "manager": ["public", "internal"], "hr": ["public", "internal", "hr"]}


def allowed_filter(role: str) -> dict:
    # TODO: return a Chroma where-filter so only chunks with metadata "level" in ROLE_ACCESS[role] come back
    pass


def audit(user: str, role: str, question: str, sources: list[str], answer: str) -> None:
    # TODO: append one JSON line to day56/audit.log with a timestamp
    pass
