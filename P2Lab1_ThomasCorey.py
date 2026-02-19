# Corey Thomas
# 17 Feb 2026
# P2Lab1
# Use math library to calculate circle formulas

import math

# Assign radius and user input
print()
radius = float(input("What is the radius of the circle: "))

# Calculate the diameter
diameter = 2 * radius

# print (math.pi)

# Calculate the circumference
circumference = 2 * math.pi * radius

# Calculate the area
area = math.pi * math.pow(radius, 2)

# Display results to the user
print()
print (f"The diameter of the circle is: {diameter:.1f}")
print()
print (f"The circumference of the circle is: {circumference:.2f}")
print()
print (f"The area of the circle is: {area:.3f}")