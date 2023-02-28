class Shape():
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length ** 2
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def area99(self):
        return self.length * self.width
t = Rectangle(int(input()) , int(input()))
print(t.area99())