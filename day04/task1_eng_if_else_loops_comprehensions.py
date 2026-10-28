"""
Day 04 · Task 1 · Engineering: if/else, loops & comprehensions

Grade calculator, a guessing game, then rewrite loops as comprehensions.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: if / elif / else =====
def grade(score: int) -> str:
    """Return A (90+), B (75+), C (60+), D (40+) or F."""
    # TODO: use if / elif / else
    pass


if __name__ == "__main__":
    for s in [95, 80, 61, 45, 10]:
        print(s, grade(s))   # expected: A B C D F


# ===== Part 2: for and while loops =====
import random

secret = random.randint(1, 20)
tries = 0

# TODO: loop with while until the user guesses the secret
#  - read a guess with input() and convert to int
#  - add 1 to tries
#  - print "Too high" / "Too low"
#  - when correct, print "Got it in N tries!" and break


# ===== Part 3: Comprehensions =====
nums = list(range(1, 21))

# Rewrite each loop as a ONE-LINE comprehension below it.

squares = []
for n in nums:
    squares.append(n * n)
# TODO: squares2 = [...]

evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
# TODO: evens2 = [...]

lengths = {}
for word in ["agent", "rag", "embedding"]:
    lengths[word] = len(word)
# TODO: lengths2 = {...}

# TODO: print all three and check they match the loop versions
