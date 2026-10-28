"""
Day 02 · Task 1 · Engineering: Variables, numbers, strings, input/print

Write a script that asks your name and birth year with input(), converts the year with int(), and prints your age with an f-string.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# Goal: ask for your name and birth year, then print your age.
# Run: python day01/task3_variables.py

CURRENT_YEAR = 2026

name = input("What's your name? ")
birth_year_text = input("Which year were you born? ")

# TODO 1: convert birth_year_text to an int and store it in birth_year
birth_year = ...

# TODO 2: calculate age
age = ...

# TODO 3: print a message like "Hi Gagan, you are 25 years old."
#         using an f-string: f"Hi {name}, ..."


# Stretch: also print how many days old you are (roughly age * 365).
