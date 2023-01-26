#Global Variables
'''Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.'''

x = "great"
def myFunc():
    print("Casio is " + x)

myFunc()
print()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)