A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

while B != 0:
    R = A % B
    A = B
    B = R

print("HCF =", A)