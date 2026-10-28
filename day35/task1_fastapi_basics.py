"""
Day 35 · Task 1: FastAPI basics

Routes, path/query params, Pydantic request bodies, /docs page.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install fastapi uvicorn
# Run: uvicorn day35.task1_fastapi_basics:app --reload    then open http://127.0.0.1:8000/docs
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Day 35 API")


@app.get("/health")
def health():
    return {"status": "ok"}


class EchoIn(BaseModel):
    text: str
    times: int = 1


# TODO: POST /echo that returns {"result": text repeated `times` times}
# TODO: GET /items/{item_id}?q=... that returns both values
