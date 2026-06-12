from fastapi import FastAPI

app = FastAPI()

table_data = {}

# Function to generate table of 9
def table_of_9():
    result = []

    for i in range(1, 11):
        result.append(f"9 x {i} = {9 * i}")

    return result

# GET - Display table of 9
@app.get("/table9")
def get_table():
    return {
        "table": table_of_9()
    }

# POST - Store table of 9
@app.post("/table9")
def add_table():
    table_data["table9"] = table_of_9()

    return {
        "message": "Table stored successfully",
        "table": table_data["table9"]
    }

# DELETE - Delete stored table
@app.delete("/table9")
def delete_table():

    if "table9" not in table_data:
        return {"message": "Table not found"}

    del table_data["table9"]

    return {"message": "Table deleted successfully"}

# GET - View stored table
@app.get("/alltables")
def get_all_tables():
    return table_data