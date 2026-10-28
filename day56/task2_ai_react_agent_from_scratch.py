"""
Day 56 · Task 2 · AI & ML: ReAct agent from scratch

Loop: model thinks → picks a tool → you run it → feed result back, until it answers. Then: Add a max-steps limit and handle tool errors.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: ReAct loop =====
# Uses an OpenAI-compatible client. Pick ONE provider and set it in .env:
#   Gemini (free tier):  LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/  LLM_API_KEY=...  LLM_MODEL=gemini-2.0-flash
#   Ollama (local, free): LLM_BASE_URL=http://localhost:11434/v1  LLM_API_KEY=ollama  LLM_MODEL=llama3.2
#   OpenAI:              LLM_API_KEY=sk-...  LLM_MODEL=gpt-4o-mini
# pip install openai python-dotenv
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url=os.getenv("LLM_BASE_URL") or None, api_key=os.getenv("LLM_API_KEY"))
MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

import json

# Three tools: calculator, search_notes (search your Chroma DB), get_time
TOOLS_SPEC = [...]   # TODO: JSON schemas (see day 33)
TOOLS = {}           # TODO: name -> function

SYSTEM = "You are a helpful agent. Think step by step. Use tools when needed. When done, answer the user."


def agent(task: str, max_steps: int = 8) -> str:
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": task}]
    for step in range(max_steps):
        # TODO: call model with tools; if no tool call -> return answer
        # TODO: otherwise run each tool, append results, print f"step {step}: {tool_name}"
        pass
    return "Stopped after max_steps"


# ===== Part 2: Stop conditions =====
# ## Stop conditions I added
# - max steps:
# - repeated identical tool call:
# - tool error handling:
#
# A task where the agent looped, and how I fixed it:
