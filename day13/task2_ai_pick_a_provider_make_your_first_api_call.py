"""
Day 13 · Task 2 · AI & ML: Pick a provider & make your first API call

Set up a free provider (Gemini free tier or Ollama locally) and send your first messages.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Pick a provider =====
# ## My provider
# - [ ] Chosen: Gemini free tier / Ollama / OpenAI / Claude
# - [ ] `.env` created with LLM_API_KEY, LLM_MODEL (and LLM_BASE_URL if needed)
# - [ ] `.env` is in `.gitignore`


# ===== Part 2: Messages and roles =====
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

messages = [
    {"role": "system", "content": "You are a friendly Python tutor. Keep answers under 80 words."},
    {"role": "user", "content": "What is a list comprehension?"},
]

# TODO: send messages, print response.choices[0].message.content
