#1st Heading
print("-" * 40)
print("SHOPPING BILL". center(40))
print("-" * 40)
#User Inputs
product_name = (input("Please enter the product name:"))
price = float(input("Please enter the price:"))
quantity = int(input("Please enter the quantity:"))
#Formula
total = price * quantity
#Blank Line
print()
#Display Results
print(f"Product  : {product_name}")
print(f"Price    : ${price:.2f}")
print(f"Quantity : {quantity}")
print()
print(f"Total    : ${total:.2f}")
print()
print("Thank you for shopping with us!")
print("-" * 40)