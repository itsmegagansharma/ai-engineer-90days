"""
Day 37 · Task 2 · AI & ML: Tokens, n-grams & TF-IDF

Lowercase, remove stopwords, n-grams with CountVectorizer. Then: TfidfVectorizer and see which words score highest.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Tokenize and clean =====
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "Agents use tools to complete tasks",
    "RAG retrieves documents before answering",
    "Agents can retrieve documents with tools",
]

# TODO 1: CountVectorizer(stop_words="english"); print get_feature_names_out() and the matrix
# TODO 2: try ngram_range=(1, 2) and see the bigrams appear


# ===== Part 2: TF-IDF =====
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [...]  # reuse task1 docs, or 10 sentences of your own

# TODO: fit TfidfVectorizer, then for each document print its top 3 words by TF-IDF score
