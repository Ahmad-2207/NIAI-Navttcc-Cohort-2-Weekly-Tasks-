# Task 28: NumPy creating arrays
import numpy as np

# From Python lists
a = np.array([1, 2, 3, 4, 5])
print("1-D:", a, type(a))

# Dimensions: 0-D, 1-D, 2-D, 3-D
print("0-D:", np.array(42).ndim)
print("1-D:", np.array([1, 2, 3]).ndim)
print("2-D:", np.array([[1, 2, 3], [4, 5, 6]]).ndim)
print("3-D:", np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]).ndim)

# Higher dimensions with ndmin
print(np.array([1, 2, 3, 4], ndmin=5).shape)

# Built-in methods
print("zeros   :", np.zeros(4))
print("ones    :", np.ones((2, 3)))
print("full    :", np.full((2, 2), 7))
print("eye     :\n", np.eye(3))
print("arange  :", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))

# Random
print("random  :", np.random.rand(3))
