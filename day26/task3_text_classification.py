"""
Day 26 · Task 3: Text classification

Train a spam classifier with TF-IDF + LogisticRegression.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# Kaggle "SMS Spam Collection" -> day26/spam.csv  (columns: label, text)
df = pd.read_csv("day26/spam.csv", encoding="latin-1")

# TODO: split, build make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000)), fit
# TODO: print classification_report; then test on 3 messages you write yourself
