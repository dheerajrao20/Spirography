import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("blue")
turtle.bgcolor("black")
def shape(angle, side, limit):
    rd = 200
    turtle.forward(side)
    if side%(rd*2) ==0:
        angle += 2
    elif side % rd == 0:
        angle -= 2
    turtle.right(angle)
    side += 2
    if side < limit:
        shape(angle, side, limit)
angle = 135
side = 1
limit = 600
shape(angle, side, limit)
turtle.done()
