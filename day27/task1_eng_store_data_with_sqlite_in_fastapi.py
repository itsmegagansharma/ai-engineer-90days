"""
Day 27 · Task 1 · Engineering: Store data with SQLite in FastAPI

Add a notes table and CRUD endpoints using sqlite3.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import sqlite3
from contextlib import closing

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB = "day27/notes.db"
app = FastAPI(title="Notes API")


def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


with closing(db()) as c:
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)")
    c.commit()


class NoteIn(BaseModel):
    text: str


@app.post("/notes")
def create(note: NoteIn):
    # TODO: INSERT with a ? placeholder (never f-strings: SQL injection!), return the new id
    pass


@app.get("/notes")
def list_notes():
    # TODO: SELECT all, return [dict(row) for row in rows]
    pass


@app.delete("/notes/{note_id}")
def delete(note_id: int):
    # TODO: DELETE; raise HTTPException(404) if nothing was deleted
    pass
