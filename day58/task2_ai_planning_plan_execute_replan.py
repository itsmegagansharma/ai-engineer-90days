"""
Day 58 · Task 2 · AI & ML: Planning: plan, execute, replan

Ask the model to output a numbered plan as JSON. Then: Run each step with tools, store results. Then: If a step fails, send the failure back and ask for a new plan.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Plan =====
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

from pydantic import BaseModel


class Plan(BaseModel):
    steps: list[str]


def make_plan(goal: str) -> Plan:
    # TODO: ask for a numbered plan as JSON {"steps": [...]}, validate with Plan
    pass


# ===== Part 2: Execute =====
def execute(goal: str) -> list[dict]:
    plan = make_plan(goal)
    results = []
    for i, step in enumerate(plan.steps):
        # TODO: run each step with your day 50 agent; store {"step": ..., "result": ...}
        pass
    return results


# ===== Part 3: Replan =====
# TODO: if a step's result contains "Error" or the agent gives up,
#       call make_plan again with the goal + what has been done + what failed,
#       and continue from the new plan. Limit to 2 replans.
