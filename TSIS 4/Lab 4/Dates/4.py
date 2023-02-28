from datetime import datetime

# Get the two dates from the user
date1_str = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

# Convert the date strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Calculate the difference between the two dates in seconds
diff = (date2 - date1).total_seconds()

# Print the result
print("The difference between the two dates is", diff, "seconds.")