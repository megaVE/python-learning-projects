def is_leap(year):
  return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month == 2:
    return 29
  else:
    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

