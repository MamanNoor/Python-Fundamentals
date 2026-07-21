age = int(input("Please enter your age:"))
has_stable_job = (input("Do you have a stable job? (yes/no):")). lower()
eligible = age >=21 and has_stable_job == "yes"

print()
print("Age:", age)
print("Stable Job:", has_stable_job)
print("Eligible for Loan:", eligible)

