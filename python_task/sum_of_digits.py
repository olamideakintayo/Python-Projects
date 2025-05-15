#sum_of_digits.py

def sum_digits(number):
    total = 0
    while number >= 1 and number <= 10_000:
        digit = number % 10
        total = total + digit
        number = number // 10
    return total

number = int(input("Enter a number: "))
print(f"The Sum of {number} = {sum_digits(number)}")
