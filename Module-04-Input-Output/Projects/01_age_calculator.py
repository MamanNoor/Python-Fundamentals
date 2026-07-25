# 1st Heading
print("=" * 40)
print("AGE CALCULATOR".center(40))
print("=" * 40)

# User Inputs
name = input("Please enter your name: ")
birth_year = int(input("Please enter your birth year: "))
current_year = int(input("Please enter the current year: "))

# Formula
age = current_year - birth_year

# Blank Line
print()

# Display Results
print(f"Name         : {name}")
print(f"Birth Year   : {birth_year}")
print(f"Current Year : {current_year}")
print(f"Age          : {age} years")

print()
print("Age calculated successfully!")
print("=" * 40)