import datetime

date1 = input("Write the year, month and day of the first date: ")
d1 = list(int(x) for x in date1.split())
x = datetime.datetime(d1[0], d1[1], d1[2])

date2 = input("Write the year, month and day of the second date: ")
d2 = list(int(x) for x in date2.split())
y = datetime.datetime(d2[0], d2[1], d2[2])

time_difference = abs(y - x)
seconds_difference = time_difference.total_seconds()

print(f"Time difference in seconds: {seconds_difference}")

