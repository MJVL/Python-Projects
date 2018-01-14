from datetime import datetime

now = datetime.now()

print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.date())

print('%s/%s/%s' % (now.month, now.day, now.year))

print(now.hour)
print(now.minute)
print(now.second)

print('%s:%s:%s' % (now.hour, now.minute, now.second))

