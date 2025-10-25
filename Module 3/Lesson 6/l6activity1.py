import random
import time

def get_random_date(stardate, enddate):
    print(f"Printing random date between {stardate} and {enddate}")
    randomGenerator = random.random()
    dateformat = "%m/%d/%y"
    starttime = time.mktime(time.strptime(stardate, dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateformat, time.localtime(randomTime))
    return randomDate

print(f"Random Date = {get_random_date(1/1/2020, 12/12/2024)}")