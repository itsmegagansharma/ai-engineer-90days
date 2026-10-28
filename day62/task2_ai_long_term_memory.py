"""
Day 62 · Task 2 · AI & ML: Long-term memory

Use a store (or vector DB) to save user facts across threads.

Complete every TODO, run the file, then tick this task on the tracker.
"""
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
namespace = ("user", "gagan")

# TODO: store.put(namespace, "profile", {"likes": "Python", "goal": "AI engineer"})
# TODO: in your agent node, read store.search(namespace) and add the facts to the system prompt
# TODO: add a "remember" tool the agent can call to save a new fact
