# 1st Heading
print("=" * 50)
print("PALINDROME CHECKER".center(50))
print("=" * 50)
# User Input
original_text = input("Please enter a word:")
# Length of the original text
length_of_text = len(original_text)
# Reversed text
reversed_text = original_text[::-1]
# Condition for Palindrome
is_palindrome = original_text == reversed_text
# Display Results
print("-" * 50)
print("Palindrome Result".center(50))
print("-" * 50)
print(f"Original Text : {original_text}")
print(f"Length        : {length_of_text}")
print(f"Reversed Text : {reversed_text}")
print(f"Palindrome    : {is_palindrome}")
print()
# if else conditions
if is_palindrome:
    print("Palindrome!")
else:
    print("Not a Palindrome!")
print("=" * 50)


