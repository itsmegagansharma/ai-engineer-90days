"""
Day 42 · Task 2: Connect to API

Streamlit calls your FastAPI backend.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI(title="Docs RAG API")


class AskIn(BaseModel):
    question: str


@app.post("/ingest")
async def ingest(files: list[UploadFile]):
    # TODO: save files, run your day 38 ingestion, return how many chunks were added
    pass


@app.post("/ask")
def ask(body: AskIn):
    # TODO: run your day 39 answer(); return {"answer": ..., "sources": [...]}
    pass
