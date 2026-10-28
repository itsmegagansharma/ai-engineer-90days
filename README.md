# AI Engineer 90 Days

90 study days (Monday–Saturday, Sundays off) from beginner Python to Generative & Agentic AI Engineer.
Progress, reviews and help: [tracker](https://claude.ai/artifact/Q46bScTFaaMYYQyfNxW1JB).

## How the course works
Every study day has **three parallel tracks** (~2–3 hours in total):

| Track | Time | What it covers over 15 weeks |
|-------|------|------------------------------|
| Engineering | 60–75 min | Python → testing & APIs → FastAPI → Docker & CI → agent tooling → production & cloud |
| AI & ML | ~60 min | How LLMs work & prompting → stats & ML → LLM APIs & tools → RAG → deep learning → agents → LangGraph → deployment |
| Practice | ~30 min | Daily coding problems (with tests), Git & tools, interview questions, system design |

Day 6 of each week is a **build day** that combines the week's tracks into one project.

## Repo layout
- `day01/` … `day90/`: one folder per study day, one file per task: `task1_eng_…`, `task2_ai_…`, `task3_prac_…` (build days: `task1_build_…`).
- `.py` files have partial code with `TODO`s; practice files end with tests (`python file.py` prints "All tests passed!").
- Some later files build on earlier ones; their imports say which day to copy from.

## Daily routine
```
git checkout main && git pull
git checkout -b day-05
# complete the files in day05/
git add day05 && git commit -m "Day 5" && git push -u origin day-05
```
Tick your finished tasks on the tracker, press **Review my GitHub code**, then merge into main.

## Setup (day 1)
```
python -m venv .venv
# Windows: .venv\Scripts\activate     Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Weeks
| Week | Engineering · AI & ML | Days |
|------|-----------------------|------|
| 1 | Python basics · How AI & LLMs work | [01](day01/), [02](day02/), [03](day03/), [04](day04/), [05](day05/), [06](day06/) |
| 2 | Files, OOP & typing · Vectors, stats & data | [07](day07/), [08](day08/), [09](day09/), [10](day10/), [11](day11/), [12](day12/) |
| 3 | Testing & APIs · Your first LLM apps | [13](day13/), [14](day14/), [15](day15/), [16](day16/), [17](day17/), [18](day18/) |
| 4 | Data & SQL · Machine learning fundamentals | [19](day19/), [20](day20/), [21](day21/), [22](day22/), [23](day23/), [24](day24/) |
| 5 | APIs with FastAPI · Structured outputs & tools | [25](day25/), [26](day26/), [27](day27/), [28](day28/), [29](day29/), [30](day30/) |
| 6 | Docker · Classic ML algorithms | [31](day31/), [32](day32/), [33](day33/), [34](day34/), [35](day35/), [36](day36/) |
| 7 | Text processing · Embeddings & basic RAG | [37](day37/), [38](day38/), [39](day39/), [40](day40/), [41](day41/), [42](day42/) |
| 8 | UIs & vector stores · Advanced RAG | [43](day43/), [44](day44/), [45](day45/), [46](day46/), [47](day47/), [48](day48/) |
| 9 | CI & testing LLM apps · Deep learning & vision | [49](day49/), [50](day50/), [51](day51/), [52](day52/), [53](day53/), [54](day54/) |
| 10 | Reliable Python · Agent design patterns | [55](day55/), [56](day56/), [57](day57/), [58](day58/), [59](day59/), [60](day60/) |
| 11 | LangGraph · Memory & human-in-the-loop | [61](day61/), [62](day62/), [63](day63/), [64](day64/), [65](day65/), [66](day66/) |
| 12 | Agent tooling · Multi-agent & self-healing | [67](day67/), [68](day68/), [69](day69/), [70](day70/), [71](day71/), [72](day72/) |
| 13 | Production & security · Cloud & Kubernetes | [73](day73/), [74](day74/), [75](day75/), [76](day76/), [77](day77/), [78](day78/) |
| 14 | Capstone project | [79](day79/), [80](day80/), [81](day81/), [82](day82/), [83](day83/), [84](day84/) |
| 15 | Interview prep & applications | [85](day85/), [86](day86/), [87](day87/), [88](day88/), [89](day89/), [90](day90/) |
