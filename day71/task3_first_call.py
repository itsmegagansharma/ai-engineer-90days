"""
Day 71 · Task 3: First call

Call a model deployed on Azure from Python.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install openai
# Azure OpenAI uses the same SDK with the Azure client.
import os

from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-10-21",   # check the current version in the Azure docs
)

# TODO: client.chat.completions.create(model=<your deployment name>, messages=[...]); print the reply
