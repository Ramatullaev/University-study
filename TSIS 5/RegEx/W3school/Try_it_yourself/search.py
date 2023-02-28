# Search for the first white-space character in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 





'If no matches are found, the value None is returned:'
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


