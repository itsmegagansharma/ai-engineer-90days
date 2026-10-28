"""
Day 70 · Task 1 · Engineering: API keys & background jobs

Protect endpoints with API keys or JWT. Then: Run long jobs in the background and return a job id.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Auth =====
import os

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


def require_key(x_api_key: str = Header(...)):
    # TODO: compare with os.getenv("APP_API_KEY"); raise HTTPException(401) if wrong
    pass


@app.get("/private", dependencies=[Depends(require_key)])
def private():
    return {"secret": "only with a key"}


# ===== Part 2: Background tasks =====
import uuid

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()
JOBS: dict[str, dict] = {}


def long_job(job_id: str, task: str):
    # TODO: run your agent; set JOBS[job_id] = {"status": "done", "result": ...}
    pass


@app.post("/jobs")
def create(task: str, bg: BackgroundTasks):
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {"status": "running"}
    bg.add_task(long_job, job_id, task)
    return {"job_id": job_id}

# TODO: GET /jobs/{job_id} returns the status/result
