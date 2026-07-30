#Split methods
print("-" * 40)
print("SPLIT METHODS".center(40))
print("-" * 40)
#Varaibles
full_name = "Noor Mamoona"
languages = "Python Java C++"
email = "mamoonaa.noor@gmail.com"
#Display Originl Results
print(f"Full Name             : {full_name}")
print(f"Languages             : {languages}")
print(f"Email                 : {email}")
#Separator 1(split)
print("-" * 40)
print("split() Method".center(40))
print("-" * 40)
print(f"split Full Name       : {full_name.split()}")
print(f"split Languages       : {languages.split()}")
print(f"split Email           : {email.split("@")}")
print(f"Original Full Name    : {full_name}")
print(f"Original Languages    : {languages}")
print(f"Original Email        : {email}")
print()
print("split() Method demonstrated successfully!")
print("=" * 40)
