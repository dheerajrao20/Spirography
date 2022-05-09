import turtle
turtle.pensize(2)
turtle.speed(0)
turtle.bgcolor("black")
for i in range(80):
    if i%2 ==0:
        turtle.circle(150)
        turtle.color("blue")
        turtle.left(25)
    else:
        turtle.circle(150)
        turtle.color("red")
        turtle.left(25)
turtle.done()