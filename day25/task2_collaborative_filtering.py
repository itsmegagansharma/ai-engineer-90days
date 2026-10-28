"""
Day 25 · Task 2: Collaborative filtering

User-item matrix, user-user similarity on MovieLens small.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd

ratings = pd.read_csv("day25/ratings.csv")
matrix = ratings.pivot_table(index="userId", columns="movieId", values="rating")

# TODO 1: fill NaN with 0 and compute user-user cosine similarity
# TODO 2: for user 1, find the 5 most similar users
# TODO 3: recommend movies those users rated highly that user 1 hasn't seen
