# 1st Heading
print("=" * 50)
print("Text Analyzer".center(50))
print("=" * 50)
# User Input
text = input("Please enter Sentence/Paragraph.")
# Character analysis
no_of_characters = len(text)
# Word analysis
splitted_words = text.split()
no_of_words = len(splitted_words)
# Space analysis
no_of_spaces = text.count(" ")
# Letter analysis
no_of_upper = 0
no_of_lower = 0

for character in text:

    if character.isupper():
        no_of_upper += 1

    if character.islower():
        no_of_lower += 1
# Python membership check
python_in_text = "Python" in text

# Display Results
print()
print("-" * 50)
print("TEXT ANALYSIS RESULTS".center(50))
print("-" * 50)
print(f"Text              : {text}")
print(f"Characters        : {no_of_characters}")
print(f"Words             : {no_of_words}")
print(f"Spaces            : {no_of_spaces}")
print(f"Uppercase Letters : {no_of_upper}")
print(f"Lowercase Letters : {no_of_lower}")
print(f"Contains 'Python' : {python_in_text}")
print()
print("-" * 50)
print("ANALYSIS COMPLETE".center(50))
print("-" * 50)
