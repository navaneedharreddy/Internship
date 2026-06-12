from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stored_numbers = {}

class NumberInput(BaseModel):
    n: int

# Function using while loop
def generate_numbers(n):
    numbers = []
    i = 1

    while i <= n:
        numbers.append(i)
        i += 1

    return numbers

# GET - Display first n natural numbers
@app.get("/numbers/{n}")
def get_numbers(n: int):
    return {
        "numbers": generate_numbers(n)
    }

# POST - Store numbers
@app.post("/numbers")
def add_numbers(data: NumberInput):
    stored_numbers[data.n] = generate_numbers(data.n)

    return {
        "message": "Numbers stored successfully",
        "numbers": stored_numbers[data.n]
    }

# PUT - Update numbers
@app.put("/numbers/{old_n}")
def update_numbers(old_n: int, data: NumberInput):

    if old_n in stored_numbers:
        del stored_numbers[old_n]

    stored_numbers[data.n] = generate_numbers(data.n)

    return {
        "message": "Numbers updated successfully",
        "numbers": stored_numbers[data.n]
    }

# DELETE - Delete stored numbers
@app.delete("/numbers/{n}")
def delete_numbers(n: int):

    if n not in stored_numbers:
        return {"message": "Data not found"}

    del stored_numbers[n]

    return {"message": "Numbers deleted successfully"}

# GET - View all stored data
@app.get("/allnumbers")
def get_all_numbers():
    return stored_numbers