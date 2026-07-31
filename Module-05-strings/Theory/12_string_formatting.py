#String Formatting
print("-" * 40)
print("String Formatting".center(40))
print("-" * 40)
#Variables
name = "Noor"
age = 20
course = "Python"
marks = 95.5
#Display Original Results
print("Name  :", name)
print("Age   :", age)
print("Course:", course)
print("Marks :", marks)
#Separator 1(% Formatting)
print("-" * 40)
print("old style formatting".center(40))
print("-" * 40)
print("My name is %s." % name)   
print("I am %d years old." % age) 
print("I am learning %s." % course) 
print("I scored %.2f marks." % marks)  
#Separator 2(format() Method)
print("-" * 40)
print("format() Method".center(40))
print("-" * 40)
print("My name is {}.".format(name))
print("I am {} years old.".format(age))
print("I am learning {}.".format(course))
print("I scored {:.2f} marks.".format(marks))
print("{0} is learning {1}.".format("Noor","Python"))
#Separator 2(f string)
print("-" * 40)
print("f string".center(40))
print("-" * 40)
print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I am learning {course}.")
print(f"I scored {marks:.2f} marks.")
print()
print("String formatting demonstrated successfully!")
print("=" * 40)

