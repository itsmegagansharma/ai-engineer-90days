"""
Day 86 · Task 3: Python questions

GIL, generators, decorators, mutable defaults.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Predict the output BEFORE running each block, then run it.

def add_item(item, items=[]):     # mutable default!
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))      # surprised? fix it with items=None

def gen():
    yield 1
    yield 2

g = gen()
print(next(g), next(g))

def shout(fn):
    def wrapper(*a, **kw):
        return fn(*a, **kw).upper()
    return wrapper

@shout
def greet(name):
    return f"hi {name}"

print(greet("gagan"))

# TODO: write 2 lines on what the GIL is and when it matters
