# computer_assisted_instruction.py

import random

def random_question():
    return (random.randint(1, 9), random.randint(1, 9))

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
                print("Congratulations!! You're correct!\n")
                break  
            else:
                print("You're wrong, Please try again.\n")

multiplication()
