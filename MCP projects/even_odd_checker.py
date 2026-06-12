from mcp.server.fastmcp import FastMCP

# Create MCP application
mcp = FastMCP("EvenOddChecker")

@mcp.tool()
def check_even_odd(number: int) -> str:
    """
    Check whether a number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even Number"
    else:
        return f"{number} is an Odd Number"

# Run the MCP server
if __name__ == "__main__":
    mcp.run()