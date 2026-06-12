from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

student_records = {}

class Student(BaseModel):
    name: str
    maths: int
    physics: int
    chemistry: int

# Function to calculate grade
def calculate_grade(total):
    if total >= 270:
        return "A Grade"
    elif total >= 240:
        return "B Grade"
    elif total >= 180:
        return "C Grade"
    else:
        return "Fail"

# GET - Sample Student Result
@app.get("/student")
def get_student():
    maths = 90
    physics = 85
    chemistry = 95

    total = maths + physics + chemistry
    grade = calculate_grade(total)

    return {
        "name": "Navaneedhar",
        "total": total,
        "grade": grade
    }

# POST - Add Student Record
@app.post("/student")
def add_student(student: Student):

    total = student.maths + student.physics + student.chemistry
    grade = calculate_grade(total)

    student_records[student.name] = {
        "maths": student.maths,
        "physics": student.physics,
        "chemistry": student.chemistry,
        "total": total,
        "grade": grade
    }

    return {
        "message": "Student record stored successfully",
        "name": student.name,
        "total": total,
        "grade": grade
    }

# DELETE - Delete Student Record
@app.delete("/student/{name}")
def delete_student(name: str):

    if name not in student_records:
        return {"message": "Student not found"}

    del student_records[name]

    return {"message": "Student record deleted successfully"}

# GET - View All Records
@app.get("/students")
def get_students():
    return student_records