import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor("black")
turtle.pencolor("blue")
def star(leftangle, rightangle, distance):
    for i in range(5):
        turtle.left(leftangle)
        turtle.forward(distance)
        turtle.right(rightangle)
        turtle.forward(distance)
for i in range(89):
    star(58, 130, 150)
    turtle.right(89)
turtle.done()