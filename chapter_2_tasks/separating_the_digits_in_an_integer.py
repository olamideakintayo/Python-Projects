#separating_the_digits_in_an_integer

num = int(input("Enter a five-digit integer: "))

first_digit = num // 10000  
second_digit = (num // 1000) % 10  
third_digit = (num // 100) % 10  
fourth_digit = (num // 10) % 10  
fifth_digit = num % 10  

print(f"{first_digit}   {second_digit}   {third_digit}   {fourth_digit}   {fifth_digit}")
