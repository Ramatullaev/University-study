from datetime import datetime

# create a datetime object with microseconds
dt = datetime.now()

# drop microseconds from the datetime object
dt_without_micros = dt.replace(microsecond=0)

print("With microsecond:", dt)
print("Without microsecond:", dt_without_micros)