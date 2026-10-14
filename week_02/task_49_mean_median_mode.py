# Task 49: Mean, Median and Mode
# Uses numpy and scipy-free code so it runs anywhere with numpy installed.

import numpy as np
from collections import Counter

# Example from the W3Schools ML tutorial: speeds of 13 cars
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean: the average value
mean = np.mean(speed)
print("Mean   :", round(mean, 2))

# Median: the middle value after sorting
median = np.median(speed)
print("Median :", median)

# Mode: the most common value (computed with Counter, works for any data)
counts = Counter(speed)
mode_value, mode_count = counts.most_common(1)[0]
print(f"Mode   : {mode_value} (appears {mode_count} times)")

# Manual calculation to show how it works
sorted_speed = sorted(speed)
n = len(sorted_speed)
manual_mean = sum(speed) / n
manual_median = sorted_speed[n // 2] if n % 2 else (sorted_speed[n // 2 - 1] + sorted_speed[n // 2]) / 2
print("\nManual check:", round(manual_mean, 2), manual_median)

# Effect of an outlier: mean moves a lot, median barely moves
with_outlier = speed + [500]
print("\nWith an outlier of 500:")
print("Mean   :", round(np.mean(with_outlier), 2))
print("Median :", np.median(with_outlier))

# Even number of values: median is the average of the two middle values
print("\nMedian of [1, 2, 3, 4] =", np.median([1, 2, 3, 4]))
