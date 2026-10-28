"""
Day 33 · Task 2: Tool loop

Model asks for a tool → you run it → send result back → model answers.

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
from task1_define_tools import tools, calculator, get_weather

TOOLS = {"calculator": calculator, "get_weather": get_weather}


def run(question: str) -> str:
    messages = [{"role": "user", "content": question}]
    for _ in range(5):                                  # safety limit
        resp = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
        msg = resp.choices[0].message
        if not msg.tool_calls:
            return msg.content
        messages.append(msg)
        for call in msg.tool_calls:
            # TODO: look up TOOLS[call.function.name], run it with json.loads(call.function.arguments)
            # TODO: append {"role": "tool", "tool_call_id": call.id, "content": result}
            pass
    return "Stopped: too many steps"


print(run("What's 17% of 2350, and is it hot in Nashik today?"))
