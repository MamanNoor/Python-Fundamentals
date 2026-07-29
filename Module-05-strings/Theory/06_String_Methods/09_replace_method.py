#Replace methods
print("-" * 40)
print("REPLACE METHODS".center(40))
print("-" * 40)
#Variables
name = "Noor"
city = "Peshawar"
quote = "Python is easy"
#Display Original Results
print(f"Name               : {name}")
print(f"City               : {city}")
print(f"Quote              : {quote}")
#Separator 1(replace)
print("-" * 40)
print("replace() Method".center(40))
print("-" * 40)
print(f"replace() Noor     : {name.replace("Noor","Mamoona")}")
print(f"replace() Peshawar : {city.replace("Peshawar", "Islamabad")}")
print(f"replace Python     : {quote.replace("Python", "Programming")}")
print()
print(f"Original Name      : {name}")
print(f"Original City      : {city}")
print(f"Original Quote     : {quote}")
print()
#Bonus Variable
print("-" * 40)
print("replace() Method with count".center(40))
print("-" * 40)
text = "apple apple apple"
#Bonus Result
print(f"Original Text      : {text}")
print(f"Replace text       :  {text.replace("apple", "Python", 2)}")
print()
print("replace() Method demonstrated successfully!")
print("=" * 40)

