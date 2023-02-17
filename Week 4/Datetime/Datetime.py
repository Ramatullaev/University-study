# Python Dates
'''A date in Python is not a data type of its own, but we can 
import a module named datetime to work with dates as date objects.'''

import datetime

x = datetime.datetime.now()
print(x)                    # will be: 2023-02-17 11:35:08.062249


# Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)             # will be: 2023
print(x.strftime("%A"))   # will be: Friday

# Create a date object:
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
'''The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, 
format, to specify the format of the returned string:'''

# Display the name of the month:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))    # will be: June


 
