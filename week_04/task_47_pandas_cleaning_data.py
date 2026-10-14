# Task 47: Pandas data cleaning
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "data" / "fitness_messy.csv")
print("RAW DATA")
print(df)
print("\nmissing values:\n", df.isnull().sum())

# 1. Empty cells: drop rows or fill
no_na = df.dropna()
print("\nrows after dropna:", len(no_na), "(was", len(df), ")")

clean = df.copy()
clean["Calories"] = clean["Calories"].fillna(clean["Calories"].mean())
clean["Pulse"] = clean["Pulse"].fillna(clean["Pulse"].median())

# 2. Wrong format: fix dates (invalid or missing dates become NaT)
clean["Date"] = pd.to_datetime(clean["Date"], format="mixed", errors="coerce")
clean = clean.dropna(subset=["Date"])

# 3. Wrong data: replace an unrealistic value (450 minutes) with a limit
for idx in clean.index:
    if clean.loc[idx, "Duration"] > 180:
        clean.loc[idx, "Duration"] = 120

# 4. Duplicates
print("\nduplicated rows:", clean.duplicated().sum())
clean = clean.drop_duplicates()

print("\nCLEAN DATA")
print(clean.reset_index(drop=True))
print("\nmissing values after cleaning:", int(clean.isnull().sum().sum()))
