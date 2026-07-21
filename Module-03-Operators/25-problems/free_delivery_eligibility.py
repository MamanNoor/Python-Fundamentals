order_amount = int(input("Please enter your order amount:"))
premium_member = (input("Are you a premium member? (yes/no):")). lower()
free_delivery = order_amount >=1000 or premium_member == "yes"

print()
print("Order Amount:", order_amount)
print("Premium Member:", premium_member)
print("Free Delivery:", free_delivery)
