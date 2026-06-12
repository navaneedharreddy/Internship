from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NumberComparison")

@mcp.tool()
def compare_numbers(first_number: int, second_number: int) -> str:
    """
    Compare two numbers and determine which one is greater.
    """
    if first_number > second_number:
        return f"{first_number} is greater than {second_number}"
    elif second_number > first_number:
        return f"{second_number} is greater than {first_number}"
    else:
        return "Both numbers are equal"

if __name__ == "__main__":
    mcp.run()