#world_population.py

current_population = 8_000_000_000
growth_rate = 0.011

doubling_year = None
quadrupling_year = None

print(f"{'Year':<5} {'Population':<15} {'Increase':<15}")

for year in range(1, 101):
    population = current_population * (1 + growth_rate)**year
    increase = population - current_population * (1 + growth_rate)**(year - 1)
    
    print(f"{year:<5} {population:,.0f} {increase:,.0f}")
    
    if population >= 2 * current_population and doubling_year is None:
        doubling_year = year
    if population >= 4 * current_population and quadrupling_year is None and year > doubling_year:
        quadrupling_year = year

print(f"\nThe population will double in year {doubling_year}.")
print(f"The population will quadruple in year {quadrupling_year}.")
