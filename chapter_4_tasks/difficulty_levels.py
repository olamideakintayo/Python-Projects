# computer_assisted_instruction.py

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
    try:
        difficulty = int(input("Choose difficulty level (1 for single-digit, 2 for two-digit): "))
    except ValueError:
        print("Invalid input. Defaulting to difficulty level 1.")
        difficulty = 1

    while True:
        number1, number2 = random_question(difficulty)
        answer = number1 * number2

        while True:
            user_input = input(f"What is {number1} times {number2}? Or type 'quit' to end the program: ")

            if user_input.lower() == 'quit':
                print('Thanks for Playing')
                return

            try:
                if int(user_input) == answer:
                    print(correct_response() + "\n")
                    break  
                else:
                    print(incorrect_response() + "\n")
            except ValueError:
                print("Please enter a valid number or 'quit'.\n")

multiplication()
