"""
Day 65 · Task 1 · Engineering: Validation loops

Validate each output; on failure, send the error back.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# In LangGraph: a "validate" node checks the output; on failure it routes back to "generate"
# with the error added to state. Stop after 3 tries and route to a "give_up" node.
from typing import TypedDict


class State(TypedDict):
    task: str
    output: str
    error: str
    tries: int

# TODO: generate -> validate -> (ok: END | bad and tries<3: generate | else: give_up)
