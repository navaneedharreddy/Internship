from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Store numbers
numbers = {}

class Number(BaseModel):
    number: int

# Function to check number type
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# GET - Check a number directly
@app.get("/check/{num}")
def get_number_status(num: int):
    return {
        "number": num,
        "status": check_number(num)
    }

# POST - Add a number
@app.post("/numbers")
def add_number(data: Number):
    status = check_number(data.number)

    numbers[data.number] = status

    return {
        "message": "Number added successfully",
        "number": data.number,
        "status": status
    }

# PUT - Update a number
@app.put("/numbers/{old_num}")
def update_number(old_num: int, data: Number):
    if old_num not in numbers:
        return {"message": "Number not found"}

    del numbers[old_num]

    status = check_number(data.number)
    numbers[data.number] = status

    return {
        "message": "Number updated successfully",
        "number": data.number,
        "status": status
    }

# DELETE - Delete a number
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