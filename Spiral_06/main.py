import turtle
import time
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
distance = 0
for i in range(120):
    turtle.forward(distance)
    turtle.left(90)
    turtle.pencolor("red")
    distance += 1
time.sleep(10)