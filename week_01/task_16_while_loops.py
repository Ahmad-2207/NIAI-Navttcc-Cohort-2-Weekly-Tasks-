# Task 16: Exercises on while loops

# 1. Count from 1 to 5
count = 1
while count <= 5:
    print("count =", count)
    count += 1

# 2. Sum of digits of a number
n = 98765
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits of 98765 =", total)

# 3. Factorial of 6
num, fact = 6, 1
while num > 1:
    fact *= num
    num -= 1
print("6! =", fact)

# 4. Reverse a number
n, rev = 12345, 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reverse of 12345 =", rev)

# 5. while ... else
i = 0
while i < 3:
    i += 1
else:
    print("while loop ended normally, i =", i)

# 6. Collatz sequence from 6
x, seq = 6, [6]
while x != 1:
    x = x // 2 if x % 2 == 0 else 3 * x + 1
    seq.append(x)
print("Collatz(6):", seq)
