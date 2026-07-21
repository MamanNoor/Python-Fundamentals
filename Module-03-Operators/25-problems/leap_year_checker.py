year = int(input("Please enter year:"))
leap_year =( year % 4 == 0 and year % 100 != 0) or year % 400 == 0
 
print()
print("Year:", year)
print("Leap Year:", leap_year)