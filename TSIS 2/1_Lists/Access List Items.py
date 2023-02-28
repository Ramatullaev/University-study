# Print the second item of the list:

gimme = ["apple", "banana", "cherry"]
print(gimme[1])  # will be: banana

# Negative Indexing 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])   # will be: cherry

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[2:5])     # will be: ['cherry', 'orange', 'kiwi']
# Remember that the first item has index 0

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])    # will be: ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])   # will be: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # will be: ['orange', 'kiwi', 'melon']

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")