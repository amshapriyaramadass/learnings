import calendar

if __name__ == '__main__':

    mm,dd,yy=list(map(int,input().split()))

    wd=calendar.weekday(yy,mm,dd)
    print(wd)
    week=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    print(week[wd]) 