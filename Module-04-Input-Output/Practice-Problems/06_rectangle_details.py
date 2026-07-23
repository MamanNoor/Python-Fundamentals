#1st Heading
print("-" * 40)
print("RECTANGLE DETAILS". center(40))
print("-" * 40)
#User Inputs
length = float(input("Please enter the length:"))
width = float(input("Please enter the width:"))
#Formulas
area = length * width
perimeter = 2 * (length + width)
#Blank Line
print()
#Display Results
print(f"Length     : {length:.2f}")
print(f"Width      : {width:.2f}")
print(f"Area       : {area:.2f}")
print(f"Perimeter  : {perimeter:.2f}")
print("Rectangle calculations completed successfully!")
print("-" * 40)
