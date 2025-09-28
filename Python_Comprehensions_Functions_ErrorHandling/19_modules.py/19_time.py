import time

local_time = time.localtime()
print(local_time)

readable_time = time.asctime(local_time)
print(readable_time)