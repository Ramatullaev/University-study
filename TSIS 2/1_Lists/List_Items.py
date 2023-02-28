thislist = ["apple", "banana", "cherry"]
print(thislist)  # will be: ['apple', 'banana', 'cherry']
print(thislist[0])  # will be: apple 

# If you add new items to a list, the new items will be placed at the end of the list

# Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)   # will be: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))   # will be 3

# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
