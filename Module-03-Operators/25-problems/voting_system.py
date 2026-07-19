# Voting Eligibility System

age = int(input("Please enter your age: "))

citizen = input("Are you a citizen? (yes/no): ").lower()

is_citizen = citizen == "yes"

eligible = age >= 18 and is_citizen

print()
print("Age:", age)
print("Citizen:", is_citizen)
print("Eligible to Vote:", eligible)