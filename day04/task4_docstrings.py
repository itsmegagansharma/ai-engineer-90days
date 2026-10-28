"""
Day 04 · Task 4: Docstrings

Add a one-line docstring to each function. LLM tool descriptions work the same way.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Add a one-line docstring to every function.
# LLM "tools" use the same idea: a name, a description, and typed parameters.

def celsius_to_f(c):
    return c * 9 / 5 + 32

def is_even(n):
    return n % 2 == 0

def initials(full_name):
    return "".join(part[0].upper() for part in full_name.split())

# TODO: add docstrings, then run help(celsius_to_f) and see your text appear
