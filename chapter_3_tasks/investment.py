#investment.py

p = 1000
r = 0.07

for year in range(1, 31):
    amount = p * (1 + r) ** year
    print(f'Amount after {year} year(s): ${amount:.2f}')
