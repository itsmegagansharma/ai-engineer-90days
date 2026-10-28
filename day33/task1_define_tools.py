"""
Day 33 · Task 1: Define tools

Describe calculator and get_weather with JSON schemas.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Tool definitions in the OpenAI "tools" format
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic arithmetic expression like '12 * (3 + 4)'.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
            },
        },
    },
    # TODO: add get_weather(city: str) in the same format
]


def calculator(expression: str) -> str:
    # TODO: evaluate safely: only allow digits, spaces and + - * / ( ) .
    pass


def get_weather(city: str) -> str:
    # TODO: reuse your day 12 code, return a short text summary
    pass
