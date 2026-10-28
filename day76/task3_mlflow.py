"""
Day 76 · Task 3: MLflow

Track experiments and register a model.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install mlflow    Run the UI: mlflow ui
import mlflow

with mlflow.start_run(run_name="rag-hybrid-rerank"):
    mlflow.log_param("chunk_size", 800)
    mlflow.log_param("retriever", "hybrid+rerank")
    # TODO: log your day 46 eval scores with mlflow.log_metric(...)
