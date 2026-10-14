# Task 17: Exercises on the break statement

# 1. Stop a loop when a value is found
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        print("First e or s found:", letter)
        break

# 2. Find the first number divisible by 7 after 50
for n in range(51, 100):
    if n % 7 == 0:
        print("First multiple of 7 after 50:", n)
        break

# 3. break inside while True with a condition
total, i = 0, 1
while True:
    total += i
    if total > 50:
        print(f"Sum passed 50 at i={i}, total={total}")
        break
    i += 1

# 4. Prime check using break and for-else
for candidate in [17, 21, 29]:
    for d in range(2, int(candidate ** 0.5) + 1):
        if candidate % d == 0:
            print(candidate, "is not prime (divisible by", d, ")")
            break
    else:
        print(candidate, "is prime")

# 5. break only leaves the innermost loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print("i, j =", i, j)
