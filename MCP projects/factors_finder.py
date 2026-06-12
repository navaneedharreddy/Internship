from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FactorsFinder")

@mcp.tool()
def find_factors(number: int) -> list:
    """
    Find and display all factors of a given number.
    """
    factors = []

    for i in range(1, abs(number) + 1):
        if number % i == 0:
            factors.append(i)

    return factors

if __name__ == "__main__":
    mcp.run()