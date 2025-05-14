#side_by_side_triangle_patterns

for row in range(1, 11):
    for column in range(row):
        print('*', end='')
    for space in range(10 - row):
        print(' ', end='')

    print('   ', end='')

    for column in range(11 - row):
        print('*', end='')
    for space in range(row - 1):
        print(' ', end='')

    print('   ', end='')

    for space in range(row - 1):
        print(' ', end='')
    for column in range(11 - row):
        print('*', end='')

    print('   ', end='')

    for space in range(10 - row):
        print(' ', end='')
    for column in range(row):
        print('*', end='')

    print()
