import time as t

t.localtime()
time_now = t.localtime()

print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) +  "m")
