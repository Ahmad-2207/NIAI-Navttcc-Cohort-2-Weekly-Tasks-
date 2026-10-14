# Task 22: Exercises on the Tuple data type

t = (10, 20, 30, 40, 20)
print("Tuple:", t)

# Access and slicing
print(t[0], t[-1], t[1:3])

# Methods
print("count(20):", t.count(20), "| index(30):", t.index(30))

# Tuples are immutable
try:
    t[0] = 99
except TypeError as e:
    print("Cannot modify a tuple:", e)

# Single element tuple needs a trailing comma
single = (5,)
print(type(single), type((5)))

# Packing and unpacking
point = (3, 4)
x, y = point
print("x =", x, "y =", y)
first, *rest = (1, 2, 3, 4)
print(first, rest)

# Concatenate and repeat
print((1, 2) + (3, 4), (0,) * 3)

# Convert between list and tuple (the way to "change" a tuple)
as_list = list(t)
as_list[0] = 99
t = tuple(as_list)
print("Updated:", t)

# Tuples as dictionary keys
locations = {(31.52, 74.35): "Lahore", (33.68, 73.04): "Islamabad"}
print(locations[(31.52, 74.35)])
