print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
t = (name1 + name2).lower().count('t')
r = (name1 + name2).lower().count('r')
u = (name1 + name2).lower().count('u')
e = (name1 + name2).lower().count('e')
l = (name1 + name2).lower().count('l')
o = (name1 + name2).lower().count('o')
v = (name1 + name2).lower().count('v')

score = 10 * (t + r + u + e) + (l + o + v + e)

if(score < 10 or score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")