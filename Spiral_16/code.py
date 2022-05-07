import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor("black")
turtle.pencolor("blue")
def shape(angle, side, limit):
    rd = 200
    turtle.forward(side)
    if side%(rd*2) == 0:
        angle += 2
    elif side % rd == 0:
        angle -= 2
    turtle.right(angle)
    side += 2
    if side < limit:
        shape(angle, side, limit)
angle = 119
side = 0
limit = 9000
shape(angle, side, limit)
turtle.done()