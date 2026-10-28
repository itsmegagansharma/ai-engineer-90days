"""
Day 10 · Task 3 · Practice: Reading tracebacks

Break code on purpose and learn to read Python errors from the bottom up.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# Run each block one at a time (comment the others out), read the traceback, and write
# below it: (1) the error type, (2) the line that caused it, (3) the fix.

# 1
numbers = [1, 2, 3]
print(numbers[3])
# error type:
# line:
# fix:

# 2
user = {"name": "Gagan"}
print(user["age"])

# 3
total = "5" + 3

# 4
def greet(name):
    return "Hi " + name
greet()

# 5
import json
json.loads("{bad json}")
