"""
Day 42 · Task 1 · Build: RAG from scratch with citations

Return the answer plus file + page references.

Complete every TODO, run the file, then tick this task on the tracker.
"""
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

from task2_ai_rag_retrieve_augment import retrieve  # from day 41: copy task2_ai_rag_retrieve_augment.py from day41/ into this folder
from task2_ai_rag_retrieve_augment import build_prompt  # from day 41: copy task2_ai_rag_retrieve_augment.py from day41/ into this folder


def answer(question: str) -> str:
    # TODO: retrieve -> build_prompt -> call model -> return answer
    pass


if __name__ == "__main__":
    while (q := input("question> ")) not in {"quit", ""}:
        print(answer(q), "\n")
