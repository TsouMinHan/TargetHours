import time
import datetime

now = time.time()
print(now)

a = datetime.datetime.strftime(now, "%H:%M:%S")
print(a)