# Task 37: NumPy splitting arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# array_split returns a list of arrays
parts = np.array_split(arr, 3)
print(parts)
print("first part:", parts[0])

# Uneven split: array_split adjusts, split would raise an error
print(np.array_split(arr, 4))
try:
    np.split(arr, 4)
except ValueError as e:
    print("np.split error:", e)

# Split a 2-D array
m = np.arange(1, 13).reshape(4, 3)
print("\nsplit rows into 2:")
for part in np.array_split(m, 2):
    print(part)
print("split columns into 3:")
for part in np.array_split(m, 3, axis=1):
    print(part.ravel())

# hsplit and vsplit
print("hsplit:", [p.ravel() for p in np.hsplit(m, 3)])
print("vsplit:", [p.shape for p in np.vsplit(m, 2)])

# Split at given positions
print(np.split(arr, [2, 4]))
