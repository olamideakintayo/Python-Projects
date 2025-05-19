#smallest_and_largest_arithmetic

numbers = []
sum_of_numbers = 0
product_of_numbers = 1
smallest_number = 23453 
largest_number = -23453  

for number in range(4):
    num = int(input(f"Enter integer {number+1}: "))
    numbers.append(num)
    sum_of_numbers += num
    product_of_numbers *= num
    if num < smallest_number:
        smallest_number = num
    if num > largest_number:
        largest_number = num

average_of_numbers = sum_of_numbers / 4

print(f"Sum: {sum_of_numbers}")
print(f"Average: {average_of_numbers}")
print(f"Product: {product_of_numbers}")
print(f"Smallest: {smallest_number}")
print(f"Largest: {largest_number}")

