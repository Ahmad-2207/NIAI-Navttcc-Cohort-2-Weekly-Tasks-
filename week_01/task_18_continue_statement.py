# Task 18: Exercises on the continue statement

# 1. Skip a particular letter
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print(letter, end="")
print()

# 2. Print only odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 3. Skip negative numbers while summing
numbers = [4, -1, 7, -3, 10]
total = 0
for n in numbers:
    if n < 0:
        continue
    total += n
print("Sum of positives:", total)

# 4. continue in a while loop (increment BEFORE continue to avoid an infinite loop)
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print("i =", i)

# 5. Skip vowels in a sentence
sentence = "continue statement in python"
print("".join(c for c in sentence if c not in "aeiou"))
