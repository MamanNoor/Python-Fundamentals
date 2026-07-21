age = int(input("Please enter your age:"))
student = (input("Are you a student? (yes/no):")). lower()
store_member = (input("Are you a store member? (yes/no)")). lower()
discount = student == "yes" or age >=60 or store_member == "yes"


print()
print("Age:", age)
print("Student:", student)
print("Store member:", store_member)
print("Eligible for discount:", discount)
