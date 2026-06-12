from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

prime_data = {}

class NumberInput(BaseModel):
    number: int

# Function to check prime
def is_prime(number):
    if number <= 1:
        return "Not Prime"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Not Prime"

    return "Prime"

# GET - Check Prime
@app.get("/prime/{number}")
def get_prime(number: int):
    return {
        "number": number,
        "result": is_prime(number)
    }

# POST - Store Prime Result
@app.post("/prime")
def add_prime(data: NumberInput):

    result = is_prime(data.number)

    prime_data[data.number] = result

    return {
        "message": "Result stored successfully",
        "number": data.number,
        "result": result
    }

# DELETE - Delete Prime Result
@app.delete("/prime/{number}")
def delete_prime(number: int):

    if number not in prime_data:
        return {"message": "Number not found"}

    del prime_data[number]

    return {"message": "Result deleted successfully"}

# GET - View All Results
@app.get("/allprimes")
def get_all_primes():
    return prime_data