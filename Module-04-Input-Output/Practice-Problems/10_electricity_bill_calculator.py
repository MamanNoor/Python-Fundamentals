# 1st Heading
print("-" * 40)
print("ELECTRICITY BILL".center(40))
print("-" * 40)

# User Inputs
customer_name = input("Please enter customer name: ")
units_consumed = float(input("Please enter units consumed: "))
cost_per_unit = float(input("Please enter cost per unit: "))

# Formula
bill = units_consumed * cost_per_unit

# Blank Line
print()

# Display Results
print(f"Customer Name  : {customer_name}")
print(f"Units Consumed : {units_consumed:.2f}")
print(f"Cost Per Unit  : ${cost_per_unit:.2f}")
print(f"Total Bill     : ${bill:.2f}")

print()
print("Bill calculated successfully!")
print("-" * 40)