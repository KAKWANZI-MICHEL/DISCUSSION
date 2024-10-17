#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 


def calculate_grade(percentage):

  if percentage >= 90:
    return "A"
  elif percentage >= 80:
    return "B"
  elif percentage >= 70:
    return "C"
  elif percentage >= 60:
    return "D"
  elif percentage >= 50:
    return "E"
  else:
    return "Fail" 


def grade_students():

  num_students = int(input("Enter the number of students: "))

  for i in range(num_students):
    percentage = float(input(f"Enter the percentage for student   {i + 1}: "))
    grade = calculate_grade(percentage)
    print(f"Student {i + 1} grade: {grade}")

grade_students()


