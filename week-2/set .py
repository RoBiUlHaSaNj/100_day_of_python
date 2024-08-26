'''1. What is a Set?
A set is an unordered collection of unique elements.
A set is a collection which is unordered, unchangeable*, and unindexed.
Sets are mutable, but they cannot contain mutable elements like lists, dictionaries, or other sets.
Duplicates Not Allowed
Creating a Set:'''

my_set = {1, 2, 3, 4,4, 5}
print(my_set)

#An empty set is created using the set() function, not {}, as {} creates an empty dictionary.


empty_set = set()

'''2. Basic Operations
Adding Elements: Use add() to add a single element.'''

my_set.add(6)

'''Removing Elements:

remove(): Removes a specific element. Raises KeyError if the element is not found.'''

my_set.remove(3)
#discard(): Removes a specific element. Does not raise an error if the element is not found.


my_set.discard(10)


#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#pop(): Removes and returns an arbitrary element. Raises KeyError if the set is empty.


removed_element = my_set.pop()

#clear(): Removes all elements from the set.

my_set.clear()

'''3. Set Operations
Union (|): Combines elements from two sets (all unique elements).'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}

#Intersection (&): Returns common elements in both sets.

intersection_set = set1 & set2  # Output: {3}

#Difference (-): Returns elements that are in the first set but not in the second.

difference_set = set1 - set2  # Output: {1, 2}

#Symmetric Difference (^): Returns elements in either set, but not in both.

sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
'''4. Set Methods
union(): Returns the union of sets.'''

union_set = set1.union(set2)

#intersection(): Returns the intersection of sets.


intersection_set = set1.intersection(set2)

#difference(): Returns the difference of sets.


difference_set = set1.difference(set2)

#symmetric_difference(): Returns the symmetric difference of sets.


sym_diff_set = set1.symmetric_difference(set2)

#issubset(): Checks if one set is a subset of another.

set1 = {1, 2, 3}
set2 = {1, 2}

is_subset = set2.issubset(set1)  # Output: True

#issuperset(): Checks if one set is a superset of another.


is_superset = set1.issuperset(set2)  # Output: True
#isdisjoint(): Checks if two sets have no elements in common.


set3 = {4, 5, 6}
disjoint = set1.isdisjoint(set3)  # Output: True

'''5. Frozen Sets
A frozenset is an immutable version of a set. Once created, elements cannot be added or removed.'''

frozen = frozenset([1, 2, 3])

'''6. Common Use Cases
Removing Duplicates: Convert a list with duplicates to a set.'''

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)  # Output: {1, 2, 3, 4, 5}

#Membership Testing: Checking if an element is in a set is more efficient than in a list.

if 3 in my_set:
    print("3 is in the set")
'''7. Iterating Through a Set
Looping through the elements of a set is possible, but remember that the order is not guaranteed.'''

for element in my_set:
    print(element)

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



'''
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # {3}

# Difference
print(set1 - set2)  # {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # {1, 2, 4, 5}


'''
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	             Shortcut	       Description
add()	 	                   Adds an element to the set
clear()	 	                   Removes all the elements from the set
copy()	 	                   Returns a copy of the set
difference()	         -	   Returns a set containing the difference between two or more sets
difference_update()	    -=	   Removes the items in this set that are also included in another, specified set
discard()	 	               Remove the specified item
intersection()	        &	   Returns a set, that is the intersection of two other sets
intersection_update()	&=	   Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	           Returns whether two sets have a intersection or not
issubset()	           <=	   Returns whether another set contains this set or not
 	                    <	  Returns whether all items in this set is present in other, specified set(s)
issuperset()	        >=	 Returns whether this set contains another set or not
 	                   >	 Returns whether all items in other, specified set(s) is present in this set
pop()	 	                   Removes an element from the set
remove()	 	               Removes the specified element
symmetric_difference()	^	   Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	   Inserts the symmetric differences from this set and another
union()                      	|	   Return a set containing the union of sets
update()	                  |=	  Update the set with the union of this set and others'''
