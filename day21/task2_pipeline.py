"""
Day 21 · Task 2: Pipeline

Use sklearn Pipeline + ColumnTransformer.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric = ["Age", "Fare", "FamilySize"]
categorical = ["Sex", "Pclass", "Embarked"]

preprocess = ColumnTransformer([
    ("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
    # TODO: ("cat", Pipeline([... SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")]), categorical),
])

model = Pipeline([("prep", preprocess), ("clf", LogisticRegression(max_iter=1000))])
# TODO: fit on the raw Titanic dataframe columns and print test accuracy
