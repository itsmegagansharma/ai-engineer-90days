"""
Day 39 · Task 1 · Engineering: Clean text with regex

Remove headers/footers, collapse whitespace, strip page numbers, fix hyphenated line breaks.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import re


def clean(text: str) -> str:
    # TODO 1: join words broken across lines: "infor-\nmation" -> "information"
    # TODO 2: remove lines that are only a page number
    # TODO 3: collapse 3+ newlines into 2, and runs of spaces into one
    pass


sample = "Page 1\n\nThe infor-\nmation   age\n\n\n\n2\nNext   part"
print(clean(sample))
