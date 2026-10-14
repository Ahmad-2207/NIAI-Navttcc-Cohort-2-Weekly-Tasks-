# Task 26: Exercises on exception handling

# 1. try / except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Handling several exception types
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"  '{value}' is not a valid integer")
    except TypeError:
        print(f"  {value!r} has the wrong type")

safe_convert("42")
safe_convert("abc")
safe_convert(None)

# 3. else and finally
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  error: division by zero")
    else:
        print("  division worked, result =", result)
    finally:
        print("  finally always runs")

divide(10, 2)
divide(1, 0)

# 4. Catching the exception object
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e:
    print("IndexError:", e)

# 5. File handling with exceptions
try:
    with open("this_file_does_not_exist.txt") as f:
        f.read()
except FileNotFoundError:
    print("File not found, so we handle it gracefully")

# 6. Raising an exception
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("ValueError:", e)

# 7. Keep asking until valid input (simulated with a list of attempts)
attempts = iter(["x", "3.5", "7"])
while True:
    raw = next(attempts)
    try:
        number = int(raw)
        print("Valid number:", number)
        break
    except ValueError:
        print(f"  '{raw}' rejected, trying again")

# 8. Basic file handling: write, read, append
with open("demo_file.txt", "w") as f:
    f.write("line one\nline two\n")
with open("demo_file.txt", "a") as f:
    f.write("line three\n")
with open("demo_file.txt") as f:
    for line in f:
        print(line.rstrip())

import os
os.remove("demo_file.txt")
