
 # MortgageCalculator


print('A Mortgage Calculator: ')

principal_Amount = float(input('Please Enter the Principal Amount: '))

annual_Interest_Rate = float(input('Please Enter the Annual Interest Rate: '))

duration_In_Years = float(input('Please Enter the Duration In Years: '))


MONTHLY_RATE = float(annual_Interest_Rate / 100 / 12)
DURATION_IN_MONTHS = float(duration_In_Years * 12)


MONTHLY_PAYMENT = float(principal_Amount * (MONTHLY_RATE * (1 + MONTHLY_RATE) ** DURATION_IN_MONTHS) / ((1 + MONTHLY_RATE) ** DURATION_IN_MONTHS - 1))

print(f'The Monthly payment is:  ${MONTHLY_PAYMENT:.2f}')



