# Day 32: Structured outputs

**Week 5 · LLM fundamentals & API skills**

Agents need machine-readable outputs, not prose. Required in the job.

## Tasks
| # | File | Type |
|---|------|------|
| 1 | [JSON mode / schemas](task1_json_mode_schemas.py) | `py` |
| 2 | [Parse to Pydantic](task2_parse_to_pydantic.py) | `py` |
| 3 | [Retry on failure](task3_retry_on_failure.py) | `py` |

`.py` files have partial code: complete the TODOs and run them. `.md` files are worksheets: fill them in.

## Build goal
invoice_extractor.py: text → validated Invoice model

## If you get stuck
- [OpenAI structured outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- Open [day 32 on the tracker](https://claude.ai/artifact/Q46bScTFaaMYYQyfNxW1JB#day-32) and ask Claude in the chat.

## Submit for review
```
git checkout -b day-32
git add day32
git commit -m "Day 32: Structured outputs"
git push -u origin day-32
```
Then press **Review my GitHub code** on day 32 in the tracker.
