# Day 68 · Task 3: Secrets

> Store API keys as GitHub secrets.

## Secrets in CI
- [ ] Added `LLM_API_KEY` in GitHub → Settings → Secrets and variables → Actions
- Used in the workflow as: `env: LLM_API_KEY: ${{ secrets.LLM_API_KEY }}`
- Why tests should still mostly use mocks, not real API calls:
