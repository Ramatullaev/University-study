'''List comprehension offers a shorter syntax when 
you want to create a new list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing 
only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for 
statement with a conditional test inside:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  # will be: ['apple', 'banana', 'mango']
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)   # will be: ['banana', 'cherry', 'kiwi', 'mango']
'''The condition if x != "apple"  will return True for all elements 
other than "apple", making the new list contain all fruits except "apple".'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)


