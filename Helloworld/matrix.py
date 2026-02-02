# Python program to print a list in matrix format

def print_matrix(lst, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(lst[i * cols + j], end=" ")
        print()

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows, cols = 3, 3   # 3x3 matrix
print_matrix(my_list, rows, cols)