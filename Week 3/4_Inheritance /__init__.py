# Add the __init__() Function

'''The __init__() function is called automatically 
every time the class is being used to create a new object.'''

# Add the __init__() function to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
    #add properties etc.

'''To keep the inheritance of the parent's __init__() 
function, add a call to the parent's __init__() function:'''
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

        


