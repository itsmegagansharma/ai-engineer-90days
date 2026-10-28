"""
Day 04 · Task 3: *args, **kwargs, scope

Write total(*nums). Print kwargs in a function to see how they arrive.

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
