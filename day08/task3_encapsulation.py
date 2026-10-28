"""
Day 08 · Task 3: Encapsulation

Raise an error on withdraw if balance is too low.

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
