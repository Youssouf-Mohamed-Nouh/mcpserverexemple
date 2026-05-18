from mcp.server.fastmcp import FastMCP

# Création d’un serveur MCP nommé "Demo"
mcp = FastMCP("Demo")


# Déclaration d’un outil MCP qui additionne deux nombres
@mcp.tool()
def add(a: int, b: int) -> int:
    """Additionne deux nombres"""
    return a + b