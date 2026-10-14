# Task 30: NumPy array slicing
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# slice syntax: [start:end:step], end is excluded
print("arr[1:5]   =", arr[1:5])
print("arr[4:]    =", arr[4:])
print("arr[:4]    =", arr[:4])
print("arr[-3:-1] =", arr[-3:-1])
print("arr[1:5:2] =", arr[1:5:2])
print("arr[::2]   =", arr[::2])
print("reversed   =", arr[::-1])

# 2-D slicing
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print("\nRow 1, columns 1-3:", arr2[1, 1:4])
print("Column 2 of every row:", arr2[:, 2])
print("Sub-matrix rows 0-1, columns 1-3:\n", arr2[0:2, 1:4])
print("First two rows:\n", arr2[:2])
