# validating_user_input

# Using nested control statements to analyze examination results with input validation

passes = 0 

for student in range(10):
    while True:
        result = input('Enter result (1=pass, 2=fail): ')
        if result in ('1', '2'):
            result = int(result)
            break
        else:
            print('Invalid input. Please enter 1 for pass or 2 for fail.')

    if result == 1:
        passes += 1

failures = 10 - passes

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

