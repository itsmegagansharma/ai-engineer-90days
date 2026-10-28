# Day 65 · Task 3: docker compose

> App + Postgres(pgvector) in one compose file.

## docker-compose.yml
```yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [db]
  db:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_PASSWORD: pass
    # TODO: add a volume so data survives restarts
```
- [ ] `docker compose up` starts both
