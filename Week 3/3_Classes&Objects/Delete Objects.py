# Delete Objects

'You can delete objects by using the del keyword:'

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)

# The pass Statement

'''class definitions cannot be empty, but if you for some reason have a class 
definition with no content, put in the pass statement to avoid getting an error.'''

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement

