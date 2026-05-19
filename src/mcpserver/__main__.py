import sys

from mcpserver.deployment import mcp


def main():
    print("Starting MCP server 'Demo' (transport: stdio)...", file=sys.stderr)
    mcp.run()


if __name__ == "__main__":
    main()
