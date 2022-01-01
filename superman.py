import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor('navy')


def curve(value):
    for i in range(value):
        t.right(1)  # step by step curve
        t.forward(1)


t.penup()
t.setposition(0, 43)
t.pendown()
t.begin_fill()
t.pencolor('black')  # change the pen color to black
# change the shape fill color to maroon to match the Superman logo
t.fillcolor('maroon')
t.pensize(3)

t.forward(81.5)
t.right(49.4)
t.forward(58)
t.right(81.42)
t.forward(182)
t.right(98.36)
t.forward(182)
t.right(81.42)
t.forward(58)
t.right(49.4)
# move the pen forward by 81.5 to meet the start at the top of the shield
t.forward(81.5)
t.end_fill()
t.penup()

t.setposition(38, 32)
t.pendown()
t.begin_fill()
t.fillcolor('gold')  # change the fill color to gold to match the Superman logo
t.forward(13)
t.right(120)
t.forward(13)
t.right(120)
t.forward(13)
t.end_fill()  # the small triangle on the right is now complete
t.penup()

# now to create the larger yellow part of the Superman logo, change the position of the pen
t.setposition(81.5, 25)
t.pendown()
t.begin_fill()
t.right(210)
t.forward(25)
t.right(90)
t.forward(38)
t.right(45)
t.circle(82, 90)  # this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
t.left(90)
# create a circle of radius 82 and only complete 60 degrees of the circle
t.circle(82, 60)
curve(61)
t.left(90)
t.forward(57)
t.left(90)
t.forward(32)
t.end_fill()  # fill in the larger yellow part of the logo
t.penup()  # stop drawing
t.home()  # reset the pen location to the origin so the orientation is also reset

# finish the major parts of the S superimposition on the shield
t.setposition(-69, -38)
t.pendown()
t.begin_fill()
curve(20)
t.forward(33)
t.left(10)
t.circle(82, 20)
curve(30)
t.forward(10)
t.right(110)
curve(40)
t.right(10)
t.circle(50, 10)
curve(45)
t.right(5)
t.forward(45)
t.end_fill()
t.penup()
t.home()

t.setposition(20, -100)
t.pendown()
t.begin_fill()
t.right(135)
t.forward(27)
t.right(90)
t.forward(27)
t.right(135)
t.forward(38.18)
t.end_fill()
t.penup()
t.home()

t.setposition(-57, 32)
t.pendown()
t.begin_fill()
t.right(180)
t.forward(18)
t.left(45)
t.forward(44)
t.left(80)
t.forward(15)
t.left(130)
curve(40)
t.forward(20)
t.end_fill()

t.hideturtle()  # use this command to hide the turtle so it is not visible in the final image
