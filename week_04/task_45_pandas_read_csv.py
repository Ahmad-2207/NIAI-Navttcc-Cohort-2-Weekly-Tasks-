# Task 45: Pandas read CSV files
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).parent / "data" / "fitness.csv"

df = pd.read_csv(csv_path)

# A DataFrame with many rows is truncated when printed, so look at parts
print(df.head())          # first 5 rows
print(df.tail(3))         # last 3 rows
print("shape:", df.shape)

# Control how much is displayed
print("max rows setting:", pd.options.display.max_rows)

# Read only some columns or rows
print(pd.read_csv(csv_path, usecols=["Duration", "Calories"]).head(3))
print(pd.read_csv(csv_path, nrows=3))

# Save a new CSV and read it back
out_path = Path(__file__).parent / "data" / "fitness_top10.csv"
df.sort_values("Calories", ascending=False).head(10).to_csv(out_path, index=False)
print("saved:", out_path.name, "->", pd.read_csv(out_path).shape)
out_path.unlink()   # remove the temporary file

# Reading from a string (same as a file)
from io import StringIO
text = "a,b\n1,2\n3,4"
print(pd.read_csv(StringIO(text)))
