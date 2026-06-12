from fastapi import FastAPI
import pandas as pd

app = FastAPI()

csv_data = {}

# GET - Read and display first 10 records
@app.get("/students")
def get_students():

    df = pd.read_csv("students.csv")

    first_10 = df.head(10)

    return first_10.to_dict(orient="records")

# POST - Store first 10 records
@app.post("/students")
def store_students():

    df = pd.read_csv("students.csv")

    csv_data["students"] = df.head(10).to_dict(orient="records")

    return {
        "message": "Student records stored successfully",
        "records": csv_data["students"]
    }

# DELETE - Delete stored records
@app.delete("/students")
def delete_students():

    if "students" not in csv_data:
        return {"message": "No records found"}

    del csv_data["students"]

    return {"message": "Student records deleted successfully"}

# GET - View stored records
@app.get("/allstudents")
def get_all_students():
    return csv_data