# Task 31: NumPy data types
import numpy as np

# Default types
print("ints   :", np.array([1, 2, 3]).dtype)
print("floats :", np.array([1.5, 2.5]).dtype)
print("strings:", np.array(["apple", "banana"]).dtype)
print("bools  :", np.array([True, False]).dtype)

# Type codes: i integer, u unsigned, f float, S string, U unicode, b boolean
print(np.array([1, 2, 3, 4], dtype="S").dtype)
print(np.array([1, 2, 3, 4], dtype="i4"), np.array([1, 2, 3, 4], dtype="i4").dtype)

# Converting types with astype (returns a copy)
floats = np.array([1.1, 2.7, 3.9])
ints = floats.astype("i")
print("float -> int (truncates):", ints)
print("int -> bool:", np.array([0, 1, 2]).astype(bool))
print("str -> int:", np.array(["1", "2", "3"]).astype(int))

# Memory use
print("int8 bytes:", np.arange(1000, dtype=np.int8).nbytes)
print("int64 bytes:", np.arange(1000, dtype=np.int64).nbytes)

# Values that cannot be converted raise an error
try:
    np.array(["a", "b"], dtype="i")
except ValueError as e:
    print("ValueError:", e)
