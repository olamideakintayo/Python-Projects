#multiplication_table.py

print("    ", end="")
for i in range(1, 10):
    print(f"{i:>4}", end="")
print("\n" + "-" * 41)

for row in range(1, 10):
    print(f"{row:>2} |", end="")  
    for col in range(1, 10):
        print(f"{row * col:>4}", end="")
    print()
