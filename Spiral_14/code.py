import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("blue")
turtle.bgcolor("black")
def shape(angle, side, limit):
    rd = 200
    turtle.forward(side)
    if side%(rd*2) == 0:
        angle += 2
    elif side % rd == 0:
        angle -= 2
    turtle.right(angle)
    side += 7
    if side < limit:
        shape(angle, side, limit)
angle = 179
side = 1
limit = 1000
shape(angle, side, limit)
turtle.done()
