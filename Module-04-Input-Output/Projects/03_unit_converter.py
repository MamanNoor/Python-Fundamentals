# 1st Heading
print("=" * 40)
print("UNIT CONVERTER".center(40))
print("=" * 40)

# User Input
kilometers = float(input("Please enter distance in kilometers: "))

# Formula
miles = kilometers * 0.621371

# Blank Line
print()

# Display Results
print(f"Kilometers : {kilometers:.2f} km")
print(f"Miles      : {miles:.2f} mi")

print()
print("Unit converted successfully!")
print("=" * 40)