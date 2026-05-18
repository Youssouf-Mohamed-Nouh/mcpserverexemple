from mcpserver.deployment import mcp


def main():
    print("🚀 Starting MCP server 'Demo' (transport: stdio)...")
    mcp.run()


if __name__ == "__main__":
    main()