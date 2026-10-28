"""
Day 70 · Task 3 · Practice: PII redaction

Solve the redaction exercise: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"(?:\+91[- ]?)?[6-9]\d{9}")


def redact(text: str) -> str:
    # TODO: replace emails with [EMAIL] and phone numbers with [PHONE]
    pass


assert redact("Mail a.b@x.com or call 9876543210") == "Mail [EMAIL] or call [PHONE]"
