"""
Day 09 · Task 1: Inheritance and super()

SavingsAccount(BankAccount) adds interest. Call super().__init__.

Complete every TODO, run the file, and tick this task on the tracker.
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.04):
        # TODO: call super().__init__(owner, balance), then store rate
        pass

    def add_interest(self) -> None:
        # TODO: increase balance by balance * rate
        pass


s = SavingsAccount("Gagan", 1000)
s.add_interest()
print(s.balance)   # 1040.0
