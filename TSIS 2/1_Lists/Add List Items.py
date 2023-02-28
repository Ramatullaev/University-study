# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)    # will be: ['apple', 'banana', 'cherry', 'orange']

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)   # will be: ['apple', 'orange', 'banana', 'cherry']

# EXTEND LIST
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # will be: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
