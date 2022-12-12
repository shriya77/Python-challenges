import turtle

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.color("green", "cornflower blue")
t.pensize(2)
t.speed(15)

numbers = [10,20,30,50,100,200,300]

for length in numbers:
    draw_bar(t, length)

t.forward(30)
t.right(180)
t.forward(400)
t.right(90)
t.forward(400)

t.penup()
t.goto(-150,100)
t.pendown()
t.write("number of children")
t.penup()
t.goto(175,-40)
t.pendown()
t.write("age")

turtle.done()
