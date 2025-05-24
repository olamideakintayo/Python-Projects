# the_tortoise_and_the_hare.py

import random
import time

def tortoise_move():
    random_number = random.randint(1, 10)
    if random_number <= 5:
        return 3
    elif random_number <= 7:
        return -6
    else:
        return 1

def hare_move():
    random_number = random.randint(1, 10)
    if random_number <= 2:
        return 0
    elif random_number <= 4:
        return 9
    elif random_number == 5:
        return -12
    elif random_number <= 8:
        return 1
    else:
        return -2

def print_track(tortoise_position, hare_position, finish_line=70):
    track = [' '] * finish_line
    if tortoise_position == hare_position:
        ouch = "OUCH!!!"
        start_index = tortoise_position - 1
        for index, character in enumerate(ouch):
            if start_index + index < finish_line:
                track[start_index + index] = character
    else:
        track[tortoise_position - 1] = 'T'
        track[hare_position - 1] = 'H'
    print("".join(track))

def race():
    tortoise_position = 1
    hare_position = 1
    finish_line = 70

    print("BANG !!!!!")
    print("AND THEY'RE OFF !!!!!")

    while True:
        time.sleep(1)

        tortoise_position += tortoise_move()
        hare_position += hare_move()

        if tortoise_position < 1:
            tortoise_position = 1
        if hare_position < 1:
            hare_position = 1
        if tortoise_position > finish_line:
            tortoise_position = finish_line
        if hare_position > finish_line:
            hare_position = finish_line

        print_track(tortoise_position, hare_position, finish_line)

        if tortoise_position == finish_line and hare_position == finish_line:
            print("It's a tie!")
            break
        elif tortoise_position == finish_line:
            print("TORTOISE WINS!!! YAY!!!")
            break
        elif hare_position == finish_line:
            print("HARE WINS. Yuch.")
            break

race()
