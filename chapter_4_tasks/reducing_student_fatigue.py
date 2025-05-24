# reducing_student_fatigue.py

# computer_assisted_instruction.py

import random

def random_question():
    return (random.randint(1, 9), random.randint(1, 9))

def correct_response():
    responses = [
        "Very good!",
        "Nice work!",
        "Keep up the good work!"
    ]
    return random.choice(responses)

def incorrect_response():
    responses = [
        "No. Please try again.",
        "Wrong. Try once more.",
        "No. Keep trying."
    ]
    return random.choice(responses)

def multiplication():
    while True:
        number1, number2 = random_question()
        answer = number1 * number2

        while True:
            user_input = input(f"What is {number1} times {number2}? Or type 'quit' to end the program: ")
           
            if user_input.lower() == 'quit':
                print('Thanks for Playing')
                return

            if int(user_input) == answer:
                print(correct_response() + "\n")
                break  
            else:
                print(incorrect_response() + "\n")

multiplication()
