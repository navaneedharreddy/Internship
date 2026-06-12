from fastapi import FastAPI

app = FastAPI()

numbers_data = {}

# Function to generate first 10 natural numbers
def generate_numbers():
    numbers = []
    for i in range(1, 11):
        numbers.append(i)
    return numbers

# GET - Display first 10 natural numbers
@app.get("/numbers")
def get_numbers():
    return {
        "numbers": generate_numbers()
    }

# POST - Store numbers
@app.post("/numbers")
def add_numbers():
    numbers_data["first10"] = generate_numbers()
    return {
        "message": "Numbers stored successfully",
        "numbers": numbers_data["first10"]
    }

# PUT - Update numbers (re-generate)
@app.put("/numbers")
def update_numbers():
    numbers_data["first10"] = generate_numbers()
    return {
        "message": "Numbers updated successfully",
        "numbers": numbers_data["first10"]
    }

# DELETE - Delete stored numbers
@app.delete("/numbers")
def delete_numbers():
    if "first10" in numbers_data:
        del numbers_data["first10"]
        return {"message": "Numbers deleted successfully"}

    return {"message": "No numbers found"}