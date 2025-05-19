#categorize_numbers

def categorize_numbers(*numbs, divisible_number_by=2):
    divisible_numbers = []
    
    for num in numbs:
        if isinstance(num, (int, float)) and num % divisible_number_by == 0:
            divisible_numbers.append(num)
    
    if divisible_numbers:
        return divisible_numbers
    else:
        return "No divisible number found"
