# Login Authentication System

# Correct login credentials
correct_username = "admin"
correct_password = "python123"

# User input
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Check login
login_successful = username == correct_username and password == correct_password

# Output
print()
print("Username:", username)
print("Password:", password)
print("Login Successful:", login_successful)