from datetime import datetime

time_now = datetime.now()
print(time_now)

#formatted output 1
formatted_time = time_now.strftime("%Y-%m-%dT%H:%M:%S")
print(formatted_time)

#formatted output 2
formatted_time_v2 = time_now.isoformat(timespec='seconds')
print(formatted_time_v2)