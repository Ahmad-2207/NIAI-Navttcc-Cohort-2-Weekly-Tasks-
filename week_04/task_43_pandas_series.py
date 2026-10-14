# Task 43: Pandas Series
import pandas as pd

# From a list: default index is 0, 1, 2 ...
a = [1, 7, 2]
s = pd.Series(a)
print(s)
print("second value:", s[1])

# Custom labels
s2 = pd.Series(a, index=["x", "y", "z"])
print(s2)
print("value at label y:", s2["y"])

# From a dictionary: keys become the index
calories = {"day1": 420, "day2": 380, "day3": 390}
s3 = pd.Series(calories)
print(s3)
print("Only day1 and day2:\n", pd.Series(calories, index=["day1", "day2"]))

# Name and dtype
s3.name = "calories"
print(s3.dtype, s3.name)

# Vectorised operations and statistics
print("\nmean:", s3.mean(), "| max:", s3.max(), "| sum:", s3.sum())
print(s3 * 2)
print(s3[s3 > 385])
print(s3.sort_values())
print(s3.idxmax())
