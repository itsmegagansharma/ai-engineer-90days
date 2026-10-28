"""
Day 69 · Task 2: PII redaction

Detect and mask emails/phone numbers before sending to the LLM.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"(?:\+91[- ]?)?[6-9]\d{9}")


def redact(text: str) -> str:
    # TODO: replace emails with [EMAIL] and phone numbers with [PHONE]
    pass


assert redact("Mail a.b@x.com or call 9876543210") == "Mail [EMAIL] or call [PHONE]"
