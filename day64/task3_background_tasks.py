"""
Day 64 · Task 3: Background tasks

Run long jobs in the background and return a job id.

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
