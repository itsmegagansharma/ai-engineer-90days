"""
Day 07 · Task 1 · Engineering: Files, JSON & exceptions

Use with open('notes.txt','a') as f: to append, and 'r' to read. Then: json.dump a list of dicts to a file, json.load it back. Then: Wrap int(input()) in try/except ValueError. Use finally once. Raise your own ValueError for bad input.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Read and write files =====
# Append a line to a file, then read it back.

def add_line(path: str, text: str) -> None:
    # TODO: open the file in "a" mode with `with open(...) as f:` and write text + "\n"
    pass


def read_lines(path: str) -> list[str]:
    # TODO: open in "r" mode and return f.read().splitlines()
    pass


if __name__ == "__main__":
    add_line("day07/log.txt", "learned file handling")
    print(read_lines("day07/log.txt"))


# ===== Part 2: JSON =====
import json

notes = [
    {"id": 1, "text": "buy milk", "done": False},
    {"id": 2, "text": "finish day 5", "done": True},
]

# TODO 1: save notes to day07/notes.json with json.dump (use indent=2)

# TODO 2: load it back with json.load into loaded_notes

# TODO 3: print only the notes that are not done


# ===== Part 3: Exceptions =====
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
