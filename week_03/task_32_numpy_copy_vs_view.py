# Task 32: NumPy array copy vs view
import numpy as np

# COPY: a new array, owns its data, changes do not affect the original
arr = np.array([1, 2, 3, 4, 5])
c = arr.copy()
arr[0] = 42
print("original:", arr)
print("copy    :", c)

# VIEW: shares data with the original, changes are visible in both
arr = np.array([1, 2, 3, 4, 5])
v = arr.view()
arr[0] = 42
v[1] = 99
print("\noriginal:", arr)
print("view    :", v)

# Check ownership with .base
print("\ncopy.base is None:", c.base is None)
print("view.base is arr :", v.base is arr)

# Slices are views, fancy/boolean indexing returns copies
a = np.arange(10)
s = a[2:5]
s[0] = 100
print("\nslice modified original:", a)
b = a[[1, 2]]
b[0] = -1
print("fancy index did NOT modify original:", a)
