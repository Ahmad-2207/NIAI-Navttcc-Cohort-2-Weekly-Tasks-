# Task 42: Pandas installation and getting started
#
# Install with one of these commands in a terminal:
#     pip install pandas
#     conda install pandas
#
# Then run this file to confirm it works.
import sys

try:
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("pandas is not installed. Run: pip install pandas")

print("pandas :", pd.__version__)
print("numpy  :", np.__version__)

# Smoke test: build a tiny DataFrame
mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)
print("\nInstallation works.")
