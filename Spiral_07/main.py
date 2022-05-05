import turtle
turtle.hideturtle()
import time
def func(t):
    for i in range(1, 5):
        t.forward(150)
        t.right(90)
def art():
    turtle.bgcolor("black")
    turtle.pencolor("blue")
    turtle.pensize(2)
    turtle.speed(0)
    for i in range(130):
        func(turtle)
        turtle.right(17)
art()
time.sleep(10)
