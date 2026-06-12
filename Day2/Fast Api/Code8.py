from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tables = {}

class NumberInput(BaseModel):
    number: int

# Function to generate multiplication table
def multiplication_table(number):
    result = []

    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")

    return result

# GET - Display multiplication table
@app.get("/table/{number}")
def get_table(number: int):
    return {
        "number": number,
        "table": multiplication_table(number)
    }

# POST - Store multiplication table
@app.post("/table")
def add_table(data: NumberInput):

    tables[data.number] = multiplication_table(data.number)

    return {
        "message": "Table stored successfully",
        "table": tables[data.number]
    }

# DELETE - Delete multiplication table
@app.delete("/table/{number}")
def delete_table(number: int):

    if number not in tables:
        return {"message": "Table not found"}

    del tables[number]

    return {"message": "Table deleted successfully"}

# GET - View all stored tables
@app.get("/tables")
def get_all_tables():
    return tables