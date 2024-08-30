# 1. capitalize()
# Converts the first character of the string to uppercase.
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# 2. casefold()
# Converts the string to lowercase, more aggressive than lower().
text = "HELLO WORLD"
print(text.casefold())  # Output: "hello world"

# 3. center(width, fillchar)
# Centers the string, padded with the specified fill character.
text = "hello"
print(text.center(10, '-'))  # Output: "--hello---"

# 4. count(substring, start, end)
# Returns the number of times a substring occurs in the string.
text = "hello hello"
print(text.count("hello"))  # Output: 2

# 5. encode(encoding, errors)
# Returns an encoded version of the string.
text = "hello"
encoded_text = text.encode("utf-8")
print(encoded_text)  # Output: b'hello'

# 6. endswith(suffix, start, end)
# Returns True if the string ends with the specified suffix.
text = "hello world"
print(text.endswith("world"))  # Output: True

# 7. expandtabs(tabsize)
# Sets the tab size for the string.
text = "hello\tworld"
print(text.expandtabs(4))  # Output: "hello   world"

# 8. find(substring, start, end)
# Searches for the substring and returns its index, or -1 if not found.
text = "hello world"
print(text.find("world"))  # Output: 6

# 9. format(*args, **kwargs)
# Formats the string using the specified values.
text = "Hello, {}!"
print(text.format("world"))  # Output: "Hello, world!"

# 10. isalnum()
# Returns True if the string is alphanumeric.
text = "Hello123"
print(text.isalnum())  # Output: True

# 11. isalpha()
# Returns True if the string contains only alphabetic characters.
text = "Hello"
print(text.isalpha())  # Output: True

# 12. isdigit()
# Returns True if the string contains only digits.
text = "12345"
print(text.isdigit())  # Output: True

# 13. islower()
# Returns True if all characters in the string are lowercase.
text = "hello"
print(text.islower())  # Output: True

# 14. isnumeric()
# Returns True if the string contains only numeric characters.
text = "12345"
print(text.isnumeric())  # Output: True

# 15. isspace()
# Returns True if the string contains only whitespace characters.
text = "   "
print(text.isspace())  # Output: True

# 16. istitle()
# Returns True if the string is in title case.
text = "Hello World"
print(text.istitle())  # Output: True

# 17. isupper()
# Returns True if all characters in the string are uppercase.
text = "HELLO"
print(text.isupper())  # Output: True

# 18. join(iterable)
# Joins the elements of an iterable with the string as the separator.
text = "-"
print(text.join(["hello", "world"]))  # Output: "hello-world"

# 19. lower()
# Converts all characters in the string to lowercase.
text = "HELLO"
print(text.lower())  # Output: "hello"

# 20. replace(old, new, count)
# Replaces a specified substring with another substring.
text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

# 21. split(separator, maxsplit)
# Splits the string at the specified separator and returns a list.
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

# 22. startswith(prefix, start, end)
# Returns True if the string starts with the specified prefix.
text = "hello world"
print(text.startswith("hello"))  # Output: True

# 23. strip(chars)
# Removes leading and trailing characters (spaces by default).
text = "  hello  "
print(text.strip())  # Output: "hello"

# 24. swapcase()
# Swaps the case of all characters in the string.
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"

# 25. upper()
# Converts all characters in the string to uppercase.
text = "hello"
print(text.upper())  # Output: "HELLO"
