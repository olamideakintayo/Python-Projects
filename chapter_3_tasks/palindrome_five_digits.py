
digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0

while True:
    num = int(input("Please Enter a five digit number: "))
    if num < 10000 or num > 99999:
        print('Error! Please enter a five digit number')
    else:
        digit1 = num // 10000
        digit2 = (num // 1000) % 10
        digit3 = (num // 100) % 10
        digit4 = (num // 10) % 10
        digit5 = num % 10
        if digit1 == digit5 and digit2 == digit4:
            print("This is a palindrome number")
        else:
            print("This is not a palindrome number")
        break	
	
	
