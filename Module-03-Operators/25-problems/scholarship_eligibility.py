marks = int(input("Please enter your marks:"))
attendance = int(input("Please enter your attendence percentage:"))
eligible_for_scholarship = marks >= 90 and attendance >= 75
print()
print("Marks:", marks)
print("Attendence:", attendance)
print("Eligible for Scholarship:", eligible_for_scholarship)