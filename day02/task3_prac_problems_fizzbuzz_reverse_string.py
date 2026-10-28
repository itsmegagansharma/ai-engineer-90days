"""
Day 02 · Task 3 · Practice: Problems: FizzBuzz & Reverse String

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- FizzBuzz ----------------
def fizzbuzz(n: int) -> list[str]:
    """Return "1".."n" but "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both."""
    pass


# ---------------- Reverse String ----------------
def reverse_string(s: str) -> str:
    """Return s reversed. Try it once with slicing and once with a loop."""
    pass


if __name__ == "__main__":
    # FizzBuzz
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    # Reverse String
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
    print("All tests passed!")
