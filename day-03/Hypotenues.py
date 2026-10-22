import math

print("=== Hypotenuse Calculator ===")

length = float(input("Enter the first side in metres: "))
height = float(input("Enter the second side in metres: "))

if length > 0 and height > 0:
    answer = math.sqrt(length ** 2 + height ** 2)
    print(f"The hypotenuse is {answer:.2f} metres.")
else:
    print("ERROR: Both sides must be greater than zero.")