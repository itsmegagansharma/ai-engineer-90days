"""
Day 35 · Task 2 · AI & ML: Association rules & recommender evaluation

pip install mlxtend; run apriori on a basket dataset and read support/confidence/lift. Then: Hold out ratings and compute precision@10.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Association rules =====
# pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

baskets = [
    ["bread", "milk"], ["bread", "butter", "milk"], ["tea", "biscuits"],
    ["bread", "butter"], ["milk", "tea", "biscuits"], ["bread", "milk", "butter"],
]

te = TransactionEncoder()
df = pd.DataFrame(te.fit_transform(baskets), columns=te.columns_)

# TODO: frequent = apriori(df, min_support=0.3, use_colnames=True)
# TODO: rules = association_rules(frequent, metric="lift", min_threshold=1.0)
# TODO: print antecedents, consequents, support, confidence, lift. Explain one rule in words.


# ===== Part 2: Evaluate =====
# Hold out 20% of each user's ratings, recommend 10 movies, and check how many
# of the held-out highly-rated movies (rating >= 4) appear in the 10.

def precision_at_k(recommended: list[int], relevant: set[int], k: int = 10) -> float:
    # TODO
    pass
