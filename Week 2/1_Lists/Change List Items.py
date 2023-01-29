# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)    # will be: ['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
print(thislist)   # will be: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # will be: ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)   # will be: ['apple', 'watermelon']

# Insert Items
'''To insert a new list item, without replacing any of the
existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)   # will be: ['apple', 'banana', 'watermelon', 'cherry']