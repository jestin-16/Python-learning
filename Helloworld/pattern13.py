n=int(input("enter numer:"))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))