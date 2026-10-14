# Task 44: Pandas DataFrames
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df)

# Locate rows with loc (label based) and iloc (position based)
print("\nrow 0:\n", df.loc[0])
print("rows 0 and 1:\n", df.loc[[0, 1]])
print("iloc[1, 0] =", df.iloc[1, 0])

# Named indexes
df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])
print("\n", df2)
print("day2:\n", df2.loc["day2"])

# Add, modify and drop columns
df2["calories_per_min"] = (df2["calories"] / df2["duration"]).round(2)
print(df2)
df2 = df2.drop(columns=["calories_per_min"])

# Add a row
df2.loc["day4"] = [400, 42]
print(df2)

# Selection and conditions
print(df2[df2["duration"] > 41])
print(df2[["calories"]])

# Information about the frame
print(df2.shape, list(df2.columns), list(df2.index))
df2.info()
