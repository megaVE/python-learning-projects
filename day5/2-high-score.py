# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_grade = 0
for n in range(0, len(student_scores)):
  if(student_scores[n] > highest_grade):
    highest_grade = student_scores[n]

print(f"The highest score in the class is: {highest_grade}")