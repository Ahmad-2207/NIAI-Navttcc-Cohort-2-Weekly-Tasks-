# Task 40: NumPy random numbers
import numpy as np
from numpy import random

# Seed for reproducible results
rng = np.random.default_rng(seed=42)

print("random integer 0..99:", rng.integers(100))
print("5 integers:", rng.integers(100, size=5))
print("2x3 integers:\n", rng.integers(100, size=(2, 3)))
print("random float 0..1:", rng.random())
print("array of floats:", rng.random(3).round(3))

# Choosing from values
print("choice:", rng.choice([3, 5, 7, 9]))
print("choice 2x3:\n", rng.choice([3, 5, 7, 9], size=(2, 3)))

# Weighted probabilities (sum to 1)
print("weighted:", rng.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=10))

# Shuffle and permutation
arr = np.arange(1, 8)
rng.shuffle(arr)
print("shuffled:", arr)
print("permutation:", rng.permutation(np.arange(1, 8)))

# Distributions
normal = rng.normal(loc=50, scale=10, size=1000)
print("normal mean/std:", normal.mean().round(2), normal.std().round(2))
uniform = rng.uniform(0, 1, size=1000)
print("uniform mean:", uniform.mean().round(2))
binom = rng.binomial(n=10, p=0.5, size=1000)
print("binomial mean:", binom.mean().round(2))

# Legacy API from the W3Schools page still works
random.seed(1)
print("legacy randint:", random.randint(100))
