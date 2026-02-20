# Corey Thomas
# 19 Feb 2026
# P2HW2
# List of grades


# Assign variables to items named modules
Module_1 = float(input("Enter grade for Module 1: "))
Module_2 = float(input("Enter grade for Module 2: "))
Module_3 = float(input("Enter grade for Module 3: "))
Module_4 = float(input("Enter grade for Module 4: "))
Module_5 = float(input("Enter grade for Module 5: "))
Module_6 = float(input("Enter grade for Module 6: "))
print()

# Assign variables to list named grades
grades = [Module_1,Module_2,Module_3,Module_4,Module_5,Module_6]

# Pseudocode (detail algorithm)
Lowest_grade = min(grades)
Highest_grade = max(grades)
Sum = Module_1 + Module_2 + Module_3 + Module_4 + Module_5 + Module_6
Average = Sum / 6

# Displays
print("-----------------------Results--------------------")
print(f"{'Lowest Grade: ':35}{Lowest_grade}")
print(f"{'Highest Grade: ':35}{Highest_grade}")
print(f"{'Sum of Grades: ':35}{Sum}")
print(f"{'Average: ':35}{Average:.2f}")

sym = "-"
line = sym * 50
print(line)






