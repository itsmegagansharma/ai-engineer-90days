# Day 78 · Task 3: Architecture

> Agents, tools, data stores, deployment.

## Architecture
```mermaid
flowchart TD
  U[User] --> API[FastAPI]
  API --> SUP[Supervisor agent]
  SUP --> R[Retrieval agent]
  SUP --> A[Action agent]
  A --> HITL{Human approval}
```
