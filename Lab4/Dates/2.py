from datetime import datetime, timedelta

current_date = datetime.now()
tomorrow = current_date + timedelta(days=1)
yesterday = current_date - timedelta(days=1)

print("Today is:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow is:", tomorrow.strftime("%Y-%m-%d"))
print("Yesterday was:", yesterday.strftime("%Y-%m-%d"))

