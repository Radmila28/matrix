from turtle import *

window = Screen()
t = Turtle()
t.speed(1000)
t.penup()
t.goto(-200, -200)
t.pendown()


def fractal(l, d):
    if d == 0:
        for i in range(0, 3):
            t.fd(l)
            t.left(120)
    else:
        fractal(l / 2, d - 1)
        t.fd(l / 2)
        fractal(l / 2, d - 1)
        t.bk(l / 2)
        t.left(60)
        t.fd(l / 2)
        t.right(60)
        fractal(l / 2, d - 1)
        t.left(60)
        t.bk(l / 2)
        t.right(60)


fractal(1000, 7)
window.exitonclick()