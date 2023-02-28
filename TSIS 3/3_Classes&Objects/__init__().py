# The __init__() Function

''' Create a class named Person, use the __init__() 
function to assign values for name and age:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# The __str__() Function
'The string representation of an object WITHOUT the __str__() function:'

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

'The string representation of an object WITH the __str__() function:'
print()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.score = 120

  def __str__(self):
    return f"{self.name}({self.age} : {self.score})"

p1 = Person("John", 36)

print(p1)



