#binary_to_decimal_conversion

binary_str = input("Enter a binary number: ")

decimal_value = 0
binary_length = len(binary_str)

for number in range(binary_length):
    digit = int(binary_str[binary_length - 1 - number])
    decimal_value += digit * (2 ** number)

print("Decimal equivalent:", decimal_value)
