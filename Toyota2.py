class Car:
  def __init__(self, engine, mark, color):
    self.engine = engine
    self.mark = mark
    self.color = color

  def printInfo(self):
    return f"{self.engine}, {self.mark}, {self.color}"

t1 = Car("full" , "camry" , "white")
print(t1.printInfo())

class Toyota(Car):
    def __init__(self, contry, engine, mark, color):
        self.contry = contry
        Car.__init__(engine, mark, color)

x = Toyota("Japan", self.engine, self.mark, self.color)
print(x.printInfo())