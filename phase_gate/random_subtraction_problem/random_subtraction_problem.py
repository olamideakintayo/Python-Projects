# RandomSubtractionProblem.py

import random
import time

total_questions = 10
answer_count = 0

def random_subtraction_problem():
    number1 = random.randint(0, 999)
    number2 = random.randint(0, 999)

    minuend = max(number1, number2)
    subtrahend = min(number1, number2)

    return {
        'question': f"What is {minuend} - {subtrahend}? ",
        'answer': minuend - subtrahend
    }

def question_ask():
    global answer_count
    problem = random_subtraction_problem()
    print(problem['question'])

    attempts_left = 2
    start_time = time.time()

    while attempts_left > 0:
        try:
            user_answer = int(input("Enter your Answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_answer == problem['answer']:
            time_taken = round(time.time() - start_time, 2)
            print(f"Correct! Time taken: {time_taken} seconds")
            answer_count += 1
            return
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Wrong! Try again. Attempts left: {attempts_left}")
            else:
                time_taken = round(time.time() - start_time, 2)
                print(f"Wrong again. The correct answer was {problem['answer']}.")
                print(f"Time taken: {time_taken} seconds")

for _ in range(total_questions):
    question_ask()

print(f"Thank You!! You answered {answer_count} out of {total_questions} correctly. Have a nice Day")
