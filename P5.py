#Program 5                         #ALIZAR

days=int(input('Enter The Number Of Days : '))
month=days/30
year=month/12
day=days%30
if year is not 0:
    month=month%12
print(int(year),'Years',int(month),'Months And',int(day),'Days')
