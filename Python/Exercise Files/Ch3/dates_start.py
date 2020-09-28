#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  # print("today date is", today) 

  # # print out the date's individual components
  # print("this is date components",today.day,today.month,today.year)
  
  # # retrieve today's weekday (0=Monday, 6=Sunday)
  # print("this is weekday",today.weekday()) 
  # days=("mon","tue","wed","thu","fri","sat","sun")
  # print("today day is",days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  todaydatetime=datetime.now()
  print("today's time is",todaydatetime)


  # Get the current time
  time=datetime.time(datetime.now()) 
  print("time,",time)

  
if __name__ == "__main__":
  main();
  