# Task 38: NumPy searching arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

# where: indexes of matching values
print("Positions of 4:", np.where(arr == 4))
print("Positions of even numbers:", np.where(arr % 2 == 0))

# where with three arguments works like an if/else
print(np.where(arr > 3, "big", "small"))

# searchsorted: where a value should be inserted to keep order
sorted_arr = np.array([6, 7, 8, 9])
print("Insert 7 (left) at:", np.searchsorted(sorted_arr, 7))
print("Insert 7 (right) at:", np.searchsorted(sorted_arr, 7, side="right"))
print("Insert [2, 4, 6]:", np.searchsorted(sorted_arr, [2, 4, 6]))

# argmax, argmin
print("argmax:", arr.argmax(), "argmin:", arr.argmin())

# Membership checks
print("any > 4:", (arr > 4).any(), "| all > 0:", (arr > 0).all())
print("isin:", np.isin(arr, [1, 5]))
