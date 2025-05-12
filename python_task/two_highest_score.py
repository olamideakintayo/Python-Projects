#two_highest_score.py

number_of_students = int(input('Please Enter the Number of Students: '))
first_highest_score = -233 
second_highest_score = -233
first_top_student_name = ''
second_top_student_name = ''

for counter in range(number_of_students):
    student_name = input('Please Enter the Student Name: ')
    student_score = int(input('Please Enter the Student Score: '))
    
    if student_score > first_highest_score:
        second_highest_score = first_highest_score
        second_top_student_name = first_top_student_name
        
        first_highest_score = student_score
        first_top_student_name = student_name

    elif student_score > second_highest_score:
        second_highest_score = student_score
        second_top_student_name = student_name
            
print(f"\n{first_top_student_name} has the highest score of {first_highest_score}.")
print(f"{second_top_student_name} has the second highest score of {second_highest_score}.")
