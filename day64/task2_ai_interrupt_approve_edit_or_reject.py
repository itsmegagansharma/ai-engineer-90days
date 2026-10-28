"""
Day 64 · Task 2 · AI & ML: Interrupt, approve, edit or reject

Pause the graph before a risky tool call. Then: Resume with the human's decision.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: interrupt() =====
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


# ===== Part 2: Approve / edit / reject =====
# TODO: extend approval so the human can answer:
#   "yes"                       -> send as is
#   "no"                        -> stop
#   {"edit": "new email text"}  -> replace the draft, then send
