"""
Day 29 · Task 2 · AI & ML: Context window management

Count tokens before each call; keep under a limit. Then: When history passes the limit, summarize old turns into one message.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Token budgeting =====
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
MAX_TOKENS = 1000


def count_tokens(messages: list[dict]) -> int:
    # TODO: sum len(enc.encode(m["content"])) + 4 per message
    pass


def trim(messages: list[dict]) -> list[dict]:
    # TODO: keep the system message, drop the oldest user/assistant messages until under MAX_TOKENS
    pass


# ===== Part 2: Summarize history =====
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

def summarize_history(old_messages: list[dict]) -> dict:
    # TODO: ask the model to summarize the conversation in under 100 words
    # TODO: return {"role": "system", "content": "Summary of earlier conversation: ..."}
    pass

# TODO: in your chat loop, when history > 1000 tokens, replace everything except the
#       system prompt and the last 4 messages with one summary message
