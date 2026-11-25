# Assignment 4: Create arrays and perform addition of two matrices using List and NumPy
import numpy as np

# 1. Matrix addition using nested Python lists
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
]

list_sum = []
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[0])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    list_sum.append(row)

print("Matrix A (List):", matrix_a)
print("Matrix B (List):", matrix_b)
print("Matrix Addition using List:")
for row in list_sum:
    print(row)

# 2. Matrix addition using NumPy arrays
np_a = np.array(matrix_a)
np_b = np.array(matrix_b)
np_sum = np_a + np_b

print("\nMatrix Addition using NumPy:")
print(np_sum)
