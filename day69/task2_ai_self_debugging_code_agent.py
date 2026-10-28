"""
Day 69 · Task 2 · AI & ML: Self-debugging code agent

Agent writes code, runs pytest, reads failures, fixes, repeats.

Complete every TODO, run the file, then tick this task on the tracker.
"""
"""Self-debugging code agent.
1. Ask the LLM to write solution.py for a task + given tests
2. Run pytest in a subprocess (in a temp folder, with a timeout)
3. If tests fail, send the failure output back and ask for a fix
4. Repeat up to 4 times"""
import subprocess
import tempfile
from pathlib import Path

TESTS = """from solution import is_palindrome
def test_simple(): assert is_palindrome("racecar")
def test_spaces(): assert is_palindrome("never odd or even")
def test_no(): assert not is_palindrome("python")
"""


def run_tests(code: str) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as d:
        Path(d, "solution.py").write_text(code)
        Path(d, "test_solution.py").write_text(TESTS)
        # TODO: subprocess.run(["pytest", "-q"], cwd=d, capture_output=True, text=True, timeout=30)
        # TODO: return (returncode == 0, stdout + stderr)
        pass

# TODO: the generate -> test -> fix loop
