"""
Day 76 · Task 1 · Engineering: Local models & a provider switch

Run a model with Ollama; skim vLLM for serving at scale. Then: Make your app switch between cloud and local model via env var.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Local models =====
# ## Local models
# ```
# ollama pull llama3.2
# ollama run llama3.2 "hello"
# ```
# - Speed on my machine (tokens/s):
# - vLLM: when you'd use it instead of Ollama:


# ===== Part 2: Config switch =====
import os

from openai import OpenAI

PROVIDERS = {
    "cloud": {"base_url": None, "api_key": os.getenv("LLM_API_KEY"), "model": "gpt-4o-mini"},
    "local": {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "llama3.2"},
}


def get_client() -> tuple[OpenAI, str]:
    # TODO: read LLM_MODE env var ("cloud" or "local"), return (OpenAI client, model name)
    pass
