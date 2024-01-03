import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    new_color = (color.rgb.r / 255, color.rgb.g / 255, color.rgb.b / 255)
    rgb_colors.append(new_color)

# print(rgb_colors)

size = 20

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.forward(500)

for _ in range(size):
    tim.setheading(180)
    for _ in range(size):
        tim.dot(int(200 / size), random.choice(rgb_colors))
        tim.forward(500 / size)
    tim.setheading(0)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(500 / size)

screen = turtle.Screen()
screen.exitonclick()
