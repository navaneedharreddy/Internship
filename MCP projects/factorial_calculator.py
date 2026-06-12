from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FactorialCalculator")

@mcp.tool()
def calculate_factorial(number: int) -> str:
    """
    Calculate the factorial of a number using a loop.
    """
    if number < 0:
        return "Factorial is not defined for negative numbers."

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return f"Factorial of {number} is {factorial}"

if __name__ == "__main__":
    mcp.run()