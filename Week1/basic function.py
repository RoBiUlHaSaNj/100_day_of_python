'''
1. Basic Function Definition

A function is a block of reusable code that performs a specific task.
It is defined using the def keyword.

'''
def function_name(parameters):
    # function body
    return value  # optional


def greet():
    return"hello,world"

#Calling the function:


print(greet())



# 2. Function Arguments

 # Positional Arguments: These are the most common, where the order of arguments matters.


def greet(name):
    return f"Hello, {name}!"

print(greet("Jisan"))  # Output: Hello, Jisan!

# Default Arguments: These arguments have a default value if no argument is provided.

def greet(name="World"):
    return f"Hello, {name}!"

print(greet())        # Output: Hello, World!
print(greet("Jisan"))  # Output: Hello, Jisan!

# Keyword Arguments: You can specify arguments by name, making the order irrelevant.

def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet(name="Jisan"))          # Output: Hello, Jisan!
print(greet(name="Jisan", message="Hi"))  # Output: Hi, Jisan!


# Arbitrary Arguments (*args): Used to pass a variable number of arguments to a function.

def greet(*names):
    return f"Hello, {', '.join(names)}!"

print(greet("Jisan", "John", "Jane"))  # Output: Hello, Jisan, John, Jane!


# Arbitrary Keyword Arguments (**kwargs): Used to pass a variable number of keyword arguments.

def greet(**person):
    return f"Hello, {person['name']}! You are {person['age']} years old."

print(greet(name="Jisan", age=25))  # Output: Hello, Jisan! You are 25 years old.

# 3. Return Values

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8





