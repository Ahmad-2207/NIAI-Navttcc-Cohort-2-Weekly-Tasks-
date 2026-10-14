# Task 24: Exercises on the Set data type

s = {1, 2, 3, 3, 2}
print("Duplicates removed:", s)

# Add and remove
s.add(4)
s.update([5, 6])
s.discard(10)      # no error if missing
s.remove(6)        # error if missing
print(s)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b, a.union(b))
print("Intersection:", a & b)
print("Difference a-b:", a - b)
print("Symmetric difference:", a ^ b)

# Subset checks
print({1, 2}.issubset(a), a.issuperset({1, 2}), a.isdisjoint({9}))

# Remove duplicates from a list
data = [1, 2, 2, 3, 3, 3, 4]
print(list(set(data)))

# Membership testing is fast
print(3 in a, 10 in a)

# frozenset is an immutable set
fs = frozenset([1, 2, 3])
print(fs)

# Set comprehension
print({x % 3 for x in range(10)})
