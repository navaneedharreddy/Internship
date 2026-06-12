from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ArithmeticOperations")

@mcp.tool()
def calculate(number1: float, number2: float) -> dict:
    """
    Perform addition, subtraction, multiplication, and division.
    """
    
    result = {
        "Addition": number1 + number2,
        "Subtraction": number1 - number2,
        "Multiplication": number1 * number2
    }

    if number2 != 0:
        result["Division"] = number1 / number2
    else:
        result["Division"] = "Cannot divide by zero"

    return result

if __name__ == "__main__":
    mcp.run()