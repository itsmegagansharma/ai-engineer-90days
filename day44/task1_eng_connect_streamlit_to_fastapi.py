"""
Day 44 · Task 1 · Engineering: Connect Streamlit to FastAPI

Streamlit calls your FastAPI backend.

Complete every TODO, run the file, then tick this task on the tracker.
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
