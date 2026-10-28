"""
Day 09 · Task 2: Dunder methods

Add __repr__ and __eq__ so objects print nicely and compare.

Complete every TODO, run the file, and tick this task on the tracker.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: __repr__ so print(Point(1, 2)) shows Point(x=1, y=2)

    # TODO: __eq__ so Point(1, 2) == Point(1, 2) is True

    # TODO (stretch): __add__ so Point(1, 2) + Point(3, 4) == Point(4, 6)


print(Point(1, 2))
print(Point(1, 2) == Point(1, 2))
