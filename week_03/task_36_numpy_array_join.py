# Task 36: NumPy joining arrays
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("concatenate:", np.concatenate((a, b)))

# 2-D, axis 0 (stack rows) and axis 1 (stack columns)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print("axis=0:\n", np.concatenate((m1, m2), axis=0))
print("axis=1:\n", np.concatenate((m1, m2), axis=1))

# stack functions
print("stack (new axis):\n", np.stack((a, b)))
print("stack axis=1:\n", np.stack((a, b), axis=1))
print("hstack:", np.hstack((a, b)))
print("vstack:\n", np.vstack((a, b)))
print("dstack shape:", np.dstack((a, b)).shape)

# append and insert
print("append:", np.append(a, [7, 8]))
print("insert:", np.insert(a, 1, 99))
print("delete:", np.delete(a, 0))
