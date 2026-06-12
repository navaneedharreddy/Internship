from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

factorials = {}

class NumberInput(BaseModel):
    number: int

# Function to calculate factorial
def factorial(number):
    if number < 0:
        return "Factorial not defined for negative numbers"

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

# GET - Calculate factorial
@app.get("/factorial/{number}")
def get_factorial(number: int):
    return {
        "number": number,
        "factorial": factorial(number)
    }

# POST - Store factorial result
@app.post("/factorial")
def add_factorial(data: NumberInput):

    result = factorial(data.number)

    factorials[data.number] = result

    return {
        "message": "Factorial stored successfully",
        "number": data.number,
        "factorial": result
    }

# DELETE - Delete factorial result
@app.delete("/factorial/{number}")
def delete_factorial(number: int):

    if number not in factorials:
        return {"message": "Number not found"}

    del factorials[number]

    return {"message": "Factorial deleted successfully"}

# GET - View all stored factorials
@app.get("/allfactorials")
def get_all_factorials():
    return factorials