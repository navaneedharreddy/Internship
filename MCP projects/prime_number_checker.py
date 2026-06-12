from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PrimeNumberChecker")

@mcp.tool()
def check_prime(number: int) -> str:
    """
    Check whether a number is prime or not.
    """
    if number <= 1:
        return f"{number} is not a Prime Number"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a Prime Number"

    return f"{number} is a Prime Number"

if __name__ == "__main__":
    mcp.run()