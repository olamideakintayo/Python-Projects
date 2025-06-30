class Account:
    def __init__(self):
        self.balance = 0

    def withdraw(self):
        print('Account withdraw')

    def deposit(self, amount):
        self.balance += amount


oba = Account()
print(oba.balance)
oba.deposit(10000)
print(oba.balance)



def main():
    scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):
            print(f"inner value: ", inner_value, end='\t')
            print(f"inner index: ", inner_index)

            print(f"inner list: ", score, end='\t')
            print(f"inner list index: ", index)

main()

days_per_month = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
for month, days in days_per_month.items():
    print(f"{month}: {days}")
for month_name in days_per_month.keys():
    print(month_name)
for number_of_days in days_per_month.values():
    print(number_of_days)

number_dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
del number_dic['four']
print(number_dic)

number_dic.pop('two')
print(number_dic)

print(number_dic)
number_dic.get('ten', 'not found')


def convert_numbers_to_words(number):
    number_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    return number_words.get(number, 'invalid number')

number = int(input("Enter a number between 1 and 10: "))
number_word = convert_numbers_to_words(number)
print(number_word)


months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 2, 'October': 10, 'November': 11, 'December': 12 }
months2 = {number: name for name, number in months.items()}
print(months2)