# 1st Heading
print("-" * 40)
print("DISCOUNT CALCULATOR".center(40))
print("-" * 40)

# User Inputs
product_name = input("Please enter product name: ")
original_price = float(input("Please enter original price: "))
discount_percentage = float(input("Please enter discount percentage: "))

# Formulas
discount_amount = original_price * discount_percentage / 100
final_price = original_price - discount_amount

# Blank Line
print()

# Display Results
print(f"Product Name        : {product_name}")
print(f"Original Price      : ${original_price:.2f}")
print(f"Discount Percentage : {discount_percentage:.2f}%")
print(f"Discount Amount     : ${discount_amount:.2f}")
print(f"Final Price         : ${final_price:.2f}")

print()
print("Discount calculated successfully!")
print("-" * 40)