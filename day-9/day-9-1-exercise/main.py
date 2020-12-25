student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#Function to convert student scores to grades
def convert_scores_to_grades(score):
	if score <= 70:
		return "Fail"
	elif score <= 80:
		return "Acceptable"
	elif score <= 90:
		return "Exceeds Expectations"
	else:
		return "Outstanding"


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
	student_grades[student] = convert_scores_to_grades(student_scores[student])
    

# 🚨 Don't change the code below 👇
print(student_grades)





