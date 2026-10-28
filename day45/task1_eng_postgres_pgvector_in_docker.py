"""
Day 45 · Task 1 · Engineering: Postgres + pgvector in Docker

Run Postgres with pgvector in Docker; create a vector column and query by distance.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# Start Postgres with pgvector:
#   docker run -d --name pg -e POSTGRES_PASSWORD=pass -p 5432:5432 pgvector/pgvector:pg16
# pip install "psycopg[binary]" pgvector
import psycopg
from pgvector.psycopg import register_vector

conn = psycopg.connect("postgresql://postgres:pass@localhost:5432/postgres", autocommit=True)
conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
register_vector(conn)

# TODO: CREATE TABLE chunks (id serial primary key, text text, source text, embedding vector(384))
# TODO: insert embeddings; query: SELECT text FROM chunks ORDER BY embedding <=> %s LIMIT 5
