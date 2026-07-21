age = int(input("Please enter your age:"))
test = (input("Did you pass the driving test? (yes/no):")). lower()
eligible = age >=18 and test == "yes"

print()
print("Age:", age)
print("Driving Test:", test)
print("Eligible for Driving License:", eligible)
