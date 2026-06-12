from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

list_data = {}

class NumberList(BaseModel):
    numbers: List[int]

# Function to calculate sum
def calculate_sum(numbers):
    return sum(numbers)

# GET - Example list sum
@app.get("/sumlist")
def get_sum():
    sample_list = [10, 20, 30, 40, 50]

    return {
        "list": sample_list,
        "sum": calculate_sum(sample_list)
    }

# POST - Calculate and store sum
@app.post("/sumlist")
def add_list(data: NumberList):

    total = calculate_sum(data.numbers)

    list_data["numbers"] = {
        "list": data.numbers,
        "sum": total
    }

    return {
        "message": "List stored successfully",
        "sum": total
    }

# DELETE - Delete stored list
@app.delete("/sumlist")
def delete_list():

    if "numbers" not in list_data:
        return {"message": "No data found"}

    del list_data["numbers"]

    return {"message": "List deleted successfully"}

# GET - View stored data
@app.get("/alllists")
def get_all_lists():
    return list_data