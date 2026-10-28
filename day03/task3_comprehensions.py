"""
Day 03 · Task 3: Comprehensions

Rewrite 3 loops as list or dict comprehensions, e.g. [x*x for x in nums if x%2==0].

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
