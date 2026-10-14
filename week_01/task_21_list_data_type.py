# Task 21: Exercises on the List data type

fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

# Access, negative index, slicing
print(fruits[0], fruits[-1], fruits[0:2])

# Add items
fruits.append("date")
fruits.insert(1, "blueberry")
fruits.extend(["fig", "grape"])
print("After adding:", fruits)

# Remove items
fruits.remove("banana")
last = fruits.pop()
del fruits[0]
print("After removing:", fruits, "| popped:", last)

# Sort, reverse, count, index
nums = [5, 2, 9, 1, 5, 6]
nums.sort()
print("Sorted:", nums)
nums.reverse()
print("Reversed:", nums)
print("Count of 5:", nums.count(5), "| index of 9:", nums.index(9))

# Copy vs reference
a = [1, 2, 3]
b = a            # same list
c = a.copy()     # new list
a.append(4)
print("a:", a, "b:", b, "c:", c)

# Useful built-ins
print(len(nums), max(nums), min(nums), sum(nums))

# Nested list
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])
