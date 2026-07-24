# 1st Heading
print("-" * 40)
print("SIMPLE INTEREST CALCULATOR".center(40))
print("-" * 40)

# User Inputs
principal = float(input("Please enter principal amount: "))
rate = float(input("Please enter annual interest rate (%): "))
time = float(input("Please enter time (years): "))

# Formulas
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

# Blank Line
print()

# Display Results
print(f"Principal Amount : ${principal:.2f}")
print(f"Interest Rate    : {rate:.2f}%")
print(f"Time             : {time:.2f} years")
print(f"Simple Interest  : ${simple_interest:.2f}")
print(f"Total Amount     : ${total_amount:.2f}")

print()
print("Interest calculated successfully!")
print("-" * 40)