# Task 34: NumPy array reshaping
import numpy as np

arr = np.arange(1, 13)

# 1-D to 2-D
print(arr.reshape(4, 3))
print(arr.reshape(2, 6))

# 1-D to 3-D
print(arr.reshape(2, 3, 2))

# Unknown dimension: -1 lets NumPy work out the size
print(arr.reshape(2, 2, -1).shape)
print(arr.reshape(-1, 4).shape)

# Reshape returns a view when possible
r = arr.reshape(3, 4)
print("reshape returns a view:", r.base is arr)

# Flatten to 1-D
two_d = np.array([[1, 2, 3], [4, 5, 6]])
print("flatten:", two_d.reshape(-1), two_d.flatten(), two_d.ravel())

# Wrong shape raises an error
try:
    arr.reshape(5, 3)
except ValueError as e:
    print("ValueError:", e)

# Transpose
print("transpose:\n", two_d.T)
