# 1st Heading
print("=" * 40)
print("BMI CALCULATOR".center(40))
print("=" * 40)

# User Inputs
name = input("Please enter your name: ")
weight = float(input("Please enter your weight (kg): "))
height = float(input("Please enter your height (m): "))

# Formula
bmi = weight / (height * height)

# Blank Line
print()

# Display Results
print(f"Name   : {name}")
print(f"Weight : {weight:.2f} kg")
print(f"Height : {height:.2f} m")
print(f"BMI    : {bmi:.2f}")

print()
print("BMI calculated successfully!")
print("=" * 40)