'''Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:'''

# Remove the file "demofile.txt":
import os
os.remove("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt")

'''Check if File exist:
To avoid getting an error, you might want to check 
if the file exists before you try to delete it:'''

# Check if file exists, then delete it:
import os
if os.path.exists("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt"):
  os.remove("/Users/snezhok/Desktop/PP2/TSIS 6/w3school/demofile.txt")
else:
  print("The file does not exist")

'''Delete Folder
To delete an entire folder, use the os.rmdir() method:'''

import os
os.rmdir("mafolder")

# Note: You can only remove empty folders.
