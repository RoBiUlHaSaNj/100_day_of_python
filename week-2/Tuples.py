
'''Definition:

A tuple is a collection of items that are ordered and unchangeable (immutable).
Tuples are similar to lists, but unlike lists, once a tuple is created, it cannot be modified.'''


#Tuples are defined by enclosing the elements in parentheses ().


# Example of a tuple
my_tuple = (1, 2, 3, "apple", True)
print(my_tuple)

'''1. Accessing Elements in a Tuple
Just like lists, you can access elements in a tuple using indexing.'''


fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Accessing the first element
print(fruits[2])  # Accessing the third element

# Negative Indexing: You can also use negative indexing to access elements from the end of the tuple.

print(fruits[-1])  # Last element
print(fruits[-2])  # Second last element

'''2. Slicing a Tuple
You can access a range of elements in a tuple by slicing.'''


my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Elements from index 1 to 3
print(my_tuple[:3])   # Elements from start to index 2
print(my_tuple[2:])   # Elements from index 2 to the end


'''3. Unpacking a Tuple
Unpacking allows you to assign tuple elements to individual variables.'''


# Unpacking a tuple

person = ("John", 25, "Engineer")
name, age, profession = person
print(name)
print(age)
print(profession)

#You can also unpack part of a tuple and assign the rest to another variable using the * operator.

numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print(a)     # 1
print(b)     # 2
print(rest)  # [3, 4, 5]


'''4. Tuples are Immutable
Once a tuple is created, you cannot modify its elements (no addition, deletion, or change).'''


fruits = ("apple", "banana", "cherry")
# fruits[0] = "orange"  # This will raise a TypeError

# However, you can concatenate tuples to create a new one
new_fruits = fruits + ("orange", "grape")
print(new_fruits)


'''5. Looping Through a Tuple
You can loop through the elements of a tuple using a for loop.'''



fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

'''6. Tuple Methods
Tuples have only two built-in methods:

count(): Returns the number of times a specified value occurs in a tuple.'''

numbers = (1, 2, 3, 1, 4, 1)
print(numbers.count(1))  # Output: 3

#index(): Searches the tuple for a specified value and returns the position of where it was found.

numbers = (1, 2, 3, 4, 5)
print(numbers.index(3))  # Output: 2

#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

'''Since tuples are immutable, they do not have a built-in append() 
method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can 
convert it into a list, add your item(s), and convert it back into a tuple.


Convert the tuple into a list, add "orange", and convert it back into a tuple:'''

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)



'''2. Add tuple to a tuple. You are allowed to add tuples to tuples, 
so if you want to add one item, (or many), create a new tuple with the item(s), 
and add it to the existing tuple:


Create a new tuple with the value "orange", and add that tuple:'''

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


'''Nested Tuples:

Tuples can contain other tuples as elements, which allows for the creation of complex data structures.'''

nested_tuple = (1, 2, (3, 4), (5, (6, 7)))
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[3][1])  # Output: (6, 7)


'''Tuple Packing:

You’ve covered unpacking, but packing refers to assigning multiple values to a single tuple in one line.'''

my_tuple = 1, 2, "apple"  # Tuple packing without parentheses
print(my_tuple)

'''Returning Multiple Values from a Function:

Tuples are often used to return multiple values from a function.'''

def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20
#Using Tuples as Dictionary Keys:

#Since tuples are immutable, they can be used as keys in dictionaries, unlike lists.

coordinates = {(10, 20): "Location A", (30, 40): "Location B"}
print(coordinates[(10, 20)])  # Output: Location A
