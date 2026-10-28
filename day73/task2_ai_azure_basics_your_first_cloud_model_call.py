"""
Day 73 · Task 2 · AI & ML: Azure basics & your first cloud model call

Create a free Azure account; learn subscriptions, resource groups, IAM. Then: Explore Azure AI Foundry and Azure OpenAI models. Then: Call a model deployed on Azure from Python.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Account =====
# ## Azure basics
# - Subscription:
# - Resource group created:
# - What is IAM / RBAC (one line):


# ===== Part 2: AI services =====
# ## Azure AI Foundry
# - Models available to me:
# - Model deployed (name + region):


# ===== Part 3: First call =====
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
