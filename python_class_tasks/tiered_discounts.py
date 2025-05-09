#tiered_discounts.py

purchase_amount = float(input('Please Enter the purchase amount: '))
	
if purchase_amount >= 1000 and purchase_amount <= 10000:
	discount_rate = 5 / 100
	discount_amount = purchase_amount * (5 / 100)
	total_amount = purchase_amount - discount_amount
	print(f'The Discount Rate is: %{discount_rate}')
	print(f'The Discount is: ${discount_amount:,.2f}')
	print(f'The Amount after discount is: ${total_amount:,.2f}')
	
elif purchase_amount > 10000 and purchase_amount < 50000:
	discount_rate = 10 / 100
	discount_amount = purchase_amount * (10 / 100)
	total_amount = purchase_amount - discount_amount
	print(f'The Discount is: %{discount_amount}')
	print(f'Amount after discount is: ${discount_amount:,.2f}')
	print(f'The Amount after discount is: ${total_amount:,.2f}')

elif purchase_amount > 50000:
	discount_rate = 20 / 100
	discount_amount = purchase_amount * (20 / 100)
	total_amount = purchase_amount - discount_amount
	print(f'The Discount is: %{discount_amount}')
	print(f'Amount after discount is: ${discount_amount:,.2f}')
	print(f'The Amount after discount is: ${total_amount:,.2f}')
		
else:
	print('Invalid Amount')


