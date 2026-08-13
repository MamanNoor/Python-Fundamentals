# 1st Heading

print("=" * 50)
print("TEXT CLEANER & FORMATTER".center(50))
print("=" * 50)

# User Input

text = input("Please enter some text: ")

# Clean text
cleaned_text = " ".join(text.strip().split())

# Text Formatting

lowercase_text = cleaned_text.lower()
uppercase_text = cleaned_text.upper()
title_text = cleaned_text.title()

# Replace Text

formatted_text = cleaned_text.replace("Noor", "NOOR")

# Character Count

number_of_characters = len(cleaned_text)

# Display Results

print()
print("-" * 50)
print("TEXT CLEANING RESULTS".center(50))
print("-" * 50)

print(f"Original Text  : {text}")
print(f"Cleaned Text   : {cleaned_text}")
print(f"Lowercase      : {lowercase_text}")
print(f"Uppercase      : {uppercase_text}")
print(f"Title Case     : {title_text}")
print(f"Formatted Text : {formatted_text}")
print(f"Characters     : {number_of_characters}")

print()
print("-" * 50)
print("CLEANING COMPLETE".center(50))
print("-" * 50)
