# Task 15: Exercises on for loops

# 1. Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. range(): start, stop (exclusive), step
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()
print("Even numbers up to 10:", [i for i in range(0, 11, 2)])

# 3. Loop over a string
for ch in "Python":
    print(ch, end="-")
print()

# 4. Multiplication table of 7
print("\nTable of 7")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# 5. Sum of the first 100 numbers
total = 0
for i in range(1, 101):
    total += i
print("\nSum 1..100 =", total)

# 6. for ... else (else runs when the loop was not stopped by break)
for n in range(2, 5):
    pass
else:
    print("Loop finished without break")

# 7. Nested loop: right triangle of stars
print()
for i in range(1, 6):
    print("*" * i)
