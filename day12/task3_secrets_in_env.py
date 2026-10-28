"""
Day 12 · Task 3: Secrets in .env

pip install python-dotenv. Load API_KEY from .env and add .env to .gitignore.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install python-dotenv
# 1. Create a file named .env in the repo root containing:  MY_API_KEY=test-123
# 2. Make sure .env is listed in .gitignore
import os
from dotenv import load_dotenv

load_dotenv()

# TODO: read MY_API_KEY with os.getenv and print only its first 4 characters
#       (never print full secrets)
