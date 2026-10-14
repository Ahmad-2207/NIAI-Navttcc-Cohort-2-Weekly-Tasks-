# Task 41: Pandas basics
import pandas as pd

print("pandas version:", pd.__version__)

# A DataFrame is a 2-D table, a Series is one column
data = {
    "name": ["Ali", "Sara", "Omar", "Hina"],
    "marks": [78, 92, 85, 66],
    "city": ["Lahore", "Karachi", "Lahore", "Multan"],
}
df = pd.DataFrame(data)
print(df)

# Basic inspection
print("\nshape:", df.shape)
print("columns:", list(df.columns))
print(df.dtypes)
print(df.describe())

# Select a column, filter rows, add a column
print("\n", df["name"])
print(df[df["marks"] > 80])
df["passed"] = df["marks"] >= 70
print(df)

# Sorting and simple aggregation
print(df.sort_values("marks", ascending=False))
print("Average marks:", df["marks"].mean())
print(df["city"].value_counts())
