from datetime import datetime, timedelta

x = datetime.now()
y = timedelta(microseconds=x.microsecond)
w = x - y
w = w.replace(microsecond=0)

print(w)