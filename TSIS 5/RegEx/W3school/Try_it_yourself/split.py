# The split() function returns a list where the string has been split at each match:

'Split at each white-space character:'
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)                            # will be: ['The', 'rain', 'in', 'Spain']



'You can control the number of occurrences by specifying the maxsplit parameter:'
# Split the string only at the first occurrence:
import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)                            # will be: ['The', 'rain in Spain']





