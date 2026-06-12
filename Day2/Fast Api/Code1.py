from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Store numbers in memory
numbers = {}

class Number(BaseModel):
    number: int

# GET - Check if a number is Even or Odd
@app.get("/check/{num}")
def check_number(num: int):
    result = "Even" if num % 2 == 0 else "Odd"
    return {"number": num, "result": result}

# POST - Add a number
@app.post("/numbers")
def add_number(data: Number):
    result = "Even" if data.number % 2 == 0 else "Odd"
    numbers[data.number] = result
    return {
        "message": "Number added successfully",
        "number": data.number,
        "result": result
    }

# PUT - Update an existing number
@app.put("/numbers/{old_num}")
def update_number(old_num: int, data: Number):
    if old_num not in numbers:
        return {"message": "Number not found"}

    del numbers[old_num]

    result = "Even" if data.number % 2 == 0 else "Odd"
    numbers[data.number] = result

    return {
        "message": "Number updated successfully",
        "number": data.number,
        "result": result
    }

# DELETE - Remove a number
@app.delete("/numbers/{num}")
def delete_number(num: int):
    if num not in numbers:
        return {"message": "Number not found"}

    del numbers[num]

    return {"message": "Number deleted successfully"}

# GET - View all stored numbers
@app.get("/numbers")
def get_all_numbers():
    return numbers