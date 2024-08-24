#1. Introduction to Lists
'''
Definition: A list is a collection of items that are ordered,
changeable, and allow duplicate values.
Creating Lists: Use square brackets [] to create a list. start from 0
'''
my_list = [1, 2, 3, "apple", True]

print(my_list)
print(len(my_list))

#2. Accessing Elements

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First element
print(fruits[2])  # Third element
print(my_list[5-1])


print(fruits[-1])  # Last element
print(fruits[-2])  # Second last element

#3. Slicing a List
#slicing allows you to access a subset of elements in a list.

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Elements from index 1 to 3

print(numbers[::2])  # Every second element

#Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#4. Modifying Elements
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#5. Adding Elements

fruits.append("orange")
print(fruits)


fruits.insert(1, "banana")
print(fruits)

fruits.extend(["mango", "grape"])
print(fruits)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#6. Removing Elements

fruits.remove("banana")
print(fruits)

last_fruit = fruits.pop()  # Removes the last element
print(last_fruit)
print(fruits)


del fruits[0]  # Removes the first element
print(fruits)


#7. Finding Elements

index = fruits.index("cherry")
print(index)


fruits.append("mango")
count = fruits.count("mango")
print(count)

#8. Sorting and Reversing

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)


numbers.reverse()
print(numbers)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#9. List Comprehensions

squares = [x**2 for x in range(10)]
print(squares)


even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)


#10. Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)


#11. Common List Operations

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Repetition
repeated_list = list1 * 3
print(repeated_list)

#Membership

print(2 in list1)  # True
print(5 in list1)  # False

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1



#Copy a List

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#Use the slice Operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)





'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
