class Car:
    insurance = input()
    def __init__(self, engine, mark, color):
        self.engine = engine
        self.mark = mark
        self.color = color

    def printInfo(self):
        return f"{self.engine}, {self.mark}, {self.color}"

    def settter(self, insurance):
        self.insurance = insurance
    
    def getter(self):
        return self.insurance

t1 = Car("full", "camry", "white")
print(t1.printInfo())

class Toyota(Car):
    price = input()
    def __init__(self, country, engine, mark, color):
        self.country = country
        #self._price = price
        super().__init__(engine, mark, color)
    def printInfo(self):
        return f"{self.country}, {self.engine}, {self.mark}, {self.color}"

    def settter(self, price):
        self.price = price
    
    def getter(self):
        return self.price

x = Toyota("Japan", "full", "camry", "white")
print(x.printInfo())
print(t1.getter())
print(x.getter())




