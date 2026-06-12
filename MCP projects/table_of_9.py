from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TableOf9")

@mcp.tool()
def display_table_of_9() -> list:
    """
    Display the multiplication table of 9 using a for loop.
    """
    table = []

    for i in range(1, 11):
        table.append(f"9 x {i} = {9 * i}")

    return table

if __name__ == "__main__":
    mcp.run()