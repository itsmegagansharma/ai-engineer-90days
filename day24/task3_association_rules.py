"""
Day 24 · Task 3: Association rules

pip install mlxtend; run apriori on a basket dataset and read support/confidence/lift.

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
