import turtle
sides = int(input("How many sides do you want in your polygon? "))
for i in range (sides):
     turtle.forward(20)
     turtle.right(360//sides)
