"""
Minimal Python MCP server for Claude Desktop (stdio transport).

Tools provided:
- echo(text): echoes the text
- add(a, b): adds two numbers
- get_time(tz): returns ISO timestamp in local time or UTC

Also exposes:
- Resource: greeting://{name}
- Prompt: Friendly Greeting

Run directly (stdio):
    python server.py

Dev with MCP Inspector (after installing mcp[cli]):
    mcp dev server.py

Install into Claude Desktop automatically:
    mcp install server.py --name "TestMCPPython"
"""

from __future__ import annotations

import datetime as _dt

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession


# Create the FastMCP server instance
mcp = FastMCP(
    name="TestMCPPython",
    instructions=(
        "A tiny demo MCP server written in Python. It has a few example tools, "
        "a resource, and a prompt."
    ),
)


@mcp.tool()
def echo(text: str) -> str:
    """Echo back the provided text."""

    return text


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""

    return a + b


@mcp.tool()
def get_time(tz: str = "local") -> str:
    """Get the current time as an ISO 8601 string.

    Parameters:
    - tz: "utc" for UTC time, anything else for local time.
    """

    now = _dt.datetime.utcnow() if tz.lower() == "utc" else _dt.datetime.now()
    # Ensure naive local times are clearly local; ISO format is fine for clients
    return now.isoformat()


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """A simple resource returning a greeting for the provided name."""

    return f"Hello, {name}!"


@mcp.prompt(title="Friendly Greeting")
def friendly_greeting(name: str) -> str:
    """Return a prompt template to generate a friendly greeting."""

    return f"Please write a short, friendly greeting for {name}."


def main() -> None:
    """Run the server using stdio (works with Claude Desktop)."""

    # Defaults to stdio transport when executed directly
    mcp.run()


if __name__ == "__main__":
    main()
