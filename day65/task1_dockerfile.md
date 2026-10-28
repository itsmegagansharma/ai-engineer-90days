# Day 65 · Task 1: Dockerfile

> Write a Dockerfile for your FastAPI app; build and run it.

## Dockerfile (save as Dockerfile in your app folder)
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# TODO: expose port 8000 and start uvicorn
```
Commands:
```
docker build -t my-agent .
docker run -p 8000:8000 --env-file .env my-agent
```
