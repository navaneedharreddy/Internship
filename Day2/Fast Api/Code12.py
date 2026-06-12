from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

factors_data = {}

class NumberInput(BaseModel):
    number: int

# Function to find factors
def find_factors(number):
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

# GET - Display factors
@app.get("/factors/{number}")
def get_factors(number: int):
    return {
        "number": number,
        "factors": find_factors(number)
    }

# POST - Store factors
@app.post("/factors")
def add_factors(data: NumberInput):

    result = find_factors(data.number)

    factors_data[data.number] = result

    return {
        "message": "Factors stored successfully",
        "number": data.number,
        "factors": result
    }

# DELETE - Delete stored factors
@app.delete("/factors/{number}")
def delete_factors(number: int):

    if number not in factors_data:
        return {"message": "Number not found"}

    del factors_data[number]

    return {"message": "Factors deleted successfully"}

# GET - View all stored factors
@app.get("/allfactors")
def get_all_factors():
    return factors_data