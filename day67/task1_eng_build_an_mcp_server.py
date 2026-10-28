"""
Day 67 · Task 1 · Engineering: Build an MCP server

Build a small MCP server exposing a database query tool. Then: Use it from your agent or an MCP client.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: MCP server =====
# pip install "mcp[cli]"
# Run: mcp dev day67/task1_mcp_server.py
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


# ===== Part 2: Connect =====
# ## Connect your MCP server
# - [ ] Tested in `mcp dev` inspector
# - [ ] Connected to an MCP client (Claude desktop app or your own agent via an MCP adapter)
# - Question asked and what the agent did:
