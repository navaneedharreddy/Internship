from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NaturalNumbers")

@mcp.tool()
def print_natural_numbers() -> list:
    """
    Print the first 10 natural numbers.
    """
    numbers = []

    for i in range(1, 11):
        numbers.append(i)

    return numbers

if __name__ == "__main__":
    mcp.run()