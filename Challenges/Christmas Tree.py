import turtle
from random import randint, choice

t = turtle.Turtle()


def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.end_fill()


def drawTree():
    for _ in range(1):
        # go random along the x axis
        t.penup()
        t.setheading(90)
        choice([t.left, t.right])(90)
        t.setheading(0)
        t.forward(randint(-100, 100))
        t.pendown()

        # draw the trunk
        drawRectangle(t, 10, h := randint(10, 20), "brown")
        t.setheading(90)
        t.forward(h)
        t.left(90)
        t.forward((h * 5 - h) / 2)
        t.setheading(0)

        # draw the leaves
        for i in range(3):
            drawTriangle(t, k := (h * 5 - i * 3), choice(["green", "red", "yellow"]))
            t.penup()
            t.forward(k / 2)
            t.setheading(90)
            t.forward(k / 2)
            t.setheading(180)
            t.forward((k - (i * 3 + 1)) / 2)
            t.setheading(0)
            t.pendown()


for i in range(5):
    drawTree()

turtle.done()
