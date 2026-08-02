#Raw Strings
print("=" * 40)
print("RAW STRINGS".center(40))
print("=" * 40)
# Variables
normal_path = "C:\\Users\\Noor\\Desktop"
raw_path = r"C:\Users\Noor\Desktop"

normal_text = "Python\nJava\tC++"
raw_text = r"Python\nJava\tC++"

# Display original results
print(f"Normal Path : {normal_path}")
print(f"Raw Path    : {raw_path}")
print(f"Normal Text : {normal_text}")
print(f"Raw Text    : {raw_text}")
# Separator 1
print("-" * 40)
print("Normal String".center(40))
print("-" * 40)
print(normal_path)
print()
print(normal_text)
print()

# Separator 2
print("-" * 40)
print("Raw String".center(40))
print("-" * 40)
print(raw_path)
print()
print(raw_text)
print()

# Success Message
print("Raw Strings demonstrated successfully!")
print("=" * 40)
