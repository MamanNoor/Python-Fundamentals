student = (input("Are you a student?(yes/no):")). lower()
library_member = (input("Are you a library member? (yes/no):")). lower()

can_borrow = student == "yes" or library_member == "yes"

print()
print("Student:", student)
print("Library member:", library_member)
print("Can Borrow Books:", can_borrow)