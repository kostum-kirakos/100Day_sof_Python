print("Welcome to the Tip Calculator\n")

# Use float() to convert user inputs to numbers
bill = float(input("What was the total bill: $"))
tip_percentage = float(input("What percentage tip would you like to give: "))
people = int(input("How many people to split the bill: "))

# Check tip_percentage to calculate the tip
if tip_percentage == 10:
    tip_factor = 1.10
elif tip_percentage == 12:
    tip_factor = 1.12
elif tip_percentage == 15:
    tip_factor = 1.15
else:
    # Handle an invalid tip percentage
    print("Invalid tip percentage. Please enter 10, 12, or 15.")
    exit()

# Calculate the total per person
result = bill * tip_factor / people 

# Display the result with two decimal places
print(f"Each person should pay: ${result: .2f}")
