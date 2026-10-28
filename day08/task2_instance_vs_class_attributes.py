"""
Day 08 · Task 2: Instance vs class attributes

Add a class attribute interest_rate and see how instances share it.

Complete every TODO, run the file, and tick this task on the tracker.
"""
class BankAccount:
    interest_rate = 0.04   # class attribute: shared by every account

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


a = BankAccount("A")
b = BankAccount("B")

# TODO 1: print a.interest_rate and b.interest_rate
# TODO 2: change BankAccount.interest_rate = 0.05 and print both again
# TODO 3: set a.interest_rate = 0.10 (only on a). Print both. Explain the difference in a comment.
