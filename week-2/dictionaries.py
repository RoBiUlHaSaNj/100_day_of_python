'''Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with some initial key-value pairs
student = {
    'name': 'Alice',
    'age': 25,
    'courses': ['Math', 'Computer Science']
}
print(student)  # Output: {'name': 'Alice', 'age': 25, 'courses': ['Math', 'Computer Science']}

# Example dictionary
student_info = {
    "name": "Robiul Hasan Jisan",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

# Empty dictionary
empty_dict = {}

#Accessing Dictionary Values

name = student_info["name"]
print(name)  # Output: Robiul Hasan Jisan

age = student_info.get("age", "Not found")
print(age)  # Output: 22

# Using a non-existent key
address = student_info.get("address", "Address not found")
print(address)  # Output: Address not found


# Accessing values using keys
print(student['name'])  # Output: Alice
print(student['age'])   # Output: 25

# Using the get() method to avoid KeyError
print(student.get('courses'))  # Output: ['Math', 'Computer Science']
print(student.get('grade', 'Not Found'))  # Output: Not Found

#Modifying a Dictionary

# Adding or updating a key-value pair
student['grade'] = 'A'
print(student)  # Output: {'name': 'Alice', 'age': 25, 'courses': ['Math', 'Computer Science'], 'grade': 'A'}

# Updating multiple key-value pairs at once
student.update({'age': 26, 'name': 'Bob'})
print(student)  # Output: {'name': 'Bob', 'age': 26, 'courses': ['Math', 'Computer Science'], 'grade': 'A'}

#Removing Elements
# Removing a specific key-value pair using pop()
grade = student.pop('grade')
print(grade)    # Output: A
print(student)  # Output: {'name': 'Bob', 'age': 26, 'courses': ['Math', 'Computer Science']}

# Removing the last inserted key-value pair using popitem() (Python 3.7+)
last_item = student.popitem()
print(last_item)  # Output: ('courses', ['Math', 'Computer Science'])
print(student)    # Output: {'name': 'Bob', 'age': 26}

# Removing a specific key-value pair using del
del student['age']
print(student)  # Output: {'name': 'Bob'}

# Clearing the dictionary
student.clear()
print(student)  # Output: {}


#Common Dictionary Methods

# Reinitializing the dictionary
student = {
    'name': 'Alice',
    'age': 25,
    'courses': ['Math', 'Computer Science']
}

# Getting all keys, values, and key-value pairs
print(student.keys())    # Output: dict_keys(['name', 'age', 'courses'])
print(student.values())  # Output: dict_values(['Alice', 25, ['Math', 'Computer Science']])
print(student.items())   # Output: dict_items([('name', 'Alice'), ('age', 25), ('courses', ['Math', 'Computer Science'])])

# Checking if a key exists in a dictionary
print('name' in student)  # Output: True
print('grade' in student) # Output: False

# Copying a dictionary
student_copy = student.copy()
print(student_copy)  # Output: {'name': 'Alice', 'age': 25, 'courses': ['Math', 'Computer Science']}


#Looping through a Dictionary

# Iterating over keys
for key in student.keys():
    print(key)  # Output: name, age, courses

# Iterating over values
for value in student.values():
    print(value)  # Output: Alice, 25, ['Math', 'Computer Science']

# Iterating over key-value pairs
for key, value in student.items():
    print(f'{key}: {value}')
    # Output:
    # name: Alice
    # age: 25
    # courses: ['Math', 'Computer Science']


#Dictionary Comprehensions
# Creating a dictionary using comprehension
squares = {x: x**2 for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtering dictionary comprehension
even_squares = {x: x**2 for x in range(6) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16}


#Nested Dictionaries
# A dictionary within a dictionary
students = {
    'student1': {'name': 'Alice', 'age': 25, 'courses': ['Math', 'Physics']},
    'student2': {'name': 'Bob', 'age': 22, 'courses': ['Biology', 'Chemistry']}
}

print(students['student1']['name'])  # Output: Alice

# Iterating over nested dictionaries
for student_id, info in students.items():
    print(f"Student ID: {student_id}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    # Output:
    # Student ID: student1
    #   name: Alice
    #   age: 25
    #   courses: ['Math', 'Physics']
    # Student ID: student2
    #   name: Bob
    #   age: 22
    #   courses: ['Biology', 'Chemistry']

#Default Dictionaries

from collections import defaultdict

# Creating a defaultdict with list as the default factory
dd = defaultdict(list)
dd['a'].append(1)
dd['b'].append(2)
dd['a'].append(3)

print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2]})

# Creating a defaultdict with int as the default factory
dd_int = defaultdict(int)
dd_int['a'] += 1
dd_int['b'] += 2

print(dd_int)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})

#Counter Dictionaries
from collections import Counter

# Counting the frequency of elements in a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)
print(counter)  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})

# Most common elements
print(counter.most_common(2))  # Output: [(4, 4), (3, 3)]
#Ordered Dictionaries

from collections import OrderedDict

# OrderedDict remembers the order of insertion
ordered_dict = OrderedDict()
ordered_dict['name'] = 'Alice'
ordered_dict['age'] = 25
ordered_dict['courses'] = ['Math', 'Computer Science']

print(ordered_dict)  # Output: OrderedDict([('name', 'Alice'), ('age', 25), ('courses', ['Math', 'Computer Science'])])

#Merging Dictionaries
# Using update() to merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merging dict2 into dict1
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Dictionary merging using the | operator (Python 3.9+)
dict3 = dict1 | dict2
print(dict3)  # Output: {'a': 1, 'b': 3, 'c': 4}

#Dictionary Views

# Accessing dictionary view objects
keys = student.keys()
values = student.values()
items = student.items()

# View objects are dynamic and reflect changes
student['grade'] = 'A'
print(keys)   # Output: dict_keys(['name', 'age', 'courses', 'grade'])
print(values) # Output: dict_values(['Alice', 25, ['Math', 'Computer Science'], 'A'])
'''clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''
