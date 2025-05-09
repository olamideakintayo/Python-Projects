#tables_of_squares_and_cubes

print('number\tsquare\tcube')

for number in range(6):
    square = number ** 2
    cube = number ** 3
    print(f'{number}\t{square}\t{cube}')

print(f"{'number':>6}\t{'square':>6}\t{'cube':>6}")

for number in range(6):
    square = number ** 2
    cube = number ** 3
    print(f"{number:>6}\t{square:>6}\t{cube:>6}")

