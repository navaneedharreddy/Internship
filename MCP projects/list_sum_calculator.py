from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ListSumCalculator")

@mcp.tool()
def calculate_list_sum(numbers: list[int]) -> str:
    """
    Calculate the sum of all elements in a list.
    """
    total = 0

    for num in numbers:
        total += num

    return f"Sum of the list elements is {total}"

if __name__ == "__main__":
    mcp.run()