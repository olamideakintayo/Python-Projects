#multiplication.py

def multiply(number1, number2):
    result = 0
    negative = False
    
    if number1 < 0:
        number1 = -number1
        negative = not negative
    
    if number2 < 0:
        number2 = -number2
        negative = not negative
    
    for _ in range(number2):
        result = result + number1
    
    if negative:
        result = -result
    
    return result
	


print(multiply(-4, 5))