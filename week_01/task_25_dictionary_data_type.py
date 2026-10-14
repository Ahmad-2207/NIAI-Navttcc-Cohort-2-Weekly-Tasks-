# Task 25: Exercises on the Dictionary data type

student = {"name": "Ali", "age": 21, "course": "AI"}
print(student)

# Access
print(student["name"], student.get("age"), student.get("gpa", "N/A"))

# Add and update
student["gpa"] = 3.45
student.update({"age": 22, "city": "Lahore"})
print(student)

# Remove
student.pop("city")
del student["gpa"]
print(student)

# Loop
for key in student:
    print(key, "=", student[key])
for key, value in student.items():
    print(f"{key}: {value}")
print(list(student.keys()), list(student.values()))

# Membership
print("name" in student, "email" in student)

# Nested dictionary
school = {
    "s1": {"name": "Ali", "marks": 80},
    "s2": {"name": "Sara", "marks": 92},
}
print(school["s2"]["marks"])

# Dictionary comprehension
squares = {n: n * n for n in range(1, 6)}
print(squares)

# Count word frequency
text = "to be or not to be"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)

# Sort by value
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=True))
