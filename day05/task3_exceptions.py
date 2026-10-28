"""
Day 05 · Task 3: Exceptions

Wrap int(input()) in try/except ValueError. Use finally once. Raise your own ValueError for bad input.

Complete every TODO, run the file, and tick this task on the tracker.
"""
def ask_age() -> int:
    """Keep asking until the user types a valid whole number between 1 and 120."""
    while True:
        text = input("Your age: ")
        # TODO: try to convert with int(). On ValueError print "Please type a number" and continue.
        # TODO: if the number is outside 1..120, raise ValueError("age out of range") and catch it too.
        # TODO: return the age when it's valid.
        pass


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # TODO: return None and print a friendly message
        pass
    finally:
        print("safe_divide finished")   # notice: this always runs
