"""
Day 03 · Task 1 · Engineering: Lists, tuples, dicts & sets

Work through lists/tuples, then dictionaries, then sets in one file.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Lists and tuples =====
# Lists and tuples practice. Run each TODO, print the result.

nums = [42, 7, 19, 3, 88, 21]

# TODO 1: print the first and last item (use index 0 and -1)

# TODO 2: print items 2 to 4 using slicing -> [19, 3, 88]

# TODO 3: print the list reversed using slicing [::-1]

# TODO 4: append 100, then sort the list, then print it

point = (3, 4)
# TODO 5: try point[0] = 10 and read the error. Then explain in a comment why tuples can't change.


# ===== Part 2: Dictionaries =====
friends = {"Asha": 24, "Ravi": 27}

# TODO 1: add 3 more friends with their ages

# TODO 2: loop with .items() and print "Asha is 24" for each friend

# TODO 3: use .get() to look up someone who doesn't exist, with a default of "unknown"

# TODO 4: delete one friend with del, then print the dict

# TODO 5: print the name of the oldest friend (hint: max(friends, key=friends.get))


# ===== Part 3: Sets =====
python_learners = {"asha", "ravi", "neha", "arjun"}
ml_learners = {"neha", "arjun", "sara"}

# TODO 1: who is learning both?      (intersection: &)
# TODO 2: everyone in either group   (union: |)
# TODO 3: Python only                (difference: -)

emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
# TODO 4: remove duplicates using a set and print how many unique emails there are
