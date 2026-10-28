"""
Day 32 · Task 3: Retry on failure

If validation fails, send the error back and retry up to 2 times.

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

from pydantic import BaseModel, ValidationError


class Invoice(BaseModel):
    invoice_id: str
    vendor: str
    date: str
    total: float


def extract_with_retry(text: str, max_retries: int = 2) -> Invoice:
    messages = [{"role": "user", "content": f"Extract the invoice as JSON with keys invoice_id, vendor, date, total.\n\n{text}"}]
    for attempt in range(max_retries + 1):
        # TODO: call the model, try Invoice.model_validate_json(reply)
        # TODO: on ValidationError, append the reply and a message with the error, then loop
        pass
    raise RuntimeError("Could not get valid JSON")
