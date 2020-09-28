#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365,hours=3,minutes =1))

# print today's date
today=date.today()
print("today date is:,", today)

# print today's date one year from now
print("today's date one year from now:", today+timedelta(days=365))

# create a timedelta that uses more than one argument
print("2 weeks 3 days from now",today+timedelta(days =3, weeks=2))

# calculate the date 1 week ago, formatted as a string
t=datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d,%Y")
print("week ago date is :"+ s)

### How many days until April Fools' Day?
today = date.today()
afd= date(today.year, 4,1)
print("afd is ", afd)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
   print("April fools day is passed %d days" % ((today -afd).days)) 
   afd=afd.replace(year=today.year+1)

print("april fool days:", afd)   


# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd-today
print("its is just", time_to_afd.days,"until next April fool day")

