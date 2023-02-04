# Remove Items

'The pop() method removes the item with the specified key name:'
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)   # will be: {'brand': 'Ford', 'year': 1964}

# The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)    # will be: {'brand': 'Ford', 'model': 'Mustang'}

'The del keyword removes the item with the specified key name:'
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
'#this will cause an error because "thisdict" no longer exists.'

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)   # will be: {}


