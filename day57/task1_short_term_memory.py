"""
Day 57 · Task 1: Short-term memory

Add a checkpointer and thread_id so the graph remembers a conversation.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# llm and tools from day 55
memory = MemorySaver()
# TODO: agent = create_react_agent(llm, tools, checkpointer=memory)
config = {"configurable": {"thread_id": "gagan-1"}}

# TODO: invoke "My name is Gagan" then "What's my name?" with the SAME config -> it remembers
# TODO: try a different thread_id -> it forgets
