"""
Day 61 · Task 1 · Engineering: LangGraph: StateGraph, nodes & edges

Define a TypedDict state, add nodes, edges, compile, invoke.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# pip install langgraph
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    question: str
    answer: str


def answer_node(state: State) -> dict:
    # TODO: return {"answer": f"You asked: {state['question']}"}
    pass


graph = StateGraph(State)
graph.add_node("answer", answer_node)
graph.add_edge(START, "answer")
graph.add_edge("answer", END)
app = graph.compile()

print(app.invoke({"question": "What is LangGraph?"}))
