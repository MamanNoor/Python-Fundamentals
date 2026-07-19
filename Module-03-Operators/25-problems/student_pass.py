marks = int(input("Please enter your marks:"))
attendance = int(input("Please enter your attendance:"))
is_pass = marks >= 50 and attendance >= 75

print("Marks:", marks)
print("Attendance:", attendance)
print("Passed:", is_pass )
