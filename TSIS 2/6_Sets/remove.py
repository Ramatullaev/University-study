# Remove Set Items
'''To remove an item in a set, use the remove(), or the discard() method.'''

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)  
'# Note: If the item to remove does not exist, remove() will raise an error.'

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)  
'Note: If the item to remove does not exist, discard() will NOT raise an error.'


''' You can also use the pop() method to remove an item, but 
this method will remove a random item, so you cannot be sure what item that gets removed.'''
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

print(thisset)  # в сетах метод pop() убирает рандомный предмет

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset

print(thisset)








