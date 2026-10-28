"""
Day 16 · Task 2 · AI & ML: Chatbot with history & cost tracking

Read usage tokens from the response and estimate cost.

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

PRICE_PER_M_INPUT = 0.15     # USD per million tokens - check your provider's pricing
PRICE_PER_M_OUTPUT = 0.60

history = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user = input("you> ")
    if user in {"quit", "exit"}:
        break
    history.append({"role": "user", "content": user})
    # TODO: call the model with the full history, print the reply, append it as "assistant"
    # TODO: read response.usage.prompt_tokens / completion_tokens and print the cost of this turn
