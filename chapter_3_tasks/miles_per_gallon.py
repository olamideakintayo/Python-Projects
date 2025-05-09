#miles_per_gallon.py

total_miles = 0
total_gallons = 0

while True:
    gallons = float(input("Enter gallons driven (or -1 to stop): "))
    if gallons == -1:
        break
    
    miles = float(input("Enter miles used: "))
    if miles == -1:
        break
    
    mpg = miles / gallons
    print(f'Miles per gallon for this tank was: {mpg:.2f}')
    
    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f'The overall average miles per gallon: {overall_mpg:.2f}')
else:
    print('No valid data entered.')
