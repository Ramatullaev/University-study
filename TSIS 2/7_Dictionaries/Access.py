# Get Keys
'The keys() method will return a list of all the keys in the dictionary.'
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# Get Values
'Get a list of the values:'
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)       # will be: dict_values(['Ford', 'Mustang', 1964])



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change 

# will be: dict_values(['Ford', 'Mustang', 1964])
# will be: dict_values(['Ford', 'Mustang', 2020])

# Get Items
'The items() method will return each item in a dictionary, as tuples in a list.'
