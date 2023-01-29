# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]   # will be: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''Same example, but with a condition:
Accept only numbers lower than 5:'''
newlist = [x for x in range(10) if x < 5]   # will be: [0, 1, 2, 3, 4]

#Expression
'''The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)    # will be: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]   
print(newlist)  # will be: ['hello', 'hello', 'hello', 'hello', 'hello']

# "Return the item if it is not banana, if it is banana return orange".

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)     # will be: ['apple', 'orange', 'cherry', 'kiwi', 'mango']



