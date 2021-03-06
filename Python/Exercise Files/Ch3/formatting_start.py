#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  #### Date Formatting ####
  now=datetime.now()
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  # print(now.strftime("toyda date is ,%d/%b/%y"))
  # print(now.strftime("format date , %a ,%b, %d, %y"))

  # # %c - locale's date and time, %x - locale's date, %X - locale's time
  # print(now.strftime("locate date and time: %c"))
  # print(now.strftime("locate date: %x"))
  # print(now.strftime("locate time: %X"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Time format: %I:%M:%S %p"))
  print(now.strftime(" 24 Time format: %H:%M"))





if __name__ == "__main__":
  main();
