#ROI.py

 
investment_amount = float(input('Please Enter the Investment Amount: '))
number_of_investment_years = int(input('Please Enter the Number of Investment Years: '))
interest_rate = float(input('Please Enter the Interest Rate: '))
 
interest_rate = interest_rate / 100 

for number in range(1, number_of_investment_years+1):
	year_amount = investment_amount * (1 + interest_rate) ** number
	print(f'The Yearly Amount for year {number} is  ${year_amount:,.2f}  at %{interest_rate} interest rate')