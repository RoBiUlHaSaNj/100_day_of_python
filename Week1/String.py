#for one line

my="hello my name robiul"
you='my name alice'
print(my,you)
print(you+my)

#find length
a = "Hello, World!"
print(len(a))

#for many line

para="""Climate change is a global issue,
 and yet the effects of our climate 
crisis do not impact us all equally. 
It is well established that the
 industrialization of the Global 
North has largely contributed 
 to climate change, while the
Global South bears the brunt 
of its devastating effects. While
working towards the Paris Agreement’s
 overarching goal of limiting global 
warming above a 1.5°C rise 
in temperature, GAIA’s work on 
climate is rooted in our commitment to 
social justice. We believe the Global 
North must take accountability for its role
, and that solutions must not only address 
GHG emission reductions globally
 but address climate justice inequalities as well."""


print(para)


#find index vlaue
word = "Python"
print(word[0])  # Output: P
print(word[5])  # Output: n

#find index range base  value

word = "Python"
print(word[0:2])  # Output: Py (characters from index 0 to 1)
print(word[2:5])  # Output: tho (characters from index 2 to 4)
word = "Python"
print(word[0:2])  # Output: Py (characters from index 0 to 1)
print(word[2:5])  # Output: tho (characters from index 2 to 4)

#f-string
name = "Alice"
age = 30

# Using an f-string to format the string
message = f"Hello, my name is {name} and I am {age} years old."

print(message)



#lower() and upper(): Convert the string to lowercase or uppercase.

print("Hello".lower())  # Output: hello
print("world".upper())  # Output: WORLD
text = "  Hello, World!  "
print(text.strip())  # Output: "Hello, World!"strip(): Remove leading and trailing whitespace (or other characters).


#replace(): Replace all occurrences of a substring with another substring.

string = "Hello python"
new_string = string.replace("Hello", "Good Bye")

print(new_string)

print("Hello, World!".replace("World", "Python"))  # Output: Hello, Python!


#split(): Split the string into a list of substrings based on a delimiter.

words = "Python is fun".split()  # Splits by space
print(words)  # Output: ['Python', 'is', 'fun']

#join(): Join a list of strings into a single string with a specified delimiter.

words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)  # Output: Python is fun


#find(): Find the first occurrence of a substring and return its index.

print("Hello, World!".find("World"))  # Output: 7



#startswith() and endswith(): Check if the string starts or ends with a particular substring.

print("Hello, World!".startswith("Hello"))  # Output: True
print("Hello, World!".endswith("Python"))   # Output: False


#String Manipulation in Python
#1. Concatenation

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Output: "John Doe"
print(full_name)

#2. Repetition

laugh = "ha"
repeated_laugh = laugh * 3  # Output: "hahaha"
print(repeated_laugh)

#3. Slicing and Dicing

text = "Hello, World!"
print(text[0:5])  # Output: "Hello"
print(text[:5])   # Output: "Hello" (from the start)
print(text[7:])   # Output: "World!" (to the end)
print(text[-6:])  # Output: "World!" (using negative indexing)

#4. Reversing a String
text = "Python"
reversed_text = text[::-1]  # Output: "nohtyP"
print(reversed_text)


#5. Changing Case

text = "python programming"
print(text.upper())       # Output: "PYTHON PROGRAMMING"
print(text.lower())       # Output: "python programming"
print(text.title())       # Output: "Python Programming"
print(text.capitalize())  # Output: "Python programming"


#6. Replacing Substrings

text = "Hello, World!"
new_text = text.replace("World", "Python")  # Output: "Hello, Python!"
print(new_text)

#7. Removing Whitespace
text = "   Hello, World!   "
print(text.strip())   # Output: "Hello, World!"
print(text.lstrip())  # Output: "Hello, World!   "
print(text.rstrip())  # Output: "   Hello, World!"


#8. Splitting and Joining Strings
text = "Python is fun"
words = text.split()  # Output: ['Python', 'is', 'fun']
print(words)

joined_text = " ".join(words)  # Output: "Python is fun"
print(joined_text)


#9. Finding and Counting Substrings
text = "banana"
print(text.find("na"))  # Output: 2
print(text.count("na"))  # Output: 2

#10. Checking String Properties

text = "Python"
print(text.startswith("Py"))  # Output: True
print(text.endswith("on"))    # Output: True
print(text.isalnum())         # Output: True (no spaces or special characters)
print("12345".isdigit())      # Output: True


#11. Advanced: Regular Expressions (Regex)
#not enough 


import re

text = "The rain in Spain"

# Find all occurrences of "ai"
matches = re.findall("ai", text)  # Output: ['ai', 'ai']
print(matches)

# Replace all spaces with underscores
new_text = re.sub(r"\s", "_", text)  # Output: "The_rain_in_Spain"
print(new_text)
