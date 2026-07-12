from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple MCP Server")


@mcp.tool()
def byebye(name: str) -> str:
    """
    Say goodbye to someone
    """
    return f"Goodbye {name} from FastAPI MCP Server!"

@mcp.tool()
def reverse_text(text: str) -> str:
    """
    Reverse a string
    """
    return text[::-1]


@mcp.tool()
def word_count(text: str) -> int:
    """
    Count words in a text
    """
    return len(text.split())


@mcp.tool()
def uppercase(text: str) -> str:
    """
    Convert text to uppercase
    """
    return text.upper()

if __name__ == "__main__":
    mcp.run()