''' Tuples are unchangeable, meaning that you cannot 
change, add, or remove items once the tuple is created.

But there are some workarounds.'''

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add items
# tuples they do not have a build-in append() method

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Add tuple to a tuple.
'''Create a new tuple with the value "orange", and add that tuple:'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
'''Note: When creating a tuple with only one item, remember to 
include a comma after the item, otherwise it will not be identified as a tuple'''

# Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # this will raise an error because the tuple no longer exists



