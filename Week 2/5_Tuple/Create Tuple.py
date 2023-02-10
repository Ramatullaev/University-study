# Create Tuple With One Item
'''To create a tuple with only one item, you have to add a 
comma after the item, otherwise Python will not recognize it as a tuple.'''

# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))    # will be: <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))    # will be: <class 'str'>

# Tuple Items - Data Types
# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")   # <class 'tuple'>
tuple2 = (1, 5, 7, 9, 3)        # <class 'tuple'>
tuple3 = (True, False, False)     # <class 'tuple'>

# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

''' List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members. '''

