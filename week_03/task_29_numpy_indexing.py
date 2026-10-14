# Task 29: NumPy array indexing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("arr[0]  =", arr[0])
print("arr[2] + arr[3] =", arr[2] + arr[3])
print("arr[-1] =", arr[-1])

# 2-D indexing: arr[row, column]
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd dim, 2nd element of 1st row:", arr2[0, 1])
print("5th element of 2nd row:", arr2[1, 4])
print("Last element of 2nd row:", arr2[1, -1])

# 3-D indexing
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("arr3[0, 1, 2] =", arr3[0, 1, 2])

# Logical (boolean) selection
data = np.array([3, 8, 12, 5, 20, 1])
mask = data > 6
print("mask:", mask)
print("values > 6:", data[mask])
print("even values:", data[data % 2 == 0])

# Fancy indexing with a list of positions
print(data[[0, 2, 4]])
