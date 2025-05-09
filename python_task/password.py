# password.py

while True:
    password = input('Please Enter your password: ')
    length = len(password)

    if not password:
        print('Invalid, Try again!')

    elif length < 8:
        print('Very weak')

    elif length == 8:
        print('Weak')

    elif length <= 16:
        print('Strong')

    else:
        print('Very strong')
        break 