"""
Day 28 · Task 1 · Engineering: Test FastAPI with TestClient

Write tests for the notes API without starting a server.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# pip install httpx    Run: pytest day28 -v
from fastapi.testclient import TestClient

from task1_store_data_with_sqlite_in_fastapi import app   # adjust to your file/module name

client = TestClient(app)


def test_create_and_list():
    r = client.post("/notes", json={"text": "hello"})
    assert r.status_code == 200
    # TODO: GET /notes and assert "hello" is in the texts


def test_delete_missing_returns_404():
    # TODO
    pass


def test_validation_error():
    # TODO: POST without "text" -> 422
    pass
