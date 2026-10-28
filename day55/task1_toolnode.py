"""
Day 55 · Task 1: ToolNode

Bind tools to a model and add a ToolNode.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install langgraph langchain-openai
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition


@tool
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression."""
    # TODO
    pass


tools = [calculator]
llm = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)   # or set base_url for Gemini/Ollama


def agent(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

# TODO: graph with "agent" and ToolNode(tools); START->agent; conditional edge tools_condition; tools->agent
