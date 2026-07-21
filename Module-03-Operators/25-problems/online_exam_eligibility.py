course_completed = (input("Have you completed the course? (yes/no):")).lower()
exam_fee = (input("Have you paid the exam fee? (yes/no):")). lower()
eligible= course_completed == "yes" and exam_fee == "yes"

print()
print("Course Completed:", course_completed)
print("Exam Fee Paid:",exam_fee)
print("Eligible for Exam:", eligible)