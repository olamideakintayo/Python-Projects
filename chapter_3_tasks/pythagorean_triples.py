#pythagorean_triples.py

for side1 in range(1, 21):
    for side2 in range(side1, 21):
        for hypotenuse in range(side2, 21):
            if side1**2 + side2**2 == hypotenuse**2:
                print(f"Pythagorean triple: {side1}, {side2}, {hypotenuse}")

