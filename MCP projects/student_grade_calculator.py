from mcp.server.fastmcp import FastMCP

mcp = FastMCP("StudentGradeCalculator")

@mcp.tool()
def calculate_grade(
    student_name: str,
    maths: int,
    physics: int,
    chemistry: int
) -> dict:
    """
    Calculate total marks and grade for a student.
    """

    total = maths + physics + chemistry
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return {
        "Student Name": student_name,
        "Maths": maths,
        "Physics": physics,
        "Chemistry": chemistry,
        "Total Marks": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

if __name__ == "__main__":
    mcp.run()