"""
Day 62 · Task 1 · Engineering: Conditional edges

Route to different nodes based on state.

Complete every TODO, run the file, then tick this task on the tracker.
"""
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    question: str
    kind: str
    answer: str


def classify(state: State) -> dict:
    # TODO: set kind to "math", "code" or "general" (use the LLM, or simple rules first)
    pass


def route(state: State) -> Literal["math", "code", "general"]:
    return state["kind"]

# TODO: add math, code and general nodes; add_conditional_edges("classify", route); compile; test 3 questions
