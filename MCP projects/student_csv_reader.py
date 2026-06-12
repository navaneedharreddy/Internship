from mcp.server.fastmcp import FastMCP
import pandas as pd

mcp = FastMCP("StudentCSVReader")

@mcp.tool()
def read_student_csv() -> str:
    """
    Read CSV file and display first 10 records.
    """

    df = pd.read_csv("students.csv")

    return df.head(10).to_string(index=False)

if __name__ == "__main__":
    mcp.run()