"""
Day 29 · Task 1 · Engineering: Logging & error handling in APIs

Use the logging module and an exception handler that returns clean JSON errors.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("api")
app = FastAPI()


@app.exception_handler(Exception)
async def unhandled(request: Request, exc: Exception):
    # TODO: log.exception(...) with the path, return JSONResponse({"error": "Something went wrong"}, status_code=500)
    pass


@app.get("/boom")
def boom():
    raise RuntimeError("test failure")

# TODO: add a middleware that logs method, path, status code and duration in ms for every request
