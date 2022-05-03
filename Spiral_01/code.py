import turtle
import time
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(1,9):
    for colors in ["red", "green", "yellow", "blue", "orange", "cyan"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
time.sleep(10)