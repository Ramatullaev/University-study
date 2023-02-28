'''If you have only one statement to execute, 
you can put it on the same line as the if statement.'''

if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# The and keyword is a logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")