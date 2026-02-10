# Corey Thomas
# 10 Feb 2026
# P1HW2
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

# Heading
print("-----------Travel Expenses-----------")
print(f"Location: {destination} ")
print(f"Initial Budget: {budget} ")
print()
print(f"Fuel: {gas} ")
print(f"Accomodations: {accomodations} ")
print(f"Food: {food} ")
print()

#Operation - subtract expenses from budget
expenses = gas + accomodations + food
balance = budget - expenses

print(f"Remaining Balance: {balance}")

