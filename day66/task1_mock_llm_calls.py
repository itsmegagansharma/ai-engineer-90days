"""
Day 66 · Task 1: Mock LLM calls

Unit-test your graph with a fake model.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Test graph logic without calling a real LLM.
from unittest.mock import patch


def test_classifier_routes_math():
    with patch("myapp.llm_call", return_value="math"):
        # TODO: run your graph's classify node; assert state["kind"] == "math"
        pass
