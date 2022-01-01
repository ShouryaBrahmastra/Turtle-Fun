import turtle as tu
import colorsys

t = tu.Turtle()
s = tu.Screen()
s.bgcolor('black')

t.speed(0)
h = 0

c = ("yellow", "red", "pink", "cyan", "light green", "blue")
for i in range(150):
    t.pencolor(c[i % 6])
    t.circle(190-i/2, 90)
    t.lt(90)
    t.circle(190-i/3, 90)
    t.lt(60)
s.exitonclick()
