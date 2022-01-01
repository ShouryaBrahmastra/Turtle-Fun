import turtle as t

pen = t.Turtle()
pen.color("cyan")
pen.speed(0)
colors = ["red", "black", "cyan", "purple",
          "green", "black", "orange", "navy"]


def square_fun(color):
    for side in range(4):
        pen.forward(100)
        pen.right(90)
        for side in range(4):
            pen.forward(50)
            pen.right(90)


pen.penup()
pen.back(40)
pen.pendown()

for color in colors:
    pen.color(color)
    square_fun(color)
    pen.forward(50)
    pen.left(45)

pen.hideturtle()
t.done()
