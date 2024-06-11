import datetime
start = datetime.datetime.strptime("1970-01-01", "%Y-%m-%d")
print((datetime.datetime.now().year - start.year) * 12 + datetime.datetime.now().month - start.month)