# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

file = open('/Users/snezhok/Desktop/PP2/TSIS 5/Lab 5/Regex/row.txt', 'r')

result = re.findall(".*a.*b*", file.read())
print(result)