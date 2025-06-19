import random
numbers = []


def random_numbers():
    for i in range(10):
        numbers.append(random.randint(1, 50))
    return numbers


def length_of_numbers():
    count = 0
    for i in numbers:
        count = count + 1
    return count


def even_positions():
    even_sum = 0
    i = 0
    while i < length_of_numbers():
        if i % 2 == 0:
            even_sum = even_sum + numbers[i]
        i = i + 1
    return even_sum


def odd_positions():
    odd_sum = 0
    i = 0
    while i < length_of_numbers():
        if i % 2 != 0:
            odd_sum = odd_sum + numbers[i]
        i = i + 1
    return odd_sum
   

def multiply_elements_at_third_positions():
    multiply_elements = 1
    i = 0
    while i < length_of_numbers():
        if i % 3 == 0:
            multiply_elements = multiply_elements * numbers[i]
        i = i + 1
    return multiply_elements

def average_of_all_elements():
    sum_of_element = 0
    i = 0
    while i < length_of_numbers():
        sum_of_element = sum_of_element + numbers[i]
        i = i + 1
    return sum_of_element / length_of_numbers()

random_numbers()
print(length_of_numbers())
print(f"The Sum of numbers at even positions are: {even_positions()}")
print(f"The Sum of numbers at odd positions are: {odd_positions()}")
print(f"The answer of all elements at third positions is: {multiply_elements_at_third_positions()}")
print(f"The average of all elements in the list is: {average_of_all_elements()}")