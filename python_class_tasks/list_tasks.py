numbers = [10, 20, 30, 40, 50]
print(numbers[2])

list_of_colors = ["red", "green", "blue"]
list_of_colors[2] = "yellow"
print(list_of_colors)

list_of_colors.append("purple")
print(list_of_colors)

list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers.remove(2)
print(list_of_numbers)

list_of_names = ["Alice", "Bob", "Charlie"]
for i in list_of_names:
    print(len(i))

ascending_order_numbers = [4, 1, 3, 9, 2]
ascending_order_numbers.sort()
print(ascending_order_numbers)

numbers = [2, 5, 6, 7, 8, 9, 12, 16]
def list_of_even_numbers(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
print(list_of_even_numbers(numbers))

a = [1, 2, 3]
b = [4, 5, 6]
combine_numbers = a + b
print(combine_numbers)

a = ["lamb", "kit", "yam", "kings", "dogs", "man"]
new_list = []
for i in a:
    if len(i) > 3:
        new_list.append(i)
print(new_list)