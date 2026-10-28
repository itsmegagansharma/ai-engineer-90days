"""
Day 64 · Task 1: Streaming

Stream agent output with Server-Sent Events.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/stream")
def stream(q: str):
    def events():
        # TODO: for each token from your agent/LLM stream: yield f"data: {token}\n\n"
        yield "data: [DONE]\n\n"
    return StreamingResponse(events(), media_type="text/event-stream")
