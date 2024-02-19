from turtle import Turtle, Screen


def painting_reset():
    tim.home()
    tim.clear()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.right(10)


tim = Turtle()

screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=painting_reset)
screen.exitonclick()
