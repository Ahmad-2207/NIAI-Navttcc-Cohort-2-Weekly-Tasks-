# Task 20: Exercises on user defined functions

# 1. Basic function with a return value
def add(a, b):
    return a + b

print("add(3, 4) =", add(3, 4))

# 2. Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ali"))
print(greet("Sara", "Salam"))

# 3. Keyword arguments (order does not matter)
print(greet(greeting="Hi", name="Omar"))

# 4. *args and **kwargs
def total(*numbers):
    return sum(numbers)

def show_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print("total(1, 2, 3, 4) =", total(1, 2, 3, 4))
show_info(name="Ali", course="AI", week=2)

# 5. Returning multiple values
def min_max(values):
    return min(values), max(values)

low, high = min_max([4, 9, 1, 7])
print("min, max =", low, high)

# 6. Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print("5! =", factorial(5))
print("fibonacci(10) =", fibonacci(10))

# 7. Variable scope (local vs global)
counter = 0

def increment():
    global counter
    counter += 1

increment(); increment()
print("counter =", counter)

# 8. Lambda, map and filter
square = lambda x: x ** 2
nums = [1, 2, 3, 4, 5, 6]
print("Squares:", list(map(square, nums)))
print("Evens:", list(filter(lambda x: x % 2 == 0, nums)))

# 9. Inner (nested) function and closure
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print("double(21) =", double(21))

# 10. Docstring
def area_circle(r):
    """Return the area of a circle with radius r."""
    return 3.14159 * r ** 2

print(area_circle.__doc__, area_circle(2))
