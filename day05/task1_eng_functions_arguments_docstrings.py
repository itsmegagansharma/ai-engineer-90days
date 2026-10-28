"""
Day 05 · Task 1 · Engineering: Functions, arguments & docstrings

Calculator functions, default/keyword arguments, *args/**kwargs and docstrings.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: def, parameters, return =====
def add(a, b):
    return a + b

# TODO: write subtract, multiply and divide the same way.
# divide should return None (not crash) when b is 0.


if __name__ == "__main__":
    print(add(2, 3))          # 5
    # print(subtract(5, 2))   # 3
    # print(multiply(4, 3))   # 12
    # print(divide(10, 4))    # 2.5
    # print(divide(1, 0))     # None


# ===== Part 2: Default and keyword arguments =====
def divide(a, b, round_to=2):
    """Divide a by b and round the result."""
    # TODO: return round(a / b, round_to)
    pass


# TODO: call it three ways and print each:
#   divide(10, 3)
#   divide(10, 3, 4)
#   divide(b=3, a=10, round_to=1)   <- keyword arguments


# ===== Part 3: *args, **kwargs, scope =====
def total(*nums):
    # TODO: return the sum of all numbers passed in
    pass


def describe(**info):
    # TODO: print each key and value on its own line
    pass


counter = 0

def increment():
    # TODO: this fails without `global counter`. Run it, read the error, then fix it.
    counter = counter + 1


print(total(1, 2, 3, 4))          # 10
describe(name="Gagan", goal="AI Engineer")


# ===== Part 4: Docstrings =====
# Add a one-line docstring to every function.
# LLM "tools" use the same idea: a name, a description, and typed parameters.

def celsius_to_f(c):
    return c * 9 / 5 + 32

def is_even(n):
    return n % 2 == 0

def initials(full_name):
    return "".join(part[0].upper() for part in full_name.split())

# TODO: add docstrings, then run help(celsius_to_f) and see your text appear
