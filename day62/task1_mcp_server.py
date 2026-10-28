"""
Day 62 · Task 1: MCP server

Build a small MCP server exposing a database query tool.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install "mcp[cli]"
# Run: mcp dev day62/task1_mcp_server.py
import sqlite3

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("company-db")


@mcp.tool()
def list_tables() -> list[str]:
    """List tables in the company database."""
    # TODO
    pass


@mcp.tool()
def query(sql: str) -> list[dict]:
    """Run a read-only SELECT query."""
    # TODO: refuse non-SELECT; open the db read-only; return rows as dicts
    pass


if __name__ == "__main__":
    mcp.run()
