# guess_the_number_modification.py

import random

def guess_the_number():
    print("Guess my number between 1 and 1000 with the fewest guesses:")
    number = random.randint(1, 1000)
    guess = 0
    guess_count = 0

    while guess != number:
        guess = int(input("Your guess: "))
        guess_count += 1

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")
            print(f"You guessed the number in {guess_count} guesses.")
            if guess_count <= 10:
                print("Either you know the secret or you got lucky!")
            else:
                print("You should be able to do better!")

replay_the_game = "yes"
while replay_the_game == "yes":
    guess_the_number()
    replay_the_game = input("Would you like to play again? (yes/no): ").lower()
    if replay_the_game == "no":
    	print("Good Bye!! Have a Nice Day!")
