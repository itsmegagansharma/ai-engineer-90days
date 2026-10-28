"""
Day 67 · Task 2 · AI & ML: Supervisor with specialist agents

A supervisor node routes to research, writer and reviewer agents.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# Supervisor routes to: researcher, writer, reviewer, or FINISH
from typing import Literal

from langgraph.graph import MessagesState

AGENTS = ["researcher", "writer", "reviewer"]


class State(MessagesState):
    next: str


def supervisor(state: State) -> dict:
    # TODO: ask the LLM (structured output) which agent should act next, or "FINISH"
    pass

# TODO: one node per agent; each returns to supervisor; conditional edge from supervisor on state["next"]
