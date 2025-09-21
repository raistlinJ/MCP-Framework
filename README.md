# TestMCPPython MCP Server

A minimal Python MCP server (stdio) with a couple of example tools, a resource, and a prompt—ready for Claude Desktop.

## Features
- Tools:
  - `echo(text: str) -> str`
  - `add(a: float, b: float) -> float`
  - `get_time(tz: str = "local") -> str`
- Resource: `greeting://{name}`
- Prompt: `Friendly Greeting`

## Install dependencies

Using pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or with uv (optional):

```bash
uv sync
```

## Quick test (syntax)

```bash
python -m py_compile server.py
```

## Dev with MCP Inspector

```bash
# If using uv-managed env
uv run mcp dev server.py

# Or plain pip env
mcp dev server.py
```

## Install into Claude Desktop

Claude Desktop can auto-register stdio servers via the MCP CLI:

```bash
# uv style
uv run mcp install server.py --name "TestMCPPython"

# or pip style
mcp install server.py --name "TestMCPPython"
```

Alternatively, configure manually in Claude Desktop settings JSON (macOS):

- Config file: `~/Library/Application Support/Claude/mcp.json`
- Add an entry like:

```json
{
  "mcpServers": {
    "TestMCPPython": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"],
      "env": {}
    }
  }
}
```

Replace the path with your actual project path.

## Run directly

```bash
python server.py
```

This runs the server over stdio; MCP clients (like Claude Desktop) will connect to it when configured.
