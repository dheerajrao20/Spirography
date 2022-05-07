import turtle
turtle.pencolor("blue")
turtle.bgcolor("black")
turtle.speed(0)
x = 0
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
while x<120:
    for i in range(60):
        turtle.forward(200)
        turtle.right(61)
    turtle.right(11.11)
    x += 1
turtle.done()