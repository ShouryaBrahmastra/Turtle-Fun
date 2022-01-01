import turtle as tu
import colorsys

t = tu.Turtle()
s = tu.Screen()

s.bgcolor('black')

t.color("white")
t.speed(0)
t.width(5)
n = 200
h = 0

for i in range(200):
    t.right(59)
    for c in range(1):
        t.forward(i*2)
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h += 1/n
        t.color(c)

tu.exitonclick()
