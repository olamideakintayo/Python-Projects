#nested_control_loop

largest = None
second_largest = None

for _ in range(10):
    num = float(input("Enter a number: "))
    
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    else:
        if second_largest is None or num > second_largest:
            second_largest = num

print(f"The largest value is: {largest}")
print(f"The second largest value is: {second_largest}")
