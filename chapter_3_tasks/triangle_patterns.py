#triangle_patterns.py

for row in range(1, 11):
    for column in range(row):
        print('*', end='')
    print()

print()

for row in range(10, 0, -1):
    for column in range(row):
        print('*', end='')
    print()

print()

for row in range(10):
    for column in range(row):
        print(' ', end='')
    for column in range(10 - row):
        print('*', end='')
    print()

print()

for row in range(1, 11):
    for column in range(10 - row):
        print(' ', end='')
    for column in range(row):
        print('*', end='')
    print()
