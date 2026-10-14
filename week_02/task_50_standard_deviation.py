# Task 50: Standard Deviation and Variance

import numpy as np

# Example from the W3Schools ML tutorial
speed1 = [86, 87, 88, 86, 87, 85, 86]   # values close together
speed2 = [32, 111, 138, 28, 59, 77, 97] # values spread out

for name, data in (("speed1", speed1), ("speed2", speed2)):
    print(f"{name}: mean={np.mean(data):.2f}  variance={np.var(data):.2f}  std={np.std(data):.2f}")

# Standard deviation is the square root of the variance
print("\nsqrt(var(speed2)) =", round(np.var(speed2) ** 0.5, 2), "= std(speed2) =", round(np.std(speed2), 2))

# Manual calculation (population standard deviation)
data = speed2
mean = sum(data) / len(data)
squared_diffs = [(x - mean) ** 2 for x in data]
variance = sum(squared_diffs) / len(data)
print("\nManual variance:", round(variance, 2), "| manual std:", round(variance ** 0.5, 2))

# Sample standard deviation divides by n-1 (ddof=1)
print("Sample std (ddof=1):", round(np.std(data, ddof=1), 2))

# Coefficient of variation compares spread between datasets with different scales
for name, d in (("speed1", speed1), ("speed2", speed2)):
    print(f"CV of {name}: {np.std(d) / np.mean(d) * 100:.1f}%")

# Share of values within one standard deviation of the mean
mean, std = np.mean(speed2), np.std(speed2)
within = [x for x in speed2 if mean - std <= x <= mean + std]
print(f"\n{len(within)} of {len(speed2)} values lie within one std of the mean")
