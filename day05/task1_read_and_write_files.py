"""
Day 05 · Task 1: Read and write files

Use with open('notes.txt','a') as f: to append, and 'r' to read.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Append a line to a file, then read it back.

def add_line(path: str, text: str) -> None:
    # TODO: open the file in "a" mode with `with open(...) as f:` and write text + "\n"
    pass


def read_lines(path: str) -> list[str]:
    # TODO: open in "r" mode and return f.read().splitlines()
    pass


if __name__ == "__main__":
    add_line("day05/log.txt", "learned file handling")
    print(read_lines("day05/log.txt"))
