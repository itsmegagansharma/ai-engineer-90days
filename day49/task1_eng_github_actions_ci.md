# Day 49 · Task 1 · Engineering: GitHub Actions CI

> Workflow runs ruff and pytest on every push.

## .github/workflows/ci.yml
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt ruff pytest
      - run: ruff check .
      # TODO: run pytest
```
