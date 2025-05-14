# approximating_the_mathematical_constant_pi

approx_pi = 0
num_terms = 0
target_approximations = [3.14, 3.141, 3.1415, 3.14159]
target_approximations_counter = 0

print(f"{'Terms':>5} {'Approximated Pi':>20}")

for number in range(1, 20000, 2):
    if num_terms % 2 == 0:
        approx_pi += 4 / number
    else:
        approx_pi -= 4 / number
    
    num_terms += 1
    
    print(f"{num_terms:>5} {approx_pi:>20.15f}")
    
    if len(target_approximations) > 0 and round(approx_pi, len(str(target_approximations[vary])) - 2) == target_approximations[0]:
        print(f"Approximation of {target_approximations.pop(target_approximations_counter)} Reached at term {num_terms}")
        if len(target_approximations) == 0:
            break
            
target_approximations_counter += 1
