"""
Day 32 · Task 2: Parse to Pydantic

Validate output with a Pydantic model.

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

import json
from pydantic import BaseModel


class Invoice(BaseModel):
    invoice_id: str
    vendor: str
    date: str
    total: float


def extract(text: str) -> Invoice:
    # TODO: ask for JSON matching Invoice.model_json_schema(); parse with Invoice.model_validate_json(...)
    pass
