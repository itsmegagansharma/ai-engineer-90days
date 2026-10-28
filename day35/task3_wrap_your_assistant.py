"""
Day 35 · Task 3: Wrap your assistant

POST /chat returns the tool-using assistant's reply.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tool assistant")


class ChatIn(BaseModel):
    message: str


class ChatOut(BaseModel):
    answer: str
    tools_used: list[str]


@app.post("/chat", response_model=ChatOut)
def chat(body: ChatIn) -> ChatOut:
    # TODO: call your day 33 run() loop, track which tools were called, return ChatOut
    pass
