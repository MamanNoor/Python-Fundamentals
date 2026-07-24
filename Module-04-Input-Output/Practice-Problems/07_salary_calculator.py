#1st Heading
print("-" * 40)
print("SALARY CALCULATOR". center(40))
print("-" * 40)
#User Inputs
employee_name = (input("Please enter employee name:"))
hours_worked = float(input("Please enter hours worked:"))
hourly_rate = float(input("Please enter hourly rate:"))
#Formula
salary = hours_worked * hourly_rate
#Blank line
print()
#Display Results
print(f"Employee Name  : {employee_name}")
print(f"Hours Worked   : {hours_worked:.2f}")
print(f"Hourly Rate    : {hourly_rate:.2f}")
print(f"Salary         : {salary:.2f}")
print("Salary calculated successfully!")
print("-" * 40)
