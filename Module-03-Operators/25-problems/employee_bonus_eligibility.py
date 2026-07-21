performance_rating = (input("Please enter performance rating(Excellent/Good/Average):"))
work_experience = int(input("Please enter years of experience:"))
eligible = performance_rating == "Excellent" or work_experience >= 5

print()
print("Performance:", performance_rating)
print("Experience:", work_experience)
print("Eligible for Bonus:", eligible)