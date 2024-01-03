from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# Challenge 1: Draw a Square

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# Challenge 2: Draw a Dashed Line

# for _ in range(5):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(15)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(15)

# Challenge 3: Drawing Different Shapes

# for sides in range(3, 10):
#     for _ in range(sides):
#         timmy_the_turtle.forward(50)
#         timmy_the_turtle.right(360 / sides)

# Challenge 4: Generate a Random Walk

# from random import choice, random
#
# for steps in range(30):
#     timmy_the_turtle.color((random(), random(), random()))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.right(choice([0, 90, 180, -90]))

# Challenge 5: Draw a Spirograph

# from random import random
#
# timmy_the_turtle.speed('fastest')
# circles = 720
#
# for _ in range(circles):
#     timmy_the_turtle.color((random(), random(), random()))
#     timmy_the_turtle.circle(50)
#     timmy_the_turtle.left(360 / circles)

screen = Screen()
screen.exitonclick()
