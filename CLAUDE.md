# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A 90-day self-study curriculum (beginner Python → Generative & Agentic AI Engineer), not an application. There is no package, no entry point, and nothing to build. Each of `day01/`…`day90/` holds one day's worth of exercises.

**The `.py` files are intentionally incomplete.** All 148 ship with `TODO` comments and `pass` bodies for the learner to fill in; 95 contain a bare `pass`. Running one as shipped is *expected* to raise `AssertionError` or `TypeError`. Do not "fix" these files, implement their TODOs, or treat the failures as bugs unless the user explicitly asks for help with that day's task.

## Commands

```bash
# Setup (once)
python -m venv .venv
.venv\Scripts\activate        # Windows;  source .venv/bin/activate on Mac/Linux
pip install -r requirements.txt
cp .env.example .env

# Verify one exercise — the only test runner that matters here
python day02/task3_prac_problems_fizzbuzz_reverse_string.py   # prints "All tests passed!"

ruff check day05/            # lint (ruff is the linter this course uses)
```

Nothing is installed globally — `python -m pytest` and `ruff` both fail on a bare machine until the venv above is created and activated.

`requirements.txt` is deliberately month-1 only. Heavier packages (`torch`, `openai`, `fastapi`, `langgraph`, `chromadb`, …) are commented out and installed ad hoc as each day reaches them, so a `ModuleNotFoundError` on a later day usually means "pip install it now", not a broken environment.

### Testing

**`pytest` collects nothing.** There are no `test_*.py` files and no pytest/pyproject config; `pytest` and `pytest-cov` are in `requirements.txt` only so Day 13 can teach them. Verification is per-file instead: practice files end in an `if __name__ == "__main__":` block of `assert`s that prints `All tests passed!` (29 files follow this). To check a single exercise, run that one file directly — there is no suite-wide command, and nothing aggregates across days.

## Conventions

Filenames encode day, task number, and track — `day05/task2_ai_tokens_context_windows.py` is day 5, task 2, AI & ML track. Prefixes:

| Prefix | Count | Meaning |
|---|---|---|
| `task1_eng_` | 75 | Engineering track (60–75 min) |
| `task2_ai_` | 75 | AI & ML track (~60 min) |
| `task3_prac_` | 75 | Practice: coding problems, Git, interview questions, system design (~30 min) |
| `task1_build_` | 15 | Build day — day 6 of each week, combines that week's tracks into one project |
| `task2_review_`, `task3_review_` | 15 each | Recap quiz / writing task, paired with build days |

The `*_review_*` prefixes are not documented in README.md but exist on every build day.

- `.md` files are worksheets with blanks to fill in (quiz scores, checklists, design notes), not documentation to read for facts. Of 270 task files, 122 are `.md` and 148 are `.py` (the 90 `dayNN/README.md` files are separate).
- Each `dayNN/README.md` carries that day's task table; it is the source of truth for which files belong to the day. Orphaned files not listed there are stale.
- Filenames must stay stable — each day's README links to them by exact name, as does the external tracker.

## Cross-day dependencies

Some later files build on earlier ones and say so in a TODO (e.g. day 30 says "call your day 33 `run()` loop"; day 28 and day 42 do likewise). These reference *the learner's own completed solution* from the earlier day, which does not exist in this repo. Such a file cannot run from a clean checkout even when implemented correctly — it needs the earlier day finished first. Note that the day numbers in these comments are sometimes wrong relative to the current curriculum.

## LLM provider setup

Every LLM exercise uses one OpenAI-compatible client, switched entirely through `.env` so the same code works across providers (`.env.example` lists the variables):

```python
client = OpenAI(base_url=os.getenv("LLM_BASE_URL") or None, api_key=os.getenv("LLM_API_KEY"))
MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
```

`LLM_API_KEY` / `LLM_BASE_URL` appear in ~26 files. `LLM_BASE_URL` is unset for OpenAI, `https://generativelanguage.googleapis.com/v1beta/openai/` for Gemini's free tier, `http://localhost:11434/v1` for local Ollama. Prefer this indirection over hardcoding a provider in new examples.

## Git workflow

One branch per day, merged to `main` after review (from README.md):

```bash
git checkout main && git pull
git checkout -b day-05
git add day05 && git commit -m "Day 5" && git push -u origin day-05
```

`data/` and `*.csv` are gitignored (except `sample*.csv`), so exercise datasets stay local.
