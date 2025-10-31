# Square border pattern
n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        # Print star for first/last row or first/last column
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line
