from random import randint
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def run_game(turtles_array):
    while True:
        for turtle in turtles_array:
            turtle.forward(randint(0, 10))
            if turtle.xcor() > 230:
                return turtle


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

turtles = []
for position in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[position])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-70 + position * 30))
    turtles.append(new_turtle)

winner = run_game(turtles).pencolor()

if winner == user_bet:
    print("You won!")
else:
    print(f"You lost! The {winner} turtle was the winner.")

screen.exitonclick()
