class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(other, x, y):
        other.x = x
        other.y = y

    def dist(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

p1 = Point(int(input()),int(input()))
p1.show()
p2 = Point(int(input()),int(input()))
print(p1.dist(p2))


