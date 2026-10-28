"""
Day 03 · Task 2: for and while loops

Loop over a list, use range(), break and continue. Write a number-guessing game with while.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import random

secret = random.randint(1, 20)
tries = 0

# TODO: loop with while until the user guesses the secret
#  - read a guess with input() and convert to int
#  - add 1 to tries
#  - print "Too high" / "Too low"
#  - when correct, print "Got it in N tries!" and break
