# Task 33: NumPy array shape
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("shape:", arr.shape)       # (rows, columns)
print("ndim :", arr.ndim)
print("size :", arr.size)
print("dtype:", arr.dtype)

# 5-D array: the last number is the length of the innermost array
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print("\n5-D array:", arr5)
print("shape:", arr5.shape)
print("axis 4 has", arr5.shape[4], "elements")

# 3-D array
arr3 = np.zeros((2, 3, 4))
print("\n3-D shape:", arr3.shape, "-> 2 blocks, 3 rows, 4 columns")
print("total elements:", arr3.size)
