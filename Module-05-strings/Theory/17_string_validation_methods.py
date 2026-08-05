# String validation methods
print("=" * 40)
print("STRING VALIDATION METHODS".center(40))
print("=" * 40)
text = "Python"
number = "2026"
alpha_numeric = "Python123"
lower_text = "python"
upper_text = "PYTHON"
title_text = "Python Programming"
space_text = "  "
# Display Original Values
print(f"Text : {text}")
print(f"Number : {number}")
print(f"Alpha Numeric : {alpha_numeric}")
print(f"Lower Text : {lower_text}")
print(f"Upper Text : {upper_text}")
print(f"Title Text : {title_text}")
print(f'Space Text : "{space_text}"')
print()
#Separator 1 
print("-" * 40)
print("isalpha()".center(40))
print("-" * 40)
print(f"{text}.isalpha() : {text.isalpha()}")
print(f"{alpha_numeric}.isalpha() : {alpha_numeric.isalpha()}")
print()
#Separator 2
print("-" * 40)
print("isdigit()".center(40))
print("-" * 40)
print(f"{number}.isdigit() : {number.isdigit()}")
print(f"{text}.isdigit() : {text.isdigit()}")
print() 
#Separator 3
print("-" * 40)
print("isalnum()".center(40))
print("-" * 40)
print(f"{alpha_numeric}.isalnum() : {alpha_numeric.isalnum()}")
print(f"{title_text}.isalnum() : {title_text.isalnum()}")
print()
#Separator 4
print("-" * 40)
print("islower()".center(40))
print("-" * 40)
print(f"{lower_text}.islower() : {lower_text.islower()}")
print(f"{text}.islower() : {text.islower()}")
print()
#Separator 5
print("-" * 40)
print("isupper()".center(40))
print("-" * 40)
print(f"{upper_text}.isupper() : {upper_text.isupper()}")
print(f"{text}.isupper() : {text.isupper()}")
print()
#Separator 6
print("-" * 40)
print("istitle()".center(40))
print("-" * 40)
print(f"{title_text}.istitle() : {title_text.istitle()}")
print(f"{lower_text}.istitle() : {lower_text.istitle()}")
print()
#Separator 7
print("-" * 40)
print("isspace()".center(40))
print("-" * 40)
print(f'"{space_text}".isspace() : {space_text.isspace()}')
print(f"{text}.isspace() : {text.isspace()}")
print()
print("String Validation Methods demonstrated successfully!")
print("=" * 40)


