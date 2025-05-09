# countdown.py

n = 0

while numbers < 1:
	numbers = int(input('Enter a positive number: '))
	if numbers < 1:
		print('Please Enter a positive number greater than 0.')
			
while numbers > 0:
	print(numbers)
	numbers = numbers - 1
print('Blast Off!!')