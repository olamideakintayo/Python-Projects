# arbitrary_argument_list

def product(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(product(2, 3))               
print(product(4, 5, 6, 7, 8, 9, 10))           
print(product(1, 2, 3, 4, 5))      
print(product(10, 100))                 