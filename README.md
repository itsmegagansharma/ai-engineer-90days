# AI Engineer 90 Days

My 90-day path from beginner Python to Generative & Agentic AI Engineer.
Progress, code reviews and help: [tracker](https://claude.ai/artifact/Q46bScTFaaMYYQyfNxW1JB).

## How this repo works
- `main` has a folder for every day: `day01/` … `day90/`.
- Each task has its own file. `.py` = partial code with `TODO`s to complete. `.md` = a worksheet to fill in.
- Each folder's `README.md` lists the tasks, the build goal and links for when you're stuck.

## Daily routine
```
git checkout main
git pull
git checkout -b day-05          # today's branch
# complete the files in day05/
git add day05
git commit -m "Day 5: Files, JSON & errors"
git push -u origin day-05
```
1. Press **Review my GitHub code** on that day in the tracker. Claude reviews what changed on the branch.
2. Fix anything the review flags, push again, and re-run the review if you like.
3. Merge into main: `git checkout main && git merge day-05 && git push`.

## Setup (day 1)
```
python -m venv .venv
# Windows: .venv\Scripts\activate     Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Weeks
| Week | Focus | Days |
|------|-------|------|
| 1 | Python core + Git | [01](day01/), [02](day02/), [03](day03/), [04](day04/), [05](day05/), [06](day06/), [07](day07/) |
| 2 | Intermediate Python, testing & APIs | [08](day08/), [09](day09/), [10](day10/), [11](day11/), [12](day12/), [13](day13/), [14](day14/) |
| 3 | Data, SQL & first ML models | [15](day15/), [16](day16/), [17](day17/), [18](day18/), [19](day19/), [20](day20/), [21](day21/) |
| 4 | ML algorithms from the job description | [22](day22/), [23](day23/), [24](day24/), [25](day25/), [26](day26/), [27](day27/), [28](day28/) |
| 5 | LLM fundamentals & API skills | [29](day29/), [30](day30/), [31](day31/), [32](day32/), [33](day33/), [34](day34/), [35](day35/) |
| 6 | Embeddings, vector DBs & basic RAG | [36](day36/), [37](day37/), [38](day38/), [39](day39/), [40](day40/), [41](day41/), [42](day42/) |
| 7 | Advanced RAG & vision models | [43](day43/), [44](day44/), [45](day45/), [46](day46/), [47](day47/), [48](day48/), [49](day49/) |
| 8 | Agent patterns & LangGraph basics | [50](day50/), [51](day51/), [52](day52/), [53](day53/), [54](day54/), [55](day55/), [56](day56/) |
| 9 | Memory, HITL, self-healing & multi-agent | [57](day57/), [58](day58/), [59](day59/), [60](day60/), [61](day61/), [62](day62/), [63](day63/) |
| 10 | Production: Docker, tests, CI/CD, observability | [64](day64/), [65](day65/), [66](day66/), [67](day67/), [68](day68/), [69](day69/), [70](day70/) |
| 11 | Cloud, Kubernetes, hybrid & on-prem | [71](day71/), [72](day72/), [73](day73/), [74](day74/), [75](day75/), [76](day76/), [77](day77/) |
| 12 | Capstone project | [78](day78/), [79](day79/), [80](day80/), [81](day81/), [82](day82/), [83](day83/), [84](day84/) |
| 13 | Interview prep & applications | [85](day85/), [86](day86/), [87](day87/), [88](day88/), [89](day89/), [90](day90/) |
