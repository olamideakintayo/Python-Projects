# highest_score.py

number_of_students = int(input('Please Enter the Number of Students: '))
highest_score = -1 
top_student_name = ''

for counter in range(number_of_students):
    student_name = str(input('Please Enter the Student Name: '))
    student_score = int(input('Please Enter the Student Score: '))
    
    if student_score > highest_score:
        highest_score = student_score
        top_student_name = student_name

print(f"\n{top_student_name} has the highest score of {highest_score}.")
