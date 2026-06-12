from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MultiplicationTable")

@mcp.tool()
def print_table(number: int) -> list:
    """
    Print the multiplication table of a number from 1 to 10.
    """
    table = []

    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")

    return table

if __name__ == "__main__":
    mcp.run()