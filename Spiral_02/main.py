import turtle
import time
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(1,99):
    for colours in ["red", "green", "yellow", "blue", "orange", "lime", "cyan"]:
        turtle.color(colours)
        turtle.circle(1000)
        turtle.left(10)
time.sleep(100)

