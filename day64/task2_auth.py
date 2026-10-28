"""
Day 64 · Task 2: Auth

Protect endpoints with API keys or JWT.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import os

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


def require_key(x_api_key: str = Header(...)):
    # TODO: compare with os.getenv("APP_API_KEY"); raise HTTPException(401) if wrong
    pass


@app.get("/private", dependencies=[Depends(require_key)])
def private():
    return {"secret": "only with a key"}
