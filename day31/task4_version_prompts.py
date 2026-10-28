"""
Day 31 · Task 4: Version prompts

Store prompts in files and test each on 5 inputs.

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

from pathlib import Path

PROMPTS = Path(__file__).parent / "prompts"     # create prompts/v1.txt and prompts/v2.txt
TEST_INPUTS = ["...", "...", "...", "...", "..."]

# TODO: for each prompt version, run all 5 inputs and save results to results.md as a table
