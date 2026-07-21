correct_username = "Maman"
correct_password = "maman123"

username = (input("Please enter the correct username:"))
password = (input("Please enter the correct password:"))

login_access = username == correct_username and password == correct_password

print()
print("Username:", username)
print("Password:", password)
print("Login Access:", login_access)