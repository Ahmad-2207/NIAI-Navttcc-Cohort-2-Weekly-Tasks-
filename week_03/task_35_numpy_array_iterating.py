# Task 35: NumPy array iteration
import numpy as np

# 1-D
for x in np.array([1, 2, 3]):
    print(x, end=" ")
print()

# 2-D: iterating gives rows
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
for row in arr2:
    print("row:", row)

# Visit every scalar
for row in arr2:
    for x in row:
        print(x, end=" ")
print()

# np.nditer visits every element, whatever the dimension
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr3):
    print(x, end=" ")
print()

# Iterate with a different dtype
for x in np.nditer(arr2, flags=["buffered"], op_dtypes=["S"]):
    print(x, end=" ")
print()

# ndenumerate gives the index as well
for idx, x in np.ndenumerate(arr2):
    print(idx, x)

# Step through with nditer
for x in np.nditer(arr2[:, ::2]):
    print(x, end=" ")
print()
