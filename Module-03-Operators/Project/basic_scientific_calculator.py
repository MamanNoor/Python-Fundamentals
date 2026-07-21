#Heading
print("=" * 40)
print("BASIC SCIENTIFIC CALCULATOR". center(40))
print("=" *40)

#User Input
first_number = float(input("Please enter the first number:"))
second_number = float(input("Please enter the second number:"))

#Calculations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
modulus = first_number % second_number
exponent = first_number ** second_number

#Print Heading
print("=" * 40)
print("RESULTS". center(40))
print("=" * 40)

#Display the Result
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponent:", exponent)