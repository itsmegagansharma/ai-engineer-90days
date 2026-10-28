"""
Day 75 · Task 2: Config switch

Make your app switch between cloud and local model via env var.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import os

from openai import OpenAI

PROVIDERS = {
    "cloud": {"base_url": None, "api_key": os.getenv("LLM_API_KEY"), "model": "gpt-4o-mini"},
    "local": {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "llama3.2"},
}


def get_client() -> tuple[OpenAI, str]:
    # TODO: read LLM_MODE env var ("cloud" or "local"), return (OpenAI client, model name)
    pass
