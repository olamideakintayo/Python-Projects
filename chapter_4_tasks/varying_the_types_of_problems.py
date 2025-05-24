# varying_the_types_of_problems.py

import random

def random_question(difficulty):
    if difficulty == 1:
        return (random.randint(1, 9), random.randint(1, 9))
    elif difficulty == 2:
        return (random.randint(10, 99), random.randint(10, 99))
    else:
        print("Invalid difficulty. Defaulting to level 1.")
        return (random.randint(1, 9), random.randint(1, 9))

def correct_response():
    return random.choice([
        "Very good!",
        "Nice work!",
        "Keep up the good work!"
    ])

def incorrect_response():
    return random.choice([
        "No. Please try again.",
        "Wrong. Try once more.",
        "No. Keep trying."
    ])

def get_problem_type():
    print("Choose the type of problem:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Random mix")
    choice = input("Enter choice (1-5): ")
    return int(choice) if choice.isdigit() and 1 <= int(choice) <= 5 else 5

def generate_problem(difficulty, problem_type):
    num1, num2 = random_question(difficulty)

    if problem_type == 5:
        problem_type = random.randint(1, 4)

    if problem_type == 1:
        question = f"What is {num1} + {num2}? "
        answer = num1 + num2
    elif problem_type == 2:
        question = f"What is {num1} - {num2}? "
        answer = num1 - num2
    elif problem_type == 3:
        question = f"What is {num1} * {num2}? "
        answer = num1 * num2
    elif problem_type == 4:
        # Avoid divide by zero and ensure integer result
        while num2 == 0 or num1 % num2 != 0:
            num1, num2 = random_question(difficulty)
        question = f"What is {num1} / {num2}? "
        answer = num1 // num2
    else:
        question = f"What is {num1} * {num2}? "
        answer = num1 * num2

    return question, answer

def multiplication():
    difficulty_input = input("Choose difficulty level (1 = single-digit, 2 = two-digit): ")
    difficulty = int(difficulty_input) if difficulty_input.isdigit() else 1

    problem_type = get_problem_type()

    while True:
        question, answer = generate_problem(difficulty, problem_type)

        while True:
            user_input = input(question + "Or type 'quit' to end: ")

            if user_input.lower() == 'quit':
                print("Thanks for playing!")
                return

            if user_input.isdigit():
                if int(user_input) == answer:
                    print(correct_response() + "\n")
                    break
                else:
                    print(incorrect_response() + "\n")
            else:
                print("Please enter a valid number or 'quit'.\n")

multiplication()
