import turtle
import random
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["blue", "green", "yellow", "red"]
for i in range(180):
    if i%2 == 0:
        turtle.circle(150)
        turtle.color(random.choice(colors))
        turtle.left(2)
    else:
        turtle.circle(-150)
        turtle.color(random.choice(colors))
        turtle.left(2)
turtle.done()