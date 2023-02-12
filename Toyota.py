class Car:
  def __init__(self, engine, mark, color):
    self.engine = engine
    self.mark = mark
    self.color = color

  def __str__(self):
    return f"{self.engine}, {self.mark}, {self.color}"

t1 = Car("full" , "camry" , "white")
print(t1.engine)
print(t1.mark)
print(t1.color)

