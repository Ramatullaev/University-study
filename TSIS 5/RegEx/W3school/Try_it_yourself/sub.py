'The sub() function replaces the matches with the text of your choice:'
# Replace every white-space character with the number 9:
import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)                            # will be: The9rain9in9Spain



'You can control the number of replacements by specifying the count parameter:'
# Replace the first 2 occurrences:
import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)                                # will be: The9rain9in Spain






