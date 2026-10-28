"""
Day 26 · Task 1 · Engineering: Async endpoints

Make the /chat endpoint async.

Complete every TODO, run the file, then tick this task on the tracker.
"""
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/slow")
async def slow():
    # TODO: await asyncio.sleep(2) and return {"done": True}
    # Open /slow in 3 browser tabs at once. Do they finish together?
    pass
