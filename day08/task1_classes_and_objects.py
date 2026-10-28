"""
Day 08 · Task 1: Classes and objects

Write class BankAccount with __init__, deposit, withdraw, balance.

Complete every TODO, run the file, and tick this task on the tracker.
"""
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        # TODO: store owner and balance on self
        pass

    def deposit(self, amount: float) -> None:
        # TODO
        pass

    def withdraw(self, amount: float) -> None:
        # TODO
        pass

    def get_balance(self) -> float:
        # TODO
        pass


if __name__ == "__main__":
    acc = BankAccount("Gagan", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())   # 1300
