#approximating_themathematical_expression_e

e_estimate = 1
factorial = 1

for number in range(1, 10):
    factorial *= number
    e_estimate += 1 / factorial

print(f"Estimated value of e after 10 terms: {e_estimate}")
