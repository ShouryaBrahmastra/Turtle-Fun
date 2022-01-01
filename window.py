import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(2)
s.bgcolor("black")
t.penup()

t.goto(-50, 60)
t.pendown()

t.color("cyan")
t.begin_fill()

t.goto(100, 100)
t.goto(100, -100)
t.goto(-50, -60)
t.goto(-50, 60)
t.end_fill()

t.color("black")
t.goto(15, 100)
t.color("black")
t.width(10)
t.goto(15, -100)

t.penup()
t.goto(100, 0)
t.pendown()

t.goto(-100, 0)
