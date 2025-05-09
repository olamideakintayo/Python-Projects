
age = int(input('Please enter your age: '))

max_heart_rate = 220 - age

lower_target_heart_rate = max_heart_rate * 0.50
upper_target_heart_rate = max_heart_rate * 0.85

print('\nAccording to the American Heart Association (AHA):')
print(f'Your maximum heart rate is: {max_heart_rate} beats per minute.')
print(f'Your target heart rate range is: {lower_target_heart_rate:.1f} - {upper_target_heart_rate:.1f} beats per minute.')
