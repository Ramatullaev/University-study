class Car:
    def __init__(self, engine, mark, color):
        self.engine = engine
        self.mark = mark
        self.color = color

    def printInfo(self):
        return f"{self.engine}, {self.mark}, {self.color}"

t1 = Car("full", "camry", "white")
print(t1.printInfo())

class Toyota(Car):
    def __init__(self, country, engine, mark, color):
        self.country = country
        super().__init__(country, engine, mark, color)

x = Toyota("Japan", "full", "camry", "white")
print(x.printInfo())