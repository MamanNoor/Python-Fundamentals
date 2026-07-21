password = (input("Please enter password:"))
strong_password = len(password) >= 8 and "@" in password

print()
print("Password:", password)
print("Strong Password:", strong_password)