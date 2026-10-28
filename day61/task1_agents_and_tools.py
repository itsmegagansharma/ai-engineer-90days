"""
Day 61 · Task 1: Agents and tools

Build an agent with 2 tools.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install openai-agents
from agents import Agent, Runner, function_tool


@function_tool
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    # TODO
    pass


assistant = Agent(name="Assistant", instructions="Help the user.", tools=[get_weather])
# TODO: result = Runner.run_sync(assistant, "Weather in Nashik?"); print(result.final_output)
