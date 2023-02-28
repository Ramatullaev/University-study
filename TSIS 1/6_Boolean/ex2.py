bool("abc")   # will be: True
bool(123)   # will be: True
bool(["apple", "cherry", "banana"])   # will be : True

bool(False)  # will be: False
bool(None)   # will be: False
bool(0)   # will be: False
bool("")   # will be: False
bool(())  # will be: False
bool([])   # will be: False
bool({})   # will be: False

'''Python also has many built-in functions that return a boolean value, like the 
isinstance() function, which can be used to determine if an object is of a certain data type:'''

x = 200
print(isinstance(x, int)) # will be: True

