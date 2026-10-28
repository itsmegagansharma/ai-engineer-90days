"""
Day 17 · Task 2 · AI & ML: System prompts & few-shot in code

Give a role, rules and output format. Then: Add 2–3 examples and compare outputs. Then: Wrap documents in XML tags; ask for reasoning before the answer.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: System prompts =====
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

SYSTEM = """You are ____.
Rules:
- ____
- ____
Output format: ____"""
# TODO: fill in a system prompt for "customer support for an online cleaning-products store".
# TODO: send 3 different customer questions and check the rules are followed.


# ===== Part 2: Few-shot =====
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

examples = """Review: "Arrived broken, very disappointed" -> negative
Review: "Works great, fast delivery" -> positive
"""

reviews = ["Smells nice but leaks", "Best purchase this year", "Okay I guess"]

# TODO: classify each review zero-shot (no examples), then few-shot (with examples). Compare.


# ===== Part 3: Structure inputs =====
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

document = """(paste a short article or policy here)"""

prompt = f"""<document>
{document}
</document>

Answer the question using only the document.
First write your reasoning inside <thinking> tags, then the answer inside <answer> tags.
Question: ____"""

# TODO: send it and extract only the text inside <answer> ... </answer>
