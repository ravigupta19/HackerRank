from calendar import weekday
date = input().split()
day,month,year = int(date[1]),int(date[0]),int(date[2])
listofdays= ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
index = weekday(year,month,day)
print(listofdays[index])
