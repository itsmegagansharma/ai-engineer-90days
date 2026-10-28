"""
Day 60 · Task 1 · Build: research agent from scratch

Tools: web or notes search + calculator. Loop with ReAct, then a reflection pass. Stream progress over SSE.

Complete every TODO, run the file, then tick this task on the tracker.
"""
"""Research agent (no framework): plan -> search -> summarise -> reflect -> answer."""
from dataclasses import dataclass, field


@dataclass
class Trace:
    steps: list[dict] = field(default_factory=list)

    def log(self, kind: str, **data):
        self.steps.append({"kind": kind, **data})
        print(kind, data)


def research(question: str, max_steps: int = 8) -> str:
    trace = Trace()
    # TODO 1: ask the LLM for a short plan (2-4 search queries)
    # TODO 2: run each query with your search tool; collect findings
    # TODO 3: summarise findings into an answer with sources
    # TODO 4: reflection: ask the LLM if the answer fully addresses the question; if not, search once more
    # TODO 5: return the final answer; keep `trace` for debugging
    pass


if __name__ == "__main__":
    print(research("What are the main differences between RAG and fine-tuning?"))
