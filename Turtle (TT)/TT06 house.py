import turtle
import math

t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(10)

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
      t.left(135)
      t.forward(length / math.sqrt(2))
      t.left(90)
      t.forward(length / math.sqrt(2))
      t.left(135)
      t.end_fill()

def drawParallelogram(t, width, height, color):
      t.fillcolor(color)
      t.begin_fill()
      t.left(30)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(120)
      t.forward(width)
      t.left(60)
      t.forward(height)
      t.left(90)
      t.end_fill()


t.penup() 
t.goto(-150, -120)
t.pendown()
drawRectangle(t, 100, 110, "dark blue")

t.penup()
t.goto(-120, -120)
t.pendown()
drawRectangle(t, 40, 60, "cornflower blue")

t.penup()
t.goto(-150, -10)
t.pendown()
drawTriangle(t, 100, "light blue")

t.penup()
t.goto(-50, -120)
t.pendown()
drawParallelogram(t, 60, 110, "black")

t.penup()
t.goto(-30, -60)
t.pendown()
drawParallelogram(t, 20, 30, "brown")

t.penup()
t.goto(-50, -10)
t.pendown()
t.fillcolor("grey")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(75)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(45)
t.end_fill()
t.hideturtle()
t.penup()

  
