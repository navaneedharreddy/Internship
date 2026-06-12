from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NaturalNumbersWhile")

@mcp.tool()
def print_natural_numbers(n: int) -> list:
    """
    Print the first n natural numbers using a while loop.
    """
    numbers = []
    count = 1

    while count <= n:
        numbers.append(count)
        count += 1

    return numbers

if __name__ == "__main__":
    mcp.run()