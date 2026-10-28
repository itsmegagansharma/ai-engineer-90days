"""
Day 25 · Task 1: Content-based

Recommend movies by genre/description similarity (TF-IDF + cosine).

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# MovieLens small: movies.csv -> day25/movies.csv
movies = pd.read_csv("day25/movies.csv")
movies["genres"] = movies["genres"].str.replace("|", " ")

# TODO: tfidf matrix of genres, cosine similarity, and a function:
def recommend(title: str, n: int = 5) -> list[str]:
    pass
