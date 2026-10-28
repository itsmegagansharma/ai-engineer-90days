# Day 28 · Task 3 · Practice: Debug HTTP with curl

> Call your own API from the terminal with curl and read status codes and headers.

## curl practice (run your FastAPI app first)
```
curl -i http://127.0.0.1:8000/notes
curl -i -X POST http://127.0.0.1:8000/notes -H "Content-Type: application/json" -d '{"text":"hi"}'
curl -i -X DELETE http://127.0.0.1:8000/notes/999
```
- What does `-i` show?
- Status code for the missing note:
