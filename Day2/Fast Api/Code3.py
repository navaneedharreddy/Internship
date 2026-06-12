from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Store comparisons
comparisons = {}

class Numbers(BaseModel):
    num1: int
    num2: int

# Function to compare numbers
def compare(num1, num2):
    if num1 > num2:
        return "First number is greater"
    elif num2 > num1:
        return "Second number is greater"
    else:
        return "Both numbers are equal"

# GET - Compare two numbers
@app.get("/compare/{num1}/{num2}")
def compare_numbers(num1: int, num2: int):
    return {
        "num1": num1,
        "num2": num2,
        "result": compare(num1, num2)
    }

# POST - Add a comparison
@app.post("/comparisons")
def add_comparison(data: Numbers):
    result = compare(data.num1, data.num2)

    key = f"{data.num1}-{data.num2}"
    comparisons[key] = result

    return {
        "message": "Comparison added successfully",
        "result": result
    }

# DELETE - Delete a comparison
@app.delete("/comparisons/{num1}/{num2}")
def delete_comparison(num1: int, num2: int):
    key = f"{num1}-{num2}"

    if key not in comparisons:
        return {"message": "Comparison not found"}

    del comparisons[key]

    return {"message": "Comparison deleted successfully"}

# GET - View all comparisons
@app.get("/comparisons")
def get_all_comparisons():
    return comparisons