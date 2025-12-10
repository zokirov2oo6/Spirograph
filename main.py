from turtle import Turtle, Screen
import random

t = Turtle()

t.speed(0)

screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(100):
    t.color(random_color())
    t.circle(100)
    t.left(3.6)

screen.update()
screen.exitonclick()