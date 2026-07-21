age = int(input("Please enter your age:"))
VIP_member = (input("Are you a VIP member? (yes/no):")). lower()
eligible = age >=13 and VIP_member == "yes"

print()
print("Age:", age)
print("VIP Member:", VIP_member)
print("Eligible for VIP ticket:", eligible)