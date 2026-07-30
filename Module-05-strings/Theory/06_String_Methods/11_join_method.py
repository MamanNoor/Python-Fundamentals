#Join Methods
print("-" * 40)
print("JOIN METHODS".center(40))
print("-" * 40)
#Varaibles
name = ["Noor", "Mamoona"]
languages = ["Python", "Java", "C++"]
date = ["20", "08", "2025"]
#Display Originl Results
print(f"Full Name            : {name}")
print(f"Languages            : {languages}")
print(f"Date                 : {date}")
#Separator 1(join)
print("-" * 40)
print("join() Method".center(40))
print("-" * 40)
print(f"join Name            : {" ".join(name)}")
print(f"join Languages       : {(", ").join(languages)}")
print(f"join Date            : {("-").join(date)}")
print(f"Original Name        : {name}")
print(f"Original Languages   : {languages}")
print(f"Original Date        : {date}")
print()
print("join() Method demonstrated successfully!")
print("=" * 40)

