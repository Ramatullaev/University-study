# Functions
'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''

# In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")   # will be: The youngest child is Linus




