# Day 53 · Task 1 · Engineering: Build images in CI & use secrets

> Build the Docker image in CI. Then: Store API keys as GitHub secrets.

## Part 1: Build image

## Add an image build step
```yaml
      - run: docker build -t my-agent .
```
- [ ] Green tick on GitHub

## Part 2: Secrets

## Secrets in CI
- [ ] Added `LLM_API_KEY` in GitHub → Settings → Secrets and variables → Actions
- Used in the workflow as: `env: LLM_API_KEY: ${{ secrets.LLM_API_KEY }}`
- Why tests should still mostly use mocks, not real API calls:
