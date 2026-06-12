from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

calculations = {}

class Numbers(BaseModel):
    num1: float
    num2: float

# Function for calculations
def calculate(num1, num2):
    return {
        "Addition": num1 + num2,
        "Subtraction": num1 - num2,
        "Multiplication": num1 * num2,
        "Division": num1 / num2 if num2 != 0 else "Cannot divide by zero"
    }

# GET - Perform calculations
@app.get("/calculate/{num1}/{num2}")
def get_calculation(num1: float, num2: float):
    return calculate(num1, num2)

# POST - Store calculation
@app.post("/calculations")
def add_calculation(data: Numbers):
    result = calculate(data.num1, data.num2)

    key = f"{data.num1}-{data.num2}"
    calculations[key] = result

    return {
        "message": "Calculation stored successfully",
        "result": result
    }

# PUT - Update calculation
@app.put("/calculations/{old_num1}/{old_num2}")
def update_calculation(old_num1: float, old_num2: float, data: Numbers):
    old_key = f"{old_num1}-{old_num2}"

    if old_key not in calculations:
        return {"message": "Calculation not found"}

    del calculations[old_key]

    new_key = f"{data.num1}-{data.num2}"
    result = calculate(data.num1, data.num2)

    calculations[new_key] = result

    return {
        "message": "Calculation updated successfully",
        "result": result
    }

# DELETE - Delete calculation
@app.delete("/calculations/{num1}/{num2}")
def delete_calculation(num1: float, num2: float):
    key = f"{num1}-{num2}"

    if key not in calculations:
        return {"message": "Calculation not found"}

    del calculations[key]

    return {"message": "Calculation deleted successfully"}

# GET - View all calculations
@app.get("/calculations")
def get_all_calculations():
    return calculations