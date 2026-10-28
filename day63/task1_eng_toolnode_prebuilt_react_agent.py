"""
Day 63 · Task 1 · Engineering: ToolNode & prebuilt ReAct agent

Bind tools to a model and add a ToolNode. Then: Try create_react_agent and compare with your own loop.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: ToolNode =====
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


# ===== Part 2: Prebuilt ReAct =====
from langgraph.prebuilt import create_react_agent

# TODO: agent = create_react_agent(llm, tools)
# TODO: run the same 3 questions as your from-scratch agent and compare steps/answers
