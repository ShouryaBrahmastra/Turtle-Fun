import turtle
turtle.bgcolor("black")
artist = turtle.Turtle()
artist.speed(0)
artist.penup()
artist.left(90)
artist.goto(0, 0)
artist.forward(100)
artist.left(180)
artist.pendown()
j = 0
while(j <= 5):

    artist.pencolor("red")
    for i in range(150):
        artist.forward(100)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("dark blue")
    for i in range(150):
        artist.forward(102)
        artist.right(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(180*j)
    artist.pendown()

    artist.pencolor("dark violet")
    for i in range(150):
        artist.forward(104)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("dark red")
    for i in range(150):
        artist.forward(106)
        artist.right(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(180*j)
    artist.pendown()

    artist.pencolor("dark orange")
    for i in range(150):
        artist.forward(104)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("dark blue")
    for i in range(150):
        artist.forward(102)
        artist.right(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(180*j)
    artist.pendown()

    artist.pencolor("dark grey")
    for i in range(150):
        artist.forward(100)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("red")
    for i in range(150):
        artist.forward(100)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("dark blue")
    for i in range(150):
        artist.forward(102)
        artist.right(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(180*j)
    artist.pendown()

    artist.pencolor("dark violet")
    for i in range(150):
        artist.forward(104)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("dark red")
    for i in range(150):
        artist.forward(106)
        artist.right(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(180*j)
    artist.pendown()

    artist.pencolor("dark orange")
    for i in range(150):
        artist.forward(104)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

    artist.pencolor("dark blue")
    for i in range(150):
        artist.forward(102)
        artist.right(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(180*j)
    artist.pendown()

    artist.pencolor("dark grey")
    for i in range(150):
        artist.forward(100)
        artist.left(111)  # Let's go counterclockwise this time
    artist.penup()
    artist.right(90*j)
    artist.pendown()

j = j+1
turtle.done()
turtle.quit()
j = j+1
turtle.done()
turtle.quit()
