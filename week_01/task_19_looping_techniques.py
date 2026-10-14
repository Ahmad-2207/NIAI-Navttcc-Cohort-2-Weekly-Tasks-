# Task 19: Exercises on various looping techniques

# 1. enumerate(): index and value
for idx, name in enumerate(["Ali", "Sara", "Omar"], start=1):
    print(idx, name)

# 2. zip(): loop over two lists together
names = ["Ali", "Sara", "Omar"]
marks = [80, 92, 75]
for n, m in zip(names, marks):
    print(f"{n} scored {m}")

# 3. dict.items()
scores = {"math": 90, "physics": 85, "chemistry": 78}
for subject, score in scores.items():
    print(subject, "->", score)

# 4. reversed() and sorted()
for x in reversed([1, 2, 3]):
    print(x, end=" ")
print()
for x in sorted({5, 1, 4, 2}):
    print(x, end=" ")
print()

# 5. List comprehension
squares = [x ** 2 for x in range(1, 8)]
print("Squares:", squares)
evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)

# 6. Dictionary comprehension
print({x: x ** 3 for x in range(1, 5)})

# 7. Iterators and iterables
it = iter([10, 20, 30])
print(next(it), next(it), next(it))

# 8. Nested loops: multiplication grid
for i in range(1, 4):
    print([i * j for j in range(1, 6)])
