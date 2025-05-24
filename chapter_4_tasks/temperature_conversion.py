# temperature_conversion.py

def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f"{'Celsius':>7} {'Fahrenheit':>18}")
print('-' * 26)

for celsius in range(0, 101):
    f = fahrenheit(celsius)
    print(f"{celsius:5} {f:14.1f}")
 