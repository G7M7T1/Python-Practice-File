import datetime

print(datetime.datetime.now())

x = datetime.datetime.now()

print(x)

print(x.year)

print(x.month)

print(x.day)

print(x.hour)
print(x.minute)

print(x.second)

print(x.microsecond)


# --------------------------------------

now = datetime.datetime.now()
oneday = datetime.datetime(2020, 1, 1)
diff = now - oneday

print(diff)