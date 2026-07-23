#1st Heading
print("-" * 40)
print("TEMPERATURE CONVERTER". center(40))
print("-" * 40)
#User Input
celsius = float(input("Please enter the temperature in celsius:"))
#Formula
fahrenheit = (celsius * 9 / 5) + 32
#Blank Line
print()
#Display Results
print(f"Celsius    : {celsius:.2f}°C")
print(f"Fahrenheit : {fahrenheit:.2f}°F ")
print("Temperature converted successfully!")
print("-" * 40)
