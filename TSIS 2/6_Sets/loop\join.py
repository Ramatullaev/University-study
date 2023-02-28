# Loop Sets

'''You can loop through the set items by using a for loop:'''
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Sets
'''You can use the union() method that returns a new set containing all items from
both sets, or the update() method that inserts all the items from one set into another'''

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.

