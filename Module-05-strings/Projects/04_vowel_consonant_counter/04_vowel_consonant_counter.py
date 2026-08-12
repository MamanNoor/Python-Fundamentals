# 1st Heading
print("=" * 50)
print("VOWEL & CONSONANT COUNTER".center(50))
print("=" * 50)
text = input("Please enter a Sentence/Paragrpah :")
# Intially counters
letters = 0
vowels = 0
consonants = 0
digits = 0
spaces = 0

a = 0
e = 0
i = 0
o = 0
u = 0
# Checking each charcter

for character in text:

    # Letter checking

    if character.isalpha():
        letters += 1

        # Vowel checking

        if character.lower() in "aeiou":
            vowels += 1

            # Individual vowel checking

            if character.lower() == "a":
                a += 1

            elif character.lower() == "e":
                e += 1

            elif character.lower() == "i":
                i += 1

            elif character.lower() == "o":
                o += 1

            elif character.lower() == "u":
                u += 1

        # Consonant checking

        else:
            consonants += 1

    # Digit checking

    elif character.isdigit():
        digits += 1
    elif character == " ":
        spaces += 1
# Display Results

print()
print("-" * 50)
print("TEXT ANALYSIS RESULTS".center(50))
print("-" * 50)

print(f"Text        : {text}")
print(f"Letters     : {letters}")
print(f"Vowels      : {vowels}")
print(f"Consonants  : {consonants}")
print(f"Digits      : {digits}")
print(f"Spaces      : {spaces}")
print()
print("VOWEL BREAKDOWN".center(50))
print("-" * 50)

print(f"A           : {a}")
print(f"E           : {e}")
print(f"I           : {i}")
print(f"O           : {o}")
print(f"U           : {u}")

print()
print("-" * 50)
print("ANALYSIS COMPLETE".center(50))
print("-" * 50)
