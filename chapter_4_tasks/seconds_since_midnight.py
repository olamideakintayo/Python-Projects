# seconds_since_midnight.py

def seconds_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    return hour_in_seconds + minute_in_seconds + second


print(seconds_since_midnight(13, 30, 45))  