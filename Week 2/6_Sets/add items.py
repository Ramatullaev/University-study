# Add Set Items

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

''' To add items from another set into the current set, use the update() method.'''
# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
