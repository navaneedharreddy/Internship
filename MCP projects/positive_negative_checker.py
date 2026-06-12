from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PositiveNegativeChecker")

@mcp.tool()
def check_number(number: int) -> str:
    """
    Check whether a number is positive, negative, or zero.
    """
    if number > 0:
        return f"{number} is a Positive Number"
    elif number < 0:
        return f"{number} is a Negative Number"
    else:
        return "The number is Zero"

if __name__ == "__main__":
    mcp.run()