"""
Day 34 · Task 1 · Engineering: Config with pydantic-settings

Load settings (model name, API key, DB URL) from env vars and .env with validation.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# pip install pydantic-settings
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    llm_model: str = "gpt-4o-mini"
    llm_api_key: str = Field(default="", repr=False)   # repr=False keeps secrets out of logs
    database_url: str = "sqlite:///app.db"
    debug: bool = False


settings = Settings()
# TODO: print(settings) and confirm the key is hidden
# TODO: run with LLM_MODEL=llama3.2 in the environment and see it override the default
