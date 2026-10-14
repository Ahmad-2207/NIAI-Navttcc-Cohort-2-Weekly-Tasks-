# Task 46: Pandas analyzing data
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "data" / "fitness.csv")

# First look
print(df.head(10))
print("\nlast rows:\n", df.tail())
print("\nshape:", df.shape)

# Info: columns, non-null counts and data types
df.info()

# Summary statistics
print("\n", df.describe().round(2))

# More questions you can ask
print("\nColumn means:\n", df.mean().round(2))
print("\nLongest workout:", df["Duration"].max(), "minutes")
print("Workouts above 100 minutes:", (df["Duration"] > 100).sum())
print("Missing values per column:\n", df.isnull().sum())

# Group the durations into short / medium / long and count them
df["Length"] = pd.cut(df["Duration"], bins=[0, 45, 90, 200], labels=["short", "medium", "long"])
print("\n", df["Length"].value_counts())
print(df.groupby("Length", observed=True)["Calories"].mean().round(1))
