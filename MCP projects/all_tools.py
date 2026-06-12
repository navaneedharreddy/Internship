from mcp.server.fastmcp import FastMCP
import pandas as pd

mcp = FastMCP("AllPythonPrograms")


# 1. Even or Odd
@mcp.tool()
def check_even_odd(number: int) -> str:
    return f"{number} is Even" if number % 2 == 0 else f"{number} is Odd"


# 2. Voting Eligibility
@mcp.tool()
def check_voting_eligibility(age: int) -> str:
    return "Eligible to Vote" if age >= 18 else "Not Eligible to Vote"


# 3. Compare Numbers
@mcp.tool()
def compare_numbers(first_number: int, second_number: int) -> str:
    if first_number > second_number:
        return f"{first_number} is greater than {second_number}"
    elif second_number > first_number:
        return f"{second_number} is greater than {first_number}"
    else:
        return "Both numbers are equal"


# 4. Positive, Negative, or Zero
@mcp.tool()
def check_number(number: int) -> str:
    if number > 0:
        return "Positive Number"
    elif number < 0:
        return "Negative Number"
    else:
        return "Zero"


# 5. Arithmetic Operations
@mcp.tool()
def calculate(number1: float, number2: float) -> dict:
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


# 6. First 10 Natural Numbers
@mcp.tool()
def print_natural_numbers() -> list:
    return list(range(1, 11))


# 7. First N Natural Numbers
@mcp.tool()
def print_n_natural_numbers(n: int) -> list:
    numbers = []
    count = 1

    while count <= n:
        numbers.append(count)
        count += 1

    return numbers


# 8. Multiplication Table
@mcp.tool()
def print_table(number: int) -> list:
    table = []

    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")

    return table


# 9. Table of 9
@mcp.tool()
def display_table_of_9() -> list:
    table = []

    for i in range(1, 11):
        table.append(f"9 x {i} = {9 * i}")

    return table


# 10. Sum of Digits
@mcp.tool()
def calculate_sum_of_digits(number: int) -> int:
    number = abs(number)
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number //= 10

    return digit_sum


# 11. Factorial
@mcp.tool()
def calculate_factorial(number: int) -> str:
    if number < 0:
        return "Factorial is not defined for negative numbers."

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return f"Factorial of {number} is {factorial}"


# 12. Factors of a Number
@mcp.tool()
def find_factors(number: int) -> list:
    factors = []

    for i in range(1, abs(number) + 1):
        if number % i == 0:
            factors.append(i)

    return factors


# 13. Prime Number Checker
@mcp.tool()
def check_prime(number: int) -> str:
    if number <= 1:
        return f"{number} is not a Prime Number"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a Prime Number"

    return f"{number} is a Prime Number"


# 14. Sum of List Elements
@mcp.tool()
def calculate_list_sum(numbers: list[int]) -> int:
    total = 0

    for num in numbers:
        total += num

    return total


# 15. Student Grade Calculator
@mcp.tool()
def calculate_grade(
    student_name: str,
    maths: int,
    physics: int,
    chemistry: int
) -> dict:

    total = maths + physics + chemistry
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return {
        "Student Name": student_name,
        "Maths": maths,
        "Physics": physics,
        "Chemistry": chemistry,
        "Total Marks": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }


# 16. Read CSV using Pandas
@mcp.tool()
def read_student_csv() -> str:
    df = pd.read_csv("students.csv")
    return df.head(10).to_string(index=False)


if __name__ == "__main__":
    mcp.run()