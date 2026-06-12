from mcp.server.fastmcp import FastMCP

mcp = FastMCP("VotingEligibilityChecker")

@mcp.tool()
def check_voting_eligibility(age: int) -> str:
    if age >= 18:
        return f"Age {age}: Eligible to vote"
    else:
        return f"Age {age}: Not eligible to vote"

if __name__ == "__main__":
    mcp.run()