# Task 23: Exercises on the String data type

s = "  Python Programming  "
print(repr(s))

# Cleaning and case
print(s.strip(), "|", s.lower(), "|", s.upper(), "|", s.strip().title())

# Indexing and slicing
word = "Programming"
print(word[0], word[-1], word[0:7], word[::-1])

# Searching and replacing
print(word.find("gram"), word.count("m"), word.replace("Pro", "Pre"))
print(word.startswith("Pro"), word.endswith("ing"))

# Split and join
sentence = "AI ML and DL are fun"
parts = sentence.split()
print(parts)
print("-".join(parts))

# Formatting: three ways
name, score = "Ali", 91.456
print("Name: %s, score: %.1f" % (name, score))
print("Name: {}, score: {:.2f}".format(name, score))
print(f"Name: {name}, score: {score:.0f}")

# Checks
print("abc123".isalnum(), "123".isdigit(), "abc".isalpha(), "   ".isspace())

# Palindrome check
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))

# Strings are immutable
try:
    word[0] = "p"
except TypeError as e:
    print("Strings are immutable:", e)
