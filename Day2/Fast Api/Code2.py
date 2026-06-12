from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Store data in memory
voters = {}

class Person(BaseModel):
    name: str
    age: int

# GET - Check voting eligibility by age
@app.get("/vote/{age}")
def check_vote(age: int):
    if age >= 18:
        return {"age": age, "status": "Eligible to Vote"}
    else:
        return {"age": age, "status": "Not Eligible to Vote"}

# POST - Add a person
@app.post("/voters")
def add_voter(person: Person):
    status = "Eligible to Vote" if person.age >= 18 else "Not Eligible to Vote"

    voters[person.name] = {
        "age": person.age,
        "status": status
    }

    return {
        "message": "Person added successfully",
        "name": person.name,
        "age": person.age,
        "status": status
    }

# PUT - Update a person's age
@app.put("/voters/{name}")
def update_voter(name: str, person: Person):
    if name not in voters:
        return {"message": "Person not found"}

    status = "Eligible to Vote" if person.age >= 18 else "Not Eligible to Vote"

    voters[name] = {
        "age": person.age,
        "status": status
    }

    return {
        "message": "Person updated successfully",
        "name": name,
        "age": person.age,
        "status": status
    }

# DELETE - Remove a person
@app.delete("/voters/{name}")
def delete_voter(name: str):
    if name not in voters:
        return {"message": "Person not found"}

    del voters[name]

    return {"message": "Person deleted successfully"}

# GET - View all voters
@app.get("/voters")
def get_all_voters():
    return voters