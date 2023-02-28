# List objects have a sort() method that will sort the list 
# alphanumerically, ascending, by default:
thislist = ["zrange", "dango", "ciwi", "aineapple", "banana"]
thislist.sort()
print(thislist)   # will be: ['aineapple', 'banana', 'ciwi', 'dango', 'zrange']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)    # will be: [23, 50, 65, 82, 100]

#Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist = ["zrange", "dango", "ciwi", "aineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)    # will be: ['zrange', 'dango', 'ciwi', 'banana', 'aineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)   # will be: [100, 82, 65, 50, 23]

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)    # will be: [50, 65, 23, 82, 100]

'''Case Insensitive Sort
By default the sort() method is case sensitive,
 resulting in all capital letters being sorted before lower case letters:'''
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)   # will be: ['Kiwi', 'Orange', 'banana', 'cherry']

# if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

'''Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)   # will be: ['cherry', 'Kiwi', 'Orange', 'banana']

