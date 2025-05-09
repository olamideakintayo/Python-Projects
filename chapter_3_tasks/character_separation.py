#character_separation


num = int(input("Enter a five-digit integer: "))

for i in range(5):
    digit = num // (10 ** (4 - i))
    num = num % (10 ** (4 - i))

    if i < 4:
        print(digit, end="   ")
    else:
        print(digit)
