# Corey Thomas
# 19 Feb 2026
# P2HW1
# Travel expenses

# Heading
print()
print("This program calculates and displays travel expenses")
print()

# Variables
# Budget entry
budget = float(input("Enter budget: "))
print()

# Travel Destination
destination = (input("Enter your travel destination: "))
print()

# Gas expenses
gas = float(input("How much do you think you will spend on gas? "))
print()

# Accommodation budget
accomodations = float(input("Approximately, how much will you need for accommodations/hotel? "))
print()

# Food expenses
food = float(input("Last, how much do you need for food? "))
print()

# Line
sym = "-"
line = sym * 51

# Heading
print("------------------Travel Expenses------------------")
print(f'{"Location:":40}{destination}')
# print(f"Location: {destination:} ")
print(f'{"Initial Budget: ":40}${budget:.2f}')
# print(f"Initial Budget: ${budget:.2f} ")
print(f'{"Fuel: ":40}${gas:.2f}')
# print(f"Fuel: ${gas:.2f} ")
print(f'{"Accommodations: ":40}${accomodations:.2f}')
# print(f"Accomodations: ${accomodations:.2f} ")
print(f'{"Food: ":40}${food:.2f}')
# print(f"Food: ${food:.2f} ")
print(line)
print()

#Operation - subtract expenses from budget
expenses = gas + accomodations + food
balance = budget- expenses

print(f'{"Remaining Balance: ":40}${balance}')
# print(f"Remaining Balance: ${balance}")

