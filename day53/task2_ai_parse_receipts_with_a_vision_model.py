"""
Day 53 · Task 2 · AI & ML: Parse receipts with a vision model

Extract a table from a scanned invoice into JSON.

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

from pydantic import BaseModel


class LineItem(BaseModel):
    description: str
    quantity: float
    amount: float


class Receipt(BaseModel):
    store: str
    date: str
    items: list[LineItem]
    total: float


# TODO: send a receipt photo + the Receipt JSON schema; validate the reply with Receipt
# TODO: check sum(item.amount) is close to total; flag if not
