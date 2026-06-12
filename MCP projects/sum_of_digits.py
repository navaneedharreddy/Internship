from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SumOfDigits")

@mcp.tool()
def calculate_sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits of a number using a while loop.
    """
    number = abs(number)  # Handles negative numbers
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number //= 10

    return digit_sum

if __name__ == "__main__":
    mcp.run()