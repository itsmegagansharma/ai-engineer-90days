"""
Day 34 · Task 2 · AI & ML: Recommender systems

Recommend movies by genre/description similarity (TF-IDF + cosine). Then: User-item matrix, user-user similarity on MovieLens small.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Content-based =====
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# MovieLens small: movies.csv -> day34/movies.csv
movies = pd.read_csv("day34/movies.csv")
movies["genres"] = movies["genres"].str.replace("|", " ")

# TODO: tfidf matrix of genres, cosine similarity, and a function:
def recommend(title: str, n: int = 5) -> list[str]:
    pass


# ===== Part 2: Collaborative filtering =====
import pandas as pd

ratings = pd.read_csv("day34/ratings.csv")
matrix = ratings.pivot_table(index="userId", columns="movieId", values="rating")

# TODO 1: fill NaN with 0 and compute user-user cosine similarity
# TODO 2: for user 1, find the 5 most similar users
# TODO 3: recommend movies those users rated highly that user 1 hasn't seen
