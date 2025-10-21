# Diamond Pattern in Python

n = int(input("Enter number of rows for the upper half: "))

# Upper half of diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Lower half of diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
