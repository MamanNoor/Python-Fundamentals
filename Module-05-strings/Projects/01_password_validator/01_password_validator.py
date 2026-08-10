# Password Validator

# 1st Heading

print("=" * 50)
print("PASSWORD VALIDATOR".center(50))
print("=" * 50)

# User Input

password = input("Please Enter Password: ")

# Condition for at least 8 characters

has_valid_length = len(password) >= 8

# Character Validation

has_digit = False
has_upper = False
has_lower = False

# Check Each Character

for character in password:

# Condition for at least one digit

    if character.isdigit():
        has_digit = True

# Condition for at least one uppercase letter

    if character.isupper():
        has_upper = True

# Condition for at least one lowercase letter

    if character.islower():
        has_lower = True

# Condition for no spaces

has_no_spaces = " " not in password

# Valid

valid = has_valid_length and has_digit and has_upper and has_lower and has_no_spaces

# Display Results

print("-" * 50)
print("VALIDATION RESULT".center(50))
print("-" * 50)

print(f"Password       : {password}")
print(f"Length         : {len(password)}")
print(f"Valid Length   : {has_valid_length}")
print(f"Contains Digit : {has_digit}")
print(f"Contains Upper : {has_upper}")
print(f"Contains Lower : {has_lower}")
print(f"No Space       : {has_no_spaces}")

print()

if valid:
    print("Valid Password!")
else:
    print("Invalid Password!")

print("=" * 50)
