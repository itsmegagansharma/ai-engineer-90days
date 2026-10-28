"""
Day 44 · Task 2: Multi-query

Have the LLM write 3 versions of the question and merge results.

Complete every TODO, run the file, and tick this task on the tracker.
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

def multi_query(question: str, n: int = 3) -> list[str]:
    # TODO: ask the model for n different rephrasings, one per line; return them plus the original
    pass

# TODO: retrieve for each query, merge with reciprocal_rank_fusion
