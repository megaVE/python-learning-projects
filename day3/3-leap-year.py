# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if(year % 4 == 0):
  if(not(year > 100 and year % 100 == 0) or (year > 400 and year % 400 == 0)):
    print("Leap year")
  else:
    print("Not leap year")
else:
  print("Not leap year")