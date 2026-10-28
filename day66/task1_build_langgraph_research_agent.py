"""
Day 66 · Task 1 · Build: LangGraph research agent

Agent that searches, summarizes and reflects on its answer.

Complete every TODO, run the file, then tick this task on the tracker.
"""
"""Research agent: search -> summarize -> reflect.
Tools: a web or notes search tool, a summarizer node, and a reflection node that
checks the summary answers the question and loops back if not (max 2 loops)."""
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class ResearchState(TypedDict):
    question: str
    findings: list[str]
    summary: str
    critique: str
    loops: int

# TODO: nodes search, summarize, reflect; conditional edge from reflect -> search or END
