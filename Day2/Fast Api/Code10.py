from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

digit_sums = {}

class NumberInput(BaseModel):
    number: int

# Function to calculate sum of digits
def sum_of_digits(number):
    total = 0
    n = abs(number)

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total

# GET - Calculate sum of digits
@app.get("/sumdigits/{number}")
def get_sum_digits(number: int):
    return {
        "number": number,
        "sum_of_digits": sum_of_digits(number)
    }

# POST - Store result
@app.post("/sumdigits")
def add_sum_digits(data: NumberInput):

    result = sum_of_digits(data.number)

    digit_sums[data.number] = result

    return {
        "message": "Result stored successfully",
        "number": data.number,
        "sum_of_digits": result
    }

# DELETE - Delete stored result
@app.delete("/sumdigits/{number}")
def delete_sum_digits(number: int):

    if number not in digit_sums:
        return {"message": "Number not found"}

    del digit_sums[number]

    return {"message": "Result deleted successfully"}

# GET - View all stored results
@app.get("/allsums")
def get_all_sums():
    return digit_sums