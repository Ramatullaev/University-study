# Создаем свой тип данных

# parent class
class User:
    def __init__(self, name , age):
        def.name = name
        def.age = age

    def run(self):
        print("run run User")


# child class
class Student:
    

    def __init__(self, id, name):
        self.name = name
        self.id = id

    def learning(self):
        print(f"study time , {self.name}")

    def __str__(self):
        return self.name + str(self.id)

stud = Student(123 , "Jonh")
stud.learning()

print(type(stud))

print(stud)

