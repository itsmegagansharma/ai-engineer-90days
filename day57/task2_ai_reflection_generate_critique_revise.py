"""
Day 57 · Task 2 · AI & ML: Reflection: generate, critique, revise

Have the model write a draft (e.g. an email or code). Then: A second call scores the draft against a rubric. Then: Loop until the score passes or 3 rounds.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Generate =====
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

def generate(task: str) -> str:
    # TODO: write a first draft (e.g. a cold email or a Python function)
    pass


# ===== Part 2: Critique =====
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

RUBRIC = """Score 1-10 on: clarity, correctness, tone. Return JSON: {"score": n, "feedback": "..."}"""


def critique(task: str, draft: str) -> dict:
    # TODO: ask the model to grade the draft with RUBRIC; json.loads the reply
    pass


# ===== Part 3: Revise =====
def reflect(task: str, target: int = 8, max_rounds: int = 3) -> str:
    draft = generate(task)
    for r in range(max_rounds):
        review = critique(task, draft)
        print(f"round {r}: score {review['score']}")
        # TODO: stop if score >= target; else revise using the feedback
    return draft
