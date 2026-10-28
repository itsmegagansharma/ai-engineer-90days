"""
Day 25 · Task 2 · AI & ML: Structured outputs: JSON mode

Ask the model for JSON matching a schema.

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

text = "Invoice INV-204 from Sharma Traders, dated 3 Oct 2026, total Rs 4,720 incl. GST."

# TODO: ask for JSON with keys invoice_id, vendor, date (YYYY-MM-DD), total (number)
#       use response_format={"type": "json_object"} and mention JSON in the prompt
#       then json.loads the reply
