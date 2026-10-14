# Task 39: NumPy sorting arrays
import numpy as np

print(np.sort(np.array([3, 2, 0, 1])))
print(np.sort(np.array(["banana", "cherry", "apple"])))
print(np.sort(np.array([True, False, True])))

# 2-D arrays are sorted along each row by default
arr = np.array([[3, 2, 4], [5, 0, 1]])
print("rows sorted:\n", np.sort(arr))
print("columns sorted:\n", np.sort(arr, axis=0))

# Descending order
nums = np.array([5, 1, 9, 3])
print("descending:", np.sort(nums)[::-1])

# argsort gives the index order, useful to sort one array by another
names = np.array(["Ali", "Sara", "Omar"])
marks = np.array([70, 95, 82])
order = np.argsort(marks)
print("names by marks (low to high):", names[order])
print("names by marks (high to low):", names[order[::-1]])

# sort() in place
nums.sort()
print("in place:", nums)
