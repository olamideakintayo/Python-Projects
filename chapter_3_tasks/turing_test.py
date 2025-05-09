#turing_test

print("Welcome to the Turing Test Medical Diagnosis System.")

input('What is your problem? ')
response = input('Have you had this problem before (yes or no)? ')

if response.lower() == 'yes':
    print('Well, you have it again.')
elif response.lower() == 'no':
    print('Well, you have it now.')
else:
    print('Sorry, I didn\'t understand your answer.')
