# Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

'''Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''

# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])   # will be: Ford

'''Changeable
Dictionaries are changeable, meaning that we can change, 
add or remove items after the dictionary has been created.'''

# Duplicates Not Allowed
'Dictionaries cannot have two items with the same key:'
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,   
  "year": 2020    
}
print(thisdict)   # will be: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))  # will be: 3

# Data type
'The values in dictionary items can be of any data type:'
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Type()
# <class 'dict'>

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# The dict() Constructor
' It is also possible to use the dict() constructor to make a dictionary. '

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Python Collections (Arrays)
'''There are four collection data types in the Python programming language:

List - is a collection which is ordered and changeable. Allows duplicate members.
Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary - is a collection which is ordered** and changeable. No duplicate members.'''

