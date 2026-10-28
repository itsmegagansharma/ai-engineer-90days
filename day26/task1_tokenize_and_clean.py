"""
Day 26 · Task 1: Tokenize and clean

Lowercase, remove stopwords, n-grams with CountVectorizer.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "Agents use tools to complete tasks",
    "RAG retrieves documents before answering",
    "Agents can retrieve documents with tools",
]

# TODO 1: CountVectorizer(stop_words="english"); print get_feature_names_out() and the matrix
# TODO 2: try ngram_range=(1, 2) and see the bigrams appear
