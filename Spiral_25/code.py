import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.pencolor("blue")
def dc(rad):
    for i in range(10):
        turtle.circle(rad)
        rad -= 4
def dd():
    for i in range(10):
        dc(150)
        turtle.right(36)
dd()
turtle.done()