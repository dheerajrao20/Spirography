import turtle
turtle.setworldcoordinates(-100, -100, 350, 180)
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.color( "blue")
turtle.begin_fill()
while True:
    turtle.forward(250)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()