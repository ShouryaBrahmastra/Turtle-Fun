import turtle as tu

t = tu.Turtle()
s = tu.Screen()

s.bgcolor('black')

c = ("purple", "pink", "red", "cyan")

t.speed(0)

for i in range(150):
    t.pencolor(c[i % 4])
    t.circle(190-i, 90)
    t.lt(90)
    t.circle(190-i, 90)
    t.lt(18)
