"""
Day 56 · Task 1 · Engineering: Text-to-SQL safely

Let the LLM write SQL against a small SQLite DB, with read-only access.

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

import sqlite3

conn = sqlite3.connect("file:day56/company.db?mode=ro", uri=True)   # read-only!
SCHEMA = "\n".join(r[0] for r in conn.execute("SELECT sql FROM sqlite_master WHERE type='table'"))


def text_to_sql(question: str) -> str:
    # TODO: ask the model for ONE SQLite SELECT statement for the schema; return only the SQL
    pass


def run_sql(sql: str):
    # TODO: refuse anything that isn't a SELECT; run it; return rows
    pass
