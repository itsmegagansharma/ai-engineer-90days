"""
Day 58 · Task 1: interrupt()

Pause the graph before a risky tool call.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from typing import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class State(TypedDict):
    draft_email: str
    approved: bool


def draft(state: State) -> dict:
    return {"draft_email": "Hi team, the report is ready."}


def approval(state: State) -> dict:
    decision = interrupt({"question": "Send this email?", "email": state["draft_email"]})
    # TODO: return {"approved": decision == "yes"}
    pass


def send(state: State) -> dict:
    # TODO: print "SENT" only if approved
    pass

# TODO: build draft -> approval -> send, compile with MemorySaver, invoke, then resume with Command(resume="yes")
