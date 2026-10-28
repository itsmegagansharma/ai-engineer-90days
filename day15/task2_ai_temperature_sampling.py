"""
Day 15 · Task 2 · AI & ML: Temperature & sampling

Temperature, top-p: what changes when you raise them.

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

prompt = "Give me a name for a coffee shop run by robots."

for temperature in [0.0, 0.7, 1.5]:
    # TODO: call client.chat.completions.create(model=MODEL, temperature=temperature,
    #        messages=[{"role": "user", "content": prompt}]) 3 times and print each answer
    pass
# Comment: what changes as temperature goes up?
