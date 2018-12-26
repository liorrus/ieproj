import datetime
import random

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
end = datetime.datetime.now()
start = datetime.datetime(2018, 1, 1, 12, 30, 59, 0)
print (start, end)

for i in range(1,1000):

    i=random_date(start, end)
    print(i)
