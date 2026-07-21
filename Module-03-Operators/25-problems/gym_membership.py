age = int(input("Please enter your age:"))
is_medically_fit = (input("Are you medically fit? (yes/no):")). lower()
eligible = age >=18 and is_medically_fit == "yes"

print()
print("Age:", age)
print("Medical Fitness:", is_medically_fit)
print("Eligible for Gym Membership:", eligible)
