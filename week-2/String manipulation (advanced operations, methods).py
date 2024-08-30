'''1. String Slicing
Basic slicing: Extract a portion of a string using indices.'''

s = "Hello, World!"
print(s[7:12])  # Output: World

#Step slicing: Extract every nth character.

print(s[::2])  # Output: Hlo ol!

'''2. String Methods
str.join(iterable): Join a sequence of strings with a specified delimiter.'''

words = ["Hello", "World"]
result = " ".join(words)  # Output: "Hello World"
#str.split(separator, maxsplit): Split a string into a list using a specified separator.

sentence = "Hello, World, Python"
result = sentence.split(", ")  # Output: ['Hello', 'World', 'Python']
#str.replace(old, new, count): Replace occurrences of a substring with another substring.

s = "Hello, World!"
result = s.replace("World", "Python")  # Output: "Hello, Python!"

#str.strip([chars]): Remove leading and trailing characters (whitespace by default).

s = "  Hello, World!  "
result = s.strip()  # Output: "Hello, World!"

#str.find(sub, start, end): Return the lowest index where the substring is found.

s = "Hello, World!"
index = s.find("World")  # Output: 7


#str.count(sub, start, end): Count the number of occurrences of a substring.

s = "Hello, World! Hello!"
count = s.count("Hello")  # Output: 2

#str.startswith(prefix, start, end) and str.endswith(suffix, start, end): Check if a string starts or ends with a specified substring.

s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World!"))   # Output: True


'''3. Advanced Formatting
str.format(): Basic formatting.'''

s = "Hello, {}!".format("World")  # Output: "Hello, World!"


#f-strings (formatted string literals): Embed expressions inside string literals.


name = "World"
s = f"Hello, {name}!"  # Output: "Hello, World!"


#Padding and alignment:

s = "Hello"
padded_s = f"{s:>10}"  # Output: "     Hello" (right-aligned with padding)


'''4. Regular Expressions (RegEx)
Python’s re module provides advanced string manipulation capabilities.
Pattern Matching:'''

import re
s = "The rain in Spain"
match = re.search(r"rain", s)
if match:
    print("Match found!")  # Output: Match found!
#Replacing Patterns:

s = "The rain in Spain"
result = re.sub(r"Spain", "France", s)  # Output: "The rain in France"


'''5. String Encoding and Decoding
str.encode(encoding): Encode a string into bytes.'''

s = "Hello, World!"
encoded = s.encode('utf-8')  # Output: b'Hello, World!'

#bytes.decode(encoding): Decode bytes into a string.

decoded = encoded.decode('utf-8')  # Output: "Hello, World!"


'''6. String Interpolation with the % Operator
Although older, the % operator is still used for formatting.'''

name = "World"
s = "Hello, %s!" % name  # Output: "Hello, World!"

'''7. Case Conversion
str.upper() and str.lower(): Convert to uppercase or lowercase.'''

s = "Hello, World!"
print(s.upper())  # Output: "HELLO, WORLD!"
print(s.lower())  # Output: "hello, world!"

#str.title(): Convert to title case.

s = "hello, world!"
print(s.title())  # Output: "Hello, World!"

#str.swapcase(): Swap the case of each character.


s = "Hello, World!"
print(s.swapcase())  # Output: "hELLO, wORLD!"

'''8. String Translation
str.translate(table): Translate characters based on a translation table created using str.maketrans().'''

s = "Hello, World!"
table = str.maketrans("Helo", "HELO")
translated = s.translate(table)  # Output: "HELLO, WOrLd!"

'''9. String Reversal
Reverse a string using slicing:'''

s = "Hello, World!"
reversed_s = s[::-1]  # Output: "!dlroW ,olleH"
