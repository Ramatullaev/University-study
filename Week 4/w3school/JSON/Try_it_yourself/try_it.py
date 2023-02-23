# Python has a built-in package called json, which can be used to work with JSON data.
import json

'''Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.'''

#Convert from JSON to Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Convert from Python to JSON:
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


'''You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None'''


#Convert Python objects into JSON strings, and print the values:
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

Python	                JSON
dict	                Object
list	                Array
tuple               	Array
str	                    String
int	                    Number
float	                Number
True	                true
False	                false
None	                null


