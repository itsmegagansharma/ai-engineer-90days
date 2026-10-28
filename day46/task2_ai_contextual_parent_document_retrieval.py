"""
Day 46 · Task 2 · AI & ML: Contextual & parent-document retrieval

Prepend a short LLM-written context to each chunk before embedding. Then: Search small chunks, return their larger parent section.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Contextual retrieval =====
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

def add_context(full_document: str, chunk: str) -> str:
    # TODO: ask the model for 1-2 sentences situating the chunk within the document
    #       (see Anthropic's "Contextual Retrieval"); return context + "\n\n" + chunk
    pass

# TODO: re-ingest your docs with contextualized chunks and re-run your day 43 test questions


# ===== Part 2: Parent-document retrieval =====
# Parent-document retrieval:
#   - split each section into small chunks (~200 chars) for precise search
#   - store parent_id in metadata
#   - after search, return the full parent section (~1500 chars) to the LLM

parents: dict[str, str] = {}    # parent_id -> full section text

# TODO: build parents + small chunks; search small; dedupe by parent_id; return parent texts
