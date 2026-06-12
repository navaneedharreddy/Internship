# Accept age from the user
age = int(input("Enter your age: "))

# Check eligibility for voting
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")