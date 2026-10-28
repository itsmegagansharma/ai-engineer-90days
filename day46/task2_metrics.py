"""
Day 46 · Task 2: Metrics

Faithfulness, answer relevance, context recall with RAGAS.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install ragas datasets
import json

testset = json.load(open("day46/testset.json"))

rows = []
for item in testset:
    # TODO: run your RAG; collect question, answer, contexts (list of chunk texts), ground_truth
    pass

# TODO: evaluate with ragas metrics: faithfulness, answer_relevancy, context_recall
#       (check the RAGAS docs for the current API; it changes between versions)
