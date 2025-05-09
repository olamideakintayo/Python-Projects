#factorial.py

n = int(input("Enter a nonnegative integer: "))

if n < 0:
    print("Invalid for negative integers.")
else:
    factorial = 1
    for number in range(1, n + 1):
        factorial *= number
    print(f"The factorial of {n} is {factorial}")
