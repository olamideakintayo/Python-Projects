# guess_the_number

import random

def guess_the_number():
    print("Guess my number between 1 and 1000 with the fewest guesses:")
    number = random.randint(1, 1000)
    guess = 0

    while guess != number:
        guess = int(input("Your guess: "))

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")


play_again = "yes"
while play_again == "yes":
    guess_the_number()
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "no":
    	print("Good Bye!! Have a Nice Day!")