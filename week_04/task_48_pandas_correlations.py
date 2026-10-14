# Task 48: Pandas data correlations
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "data" / "fitness.csv")

# corr() returns the correlation matrix (Pearson by default)
corr = df.corr().round(2)
print(corr)

# Interpretation guide
#   1.0   perfect positive      0.0   no linear relationship
#  -1.0   perfect negative      above 0.6 or below -0.6 is usually called strong

# Read single pairs
print("\nDuration vs Calories:", round(df["Duration"].corr(df["Calories"]), 2))
print("Duration vs Pulse   :", round(df["Duration"].corr(df["Pulse"]), 2))

# Strongest relationship with Calories
print("\nCorrelation with Calories:")
print(corr["Calories"].drop("Calories").sort_values(ascending=False))

# List strong pairs automatically
print("\nStrong pairs (|r| > 0.6):")
cols = corr.columns
for i, a in enumerate(cols):
    for b in cols[i + 1:]:
        if abs(corr.loc[a, b]) > 0.6:
            print(f"  {a} and {b}: {corr.loc[a, b]}")

# Optional picture of the matrix (saved, not shown)
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation matrix")
    plt.tight_layout()
    plt.savefig(Path(__file__).parent / "correlation_heatmap.png", dpi=120)
    print("\nSaved correlation_heatmap.png")
except ImportError:
    print("\n(install matplotlib and seaborn to also draw the heatmap)")
