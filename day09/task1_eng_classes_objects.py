"""
Day 09 · Task 1 · Engineering: Classes & objects

Write class BankAccount with __init__, deposit, withdraw, balance. Then: Add a class attribute interest_rate and see how instances share it. Then: Raise an error on withdraw if balance is too low.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Classes and objects =====
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


# ===== Part 2: Instance vs class attributes =====
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


# ===== Part 3: Encapsulation =====
class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance      # leading underscore = "internal, don't touch directly"

    def withdraw(self, amount):
        # TODO: raise InsufficientFunds if amount > balance, otherwise subtract
        pass

    @property
    def balance(self):
        return self._balance


# TODO: also write library.py with Book, Member and Library classes:
#   Library.add_book(book), Library.lend(book_title, member), Library.return_book(book_title)
